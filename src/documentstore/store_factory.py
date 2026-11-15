from interfaces import DocumentStore
from memory_store import InMemoryDocumentStore
from sql_store import SQLiteDocumentStore


def create_store(store_type: str, database_path: str = "documents.db") -> DocumentStore:

    if store_type == "memory":
        return InMemoryDocumentStore()

    elif store_type == "sqlite":
        return SQLiteDocumentStore(database_path)

    else:
        raise ValueError(f"Unsupported store type: {store_type}")
