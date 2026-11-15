from abc import ABC, abstractmethod


class DocumentStore(ABC):
    @abstractmethod
    def add(self, document):
        pass

    @abstractmethod
    def get(self, document_id):
        pass

    @abstractmethod
    def delete(self, document_id):
        pass

    @abstractmethod
    def list_all(self):
        pass
