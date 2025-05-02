# use_sdk.py
from vector_db_sdk import VectorDBClient, Library, Document, Chunk, LibraryMetadata
from vector_db_sdk.models import DocumentMetadata, ChunkMetadata
from datetime import datetime

# Initialize the client
client = VectorDBClient(
    base_url="http://localhost:8000",
    chunk_endpoint="/documents/{document_id}/chunks"  # Adjust if needed
)

# Create a library
library = Library(
    name="My Library",
    metadata=LibraryMetadata(
        name="My Library",
        createdAt=datetime.now().isoformat(),
        description="A test library"
    )
)
library_response = client.create_library(library)
library_id = library_response["id"]
print(f"\n``````Created library with ID: {library_id}``````\n")

# Verify library exists
library_check = client.get_library(library_id)
print(f"\n``````Verified library: {library_check}``````\n")

# Add a document
document = Document(
    metadata=DocumentMetadata(
        name="Sample Document",
        createdAt=datetime.now().isoformat()
    )
)
document_response = client.add_document(library_id, document)
document_id = document_response["id"]
print(f"\n``````Added document with ID: {document_id}``````\n")


# Add a chunk
chunk = Chunk(
    text="Hello World",
    metadata=ChunkMetadata(
        name="Kevin",
        createdAt=datetime.now().isoformat()
        )
    )
chunk_response = client.add_chunk(library_id, document_id, chunk)
chunk_id = chunk_response["chunk_id"]
print(f"\n``````Added chunk with ID: {chunk_id}``````\n")

# Add a chunk
chunk = Chunk(
    text="Good Bye",
    metadata=ChunkMetadata(
        name="Kevin",
        createdAt=datetime.now().isoformat()
        )
    )
chunk_response = client.add_chunk(library_id, document_id, chunk)
chunk_id = chunk_response["chunk_id"]
print(f"\n``````Added chunk with ID: {chunk_id}``````\n")

# Add a chunk
chunk = Chunk(
    text="New World",
    metadata=ChunkMetadata(
        name="Kevin",
        createdAt=datetime.now().isoformat()
        )
    )
chunk_response = client.add_chunk(library_id, document_id, chunk)
chunk_id = chunk_response["chunk_id"]
print(f"\n``````Added chunk with ID: {chunk_id}``````\n")

# Search across libraries
results = client.search_all_libraries(
            query_text="hello",
            metadata_filters={"name": "kevin", "createdAfter": "2025-04-29"}
        )
for result in results:
    print(f"\n``````Search result: {result["chunk"]["text"]} - {result["similarity"]}``````\n")

# Delete the chunk
client.delete_chunk(chunk_id)
print(f"\n``````Deleted chunk with ID: {chunk_id}``````\n")