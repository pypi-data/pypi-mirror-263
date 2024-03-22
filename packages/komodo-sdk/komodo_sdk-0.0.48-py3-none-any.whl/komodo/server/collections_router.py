import json
import os
from typing import List

import aiofiles
from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi import File, UploadFile
from google.protobuf import json_format
from starlette.responses import FileResponse
from werkzeug.utils import secure_filename

from komodo.server.globals import get_email_from_header, get_appliance
from komodo.shared.utils.filestats import file_details
from komodo.store.collection_store import CollectionStore

router = APIRouter(
    prefix='/api/v1/collections',
    tags=['Collections']
)


@router.post('/')
async def create_collection(request: Request, email=Depends(get_email_from_header)):
    # Parse the request body as JSON
    body = await request.json()
    collection_name = body.get("collection")
    description = body.get("description")
    shortcode = body.get("shortcode") or ''
    if not collection_name:
        raise HTTPException(status_code=400, detail="Missing 'collection_name' in Request")

    try:
        collections_store = CollectionStore()
        collection = collections_store.get_or_create_collection(shortcode, collection_name, description)
        collections_store.add_user_collection(email, collection.shortcode)
        collection_dict = json.loads(json_format.MessageToJson(collection))
        return collection_dict
    except:
        raise HTTPException(status_code=500, detail="Failed to create collection")


@router.get('/')
async def list_collection():
    collections_store = CollectionStore()
    collections = collections_store.retrieve_all_collections()
    response = []
    for collection in collections:
        try:
            collection_dict = json.loads(json_format.MessageToJson(collection))
            collection_dict['guid'] = collection.shortcode
            if 'files' in collection_dict:
                del collection_dict['files']
            response.append(collection_dict)
        except Exception as e:
            print("Failed to list collection with shortcode: ", collection.shortcode, e)

    return response


@router.get('/{shortcode}')
async def get_collection(shortcode: str):
    collections_store = CollectionStore()
    try:
        collection = collections_store.retrieve_collection(shortcode)
        collection_dict = json.loads(json_format.MessageToJson(collection))
        return collection_dict
    except Exception:
        raise HTTPException(status_code=404, detail="Collection not found")


@router.delete('/{shortcode}')
async def delete_collection(shortcode: str):
    try:
        collections_store = CollectionStore()
        response = collections_store.remove_collection(shortcode)
        return response
    except Exception:
        raise HTTPException(status_code=404, detail="Error deleting collection: " + shortcode)


@router.delete('/everything/forsure')
async def delete_all_collections():
    try:
        store = CollectionStore()
        store.remove_everything()
        return {"message": "Successfully deleted all collections"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error deleting collections: " + str(e))


@router.post("/upload_files/{shortcode}")
async def upload(shortcode, files: List[UploadFile] = File(...), appliance=Depends(get_appliance)):
    try:
        collections_store = CollectionStore()
        collection = get_collection_from_store(shortcode)

        folder = appliance.config.data_dir() / collection.path

        for file in files:
            filepath = await get_writable_filepath(folder, file.filename)
            contents = await file.read()
            async with aiofiles.open(filepath, 'wb') as f:
                await f.write(contents)

            await update_file_in_collection(collection, filepath)

        collections_store.store_collection(collection)
        collection_dict = json.loads(json_format.MessageToJson(collection))

    except Exception as e:
        return {"message": "There was an error uploading the file: " + str(e)}

    return {"message": f"Successfully uploaded {[file.filename for file in files]}", "collection": collection_dict}


def get_collection_from_store(shortcode):
    collections_store = CollectionStore()
    collection = collections_store.retrieve_collection(shortcode)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection


async def get_writable_filepath(folder, filename):
    filename = os.path.basename(secure_filename(os.path.basename(filename)))
    filepath = folder / filename
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    return filepath


async def update_file_in_collection(collection, filepath):
    updated_files = []
    for file in collection.files or []:
        if file.path != str(filepath):
            updated_files.append(file)

    uploaded = file_details(str(filepath))
    updated_files.append(uploaded)

    del collection.files[:]
    collection.files.extend(updated_files)
    return collection


@router.post('/upload_stream/{shortcode}')
async def upload_stream(shortcode, request: Request, appliance=Depends(get_appliance)):
    try:
        collection = get_collection_from_store(shortcode)

        folder = appliance.config.data_dir() / collection.path
        filename = request.headers['filename']
        filepath = await get_writable_filepath(folder, filename)

        async with aiofiles.open(filepath, 'wb') as f:
            async for chunk in request.stream():
                await f.write(chunk)

        await update_file_in_collection(collection, filepath)

        collections_store = CollectionStore()
        collections_store.store_collection(collection)
        collection_dict = json.loads(json_format.MessageToJson(collection))

    except Exception as e:
        return {"message": "There was an error uploading the file: " + str(e)}

    return {"message": f"Successfully uploaded {filename}", "collection": collection_dict}


@router.get('/{shortcode}/{file_guid}')
def download_file(shortcode: str, file_guid: str):
    collection = get_collection_from_store(shortcode)

    for file in collection.files:
        if file.guid == file_guid:
            return FileResponse(file.path, media_type='application/octet-stream', filename=file.name)

    raise HTTPException(status_code=404, detail="File not found")


@router.delete('/{shortcode}/{file_guid}')
async def remove_file(shortcode: str, file_guid: str):
    collections_store = CollectionStore()
    collection = get_collection_from_store(shortcode)

    for file in collection.files:
        if file.guid == file_guid:
            collection.files.remove(file)
            collections_store.store_collection(collection)
            return {"message": "File removed"}

    raise HTTPException(status_code=404, detail="File not found")
