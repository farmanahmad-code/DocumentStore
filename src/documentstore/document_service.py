from interfaces import DocumentStore
from models import Document


class DocumentService:
    def __init__(self, store: DocumentStore):
        self.store = store

    def add_document(self, document: Document) -> None:
        self.store.add(document)

    def get_document(self, document_id: int) -> Document | None:
        return self.store.get(document_id)

    def delete_document(self, document_id: int) -> bool:
        return self.store.delete(document_id)

    def get_all_documents(self) -> list[Document]:
        return self.store.list_all()
