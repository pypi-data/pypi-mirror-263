import os

from komodo.core.vector_stores.qdrant_store import QdrantStore
from komodo.shared.utils.digest import get_text_digest
from komodo.store.collection_store import CollectionStore


class RagContext:
    def __init__(self, path, collection_name=None, top_k=5):
        self.path = path
        self.top_k = top_k
        self.collection_name = get_text_digest(str(path)) if collection_name is None else collection_name
        CollectionStore().get_or_create_collection(self.collection_name)
        print(f"Created RagContext for path: {self.path} and collection_name: {self.collection_name}")

    def basename(self):
        return os.path.basename(self.path)

    def collection(self):
        return CollectionStore().retrieve_collection(self.collection_name)

    def qdrant_collection(self):
        return QdrantStore.create(self.collection_name)

    def reset_all(self):
        store = QdrantStore.create(self.collection_name)
        store.delete_all()
        store = CollectionStore()
        store.reset_default_collection(self.collection_name)

    def search(self, text):
        print(f"Searching Qdrant collection: {self.collection_name}")
        store = QdrantStore.create(self.collection_name)
        store.get_collection()
        return store.search(text, top_k=self.top_k)
