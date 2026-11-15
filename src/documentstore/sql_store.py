import sqlite3

from interfaces import DocumentStore
from models import Document


class SQLiteDocumentStore(DocumentStore):
    def __init__(self, database_path: str):
        self.connection = sqlite3.connect(database_path)
        self._create_table()

    def _create_table(self) -> None:
        query = """
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add(self, document: Document) -> None:
        try:
            self.connection.execute(
                """
                INSERT INTO documents (id, title, author)
                VALUES (?, ?, ?)
                """,
                (document.id, document.title, document.author),
            )
            self.connection.commit()

        except sqlite3.IntegrityError as exc:
            raise ValueError("Document ID already exists") from exc

    def get(self, document_id: int) -> Document | None:
        cursor = self.connection.execute(
            """
            SELECT id, title, author
            FROM documents
            WHERE id = ?
            """,
            (document_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Document(id=row[0], title=row[1], author=row[2])

    def delete(self, document_id: int) -> bool:
        cursor = self.connection.execute(
            "DELETE FROM documents WHERE id = ?", (document_id,)
        )

        self.connection.commit()

        return cursor.rowcount > 0

    def list_all(self) -> list[Document]:
        cursor = self.connection.execute(
            """
            SELECT id, title, author
            FROM documents
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        return [Document(id=row[0], title=row[1], author=row[2]) for row in rows]

    def close(self) -> None:
        self.connection.close()
