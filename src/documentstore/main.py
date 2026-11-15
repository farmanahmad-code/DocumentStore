import argparse

from document_service import DocumentService
from models import Document
from sql_store import SQLiteDocumentStore
from store_factory import create_store


def main():

    parser = argparse.ArgumentParser(description="Document Store CLI")

    parser.add_argument(
        "--store",
        choices=["memory", "sqlite"],
        default="memory",
        help="Storage backend",
    )

    parser.add_argument(
        "--db-path", default="documents.db", help="SQLite database file path"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--id", type=int, required=True)
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--author", required=True)

    # Get command
    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("--id", type=int, required=True)

    # List command
    subparsers.add_parser("list")

    # Delete command
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    args = parser.parse_args()

    store = create_store(args.store, args.db_path)
    service = DocumentService(store)

    try:
        if args.command == "add":
            document = Document(id=args.id, title=args.title, author=args.author)

            service.add_document(document)
            print("Document added successfully")

        elif args.command == "get":
            document = service.get_document(args.id)
            print(document if document else "Document not found")

        elif args.command == "list":
            documents = service.get_all_documents()

            for document in documents:
                print(document)

        elif args.command == "delete":
            deleted = service.delete_document(args.id)
            print("Document deleted" if deleted else "Document not found")

    except ValueError as exc:
        print(f"Error: {exc}")

    finally:
        if isinstance(store, SQLiteDocumentStore):
            store.close()


if __name__ == "__main__":
    main()
