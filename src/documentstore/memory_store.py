from interfaces import DocumentStore


class InMemoryDocumentStore(DocumentStore):
    def __init__(self):
        self.documents = {}

    def add(self, document):
        document_id = document.id
        if document_id in self.documents:
            raise ValueError("Document ID already exists")
        self.documents[document_id] = document

    def get(self, document_id):

        return self.documents.get(document_id)

    def delete(self, document_id):
        try:
            del self.documents[document_id]
            return True
        except KeyError:
            return False

    def list_all(self):
        return list(self.documents.values())
