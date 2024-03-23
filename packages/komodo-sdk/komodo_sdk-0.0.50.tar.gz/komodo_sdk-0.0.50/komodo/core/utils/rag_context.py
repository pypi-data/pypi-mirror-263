from komodo.core.vector_stores.qdrant_store import QdrantStore
from komodo.core.vector_stores.vector_store_helper import VectorStoreHelper
from komodo.shared.utils.digest import get_text_digest
from komodo.shared.utils.term_colors import print_error
from komodo.store.collection_store import CollectionStore


class RagContext:
    def __init__(self, path, shortcode=None, top_k=5):
        self.shortcode = get_text_digest(str(path))[:6] if shortcode is None else shortcode
        self.path = path
        self.top_k = top_k
        collection_store = CollectionStore()
        collection_store.get_or_create_collection(shortcode=self.shortcode, path=path)
        print(f"Created RagContext for path: {self.path} and shortcode: {self.shortcode}")

    def find_file(self, filepath):
        print("Searching for: " + filepath + " in collection: " + self.shortcode)
        collection_store = CollectionStore()
        collection = collection_store.retrieve_collection(self.shortcode)
        if not collection:
            print_error("Collection not found for shortcode: " + self.shortcode)
            return None
        return collection_store.find_file_in_collection(collection, filepath)

    def update_file(self, filepath, file):
        print("Updating: " + filepath + " in collection: " + self.shortcode)
        collection_store = CollectionStore()
        collection = collection_store.retrieve_collection(self.shortcode)
        collection_store.upsert_file_in_collection(collection, file)
        collection_store.store_collection(collection)

    def index(self, filepath):
        print("Indexing: " + filepath + " into collection: " + self.shortcode)
        helper = VectorStoreHelper(filepath)
        try:
            text = helper.text
            data = helper.data
            if data:
                print("Content: " + text[:60])
                qdrant_store = QdrantStore.create(self.shortcode)
                qdrant_store.upsert_batched(data)
            else:
                print("Data could not be extracted from: " + filepath)
        except Exception as e:
            print("Error indexing: " + filepath)
            print(e)

    def search(self, text):
        print(f"Searching Qdrant collection: {self.shortcode}")
        qdrant_store = QdrantStore.create(self.shortcode)
        return qdrant_store.search(text, top_k=self.top_k)

    def remove(self, filepath):
        print("Removing: " + filepath + " from rag context: " + self.shortcode)
        print("Removing from index: " + filepath)
        qdrant_store = QdrantStore.create(self.shortcode)
        qdrant_store.delete_all_by_source(filepath)

        print("Removing from collection: " + filepath)
        file = self.find_file(filepath)
        if file:
            collection_store = CollectionStore()
            collection = collection_store.retrieve_collection(self.shortcode)
            collection.files.remove(file)
            collection_store.store_collection(collection)

    def reset_all(self):
        qdrant_store = QdrantStore.create(self.shortcode)
        qdrant_store.delete_all()
        collection_store = CollectionStore()
        collection_store.remove_collection(self.shortcode)
