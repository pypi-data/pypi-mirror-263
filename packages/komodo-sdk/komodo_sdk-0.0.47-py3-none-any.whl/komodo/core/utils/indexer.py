import time
from datetime import datetime

from komodo.core.utils.rag_context import RagContext
from komodo.core.vector_stores.qdrant_store import QdrantStore
from komodo.core.vector_stores.vector_store_helper import VectorStoreHelper
from komodo.shared.utils.filestats import file_details
from komodo.shared.utils.globber import Globber
from komodo.store.collection_store import CollectionStore


class Indexer:
    def __init__(self, rag_context: RagContext):
        self.rag_context = rag_context
        self.globber = Globber(rag_context.path, self.__on_created, self.__on_deleted)

    def __on_created(self, filepath):
        print("Created: " + filepath)
        collection = self.rag_context.collection()

        print("Searching for: " + filepath + " in collection: " + self.rag_context.collection_name)
        file = self.find_file(collection, filepath)
        if not file:
            file = file_details(filepath)
            collection.files.append(file)

        file = self.find_file(collection, filepath)
        if file and file.indexed_at:
            print("Already indexed: " + filepath + " in collection: " + self.rag_context.collection_name)
            return

        self.index(filepath)
        file.indexed_at = datetime.utcnow().isoformat() + 'Z'

        store = CollectionStore()
        store.store_collection(collection)

    def __on_deleted(self, filepath):
        print("Deleted: " + filepath)
        collection = self.rag_context.collection()
        file = self.find_file(collection, filepath)
        if file:
            self.remove(filepath)
            collection.files.remove(file)
            store.store_collection(collection)

    @staticmethod
    def find_file(collection, filepath):
        for file in collection.files or []:
            if file.path == filepath:
                return file
        return None

    def index(self, filepath):
        print("Indexing: " + filepath + " into collection: " + self.rag_context.collection_name)
        collection = self.rag_context.qdrant_collection()
        helper = VectorStoreHelper(filepath)
        try:
            text = helper.text
            data = helper.data
            if data:
                print("Content: " + text[:60])
                collection.upsert_batched(data)
            else:
                print("Data could not be extracted from: " + filepath)
        except Exception as e:
            print("Error indexing: " + filepath)
            print(e)

    def add_intelligence(self, filepath):
        print("Adding intelligence to: " + filepath)

    def remove(self, filepath):
        print("Removing from index: " + filepath)
        collection = self.rag_context.qdrant_collection()
        collection.delete_all_by_source(filepath)

    def run(self, max_updates=1, update_interval=5, reindex=False):
        if reindex:
            print("Reindexing...")
            self.rag_context.reset_all()

        self.globber.start()
        update_count = 1  # start runs the initial update
        while update_count < max_updates or max_updates == 0:
            time.sleep(update_interval)
            self.globber.updates()
            update_count += 1

        print("Indexed. Looped " + str(update_count) + " times. Stopping...")


if __name__ == "__main__":
    qdrant = QdrantStore.create("test")
    store = CollectionStore()
    collection = store.get_or_create_collection("default", "My Collection", "My personal collection")
    path = '/Users/komodo/dev/komodo-sdk/sample/data/komodo'  # os.path.dirname(__file__)
    rag_context = RagContext(path, "default")
    indexer = Indexer(rag_context)
    indexer.run(update_interval=5)
