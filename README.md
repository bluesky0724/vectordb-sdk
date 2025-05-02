# VectorDB Python SDK

This Python SDK provides a convenient interface to interact with the VectorDB API, allowing you to manage libraries, documents, chunks, and perform searches. Below is a guide to get started and use the SDK effectively.

## Installation

To use the VectorDB Python SDK, install it via pip (assuming the package is published to PyPI) or clone the repository and install dependencies.

```bash
pip install vectordb-sdk
```

Alternatively, if you have the source code:

```bash
git clone https://github.com/bluesky0724/vectordb-sdk.git
cd vectordb-sdk
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The SDK depends on the `requests` library for HTTP requests and `pydantic` for data modeling.

## Getting Started

To use the SDK, you need the base URL of your VectorDB API. Initialize the `VectorDBClient` with the base URL and, optionally, a custom chunk endpoint.

```python
from vectordb import VectorDBClient, Library, Document, Chunk

# Initialize the client
client = VectorDBClient(base_url="https://your-vectordb-api.com")
```

## Usage Examples

### 1. Managing Libraries

Create, retrieve, update, or delete libraries.

```python
# Create a library
library = Library(name="MyLibrary", description="A test library")
response = client.create_library(library)
print(response)  # Library details

# Get a library
library_id = "lib_123"
response = client.get_library(library_id)
print(response)  # Library details

# Update a library
updated_library = Library(name="UpdatedLibrary", description="Updated description")
response = client.update_library(library_id, updated_library)
print(response)  # Updated library details

# Delete a library
client.delete_library(library_id)
```

### 2. Managing Documents

Add, retrieve, update, or delete documents within a library.

```python
# Add a document
document = Document(title="Sample Doc", content="This is a test document")
library_id = "lib_123"
response = client.add_document(library_id, document)
print(response)  # Document details

# Get a document
document_id = "doc_456"
response = client.get_document(library_id, document_id)
print(response)  # Document details

# Update a document
updated_document = Document(title="Updated Doc", content="Updated content")
response = client.update_document(library_id, document_id, updated_document)
print(response)  # Updated document details

# Delete a document
client.delete_document(library_id, document_id)
```

### 3. Managing Chunks

Add, retrieve, update, or delete chunks within a document.

```python
# Add a chunk
chunk = Chunk(content="This is a chunk of text", metadata={"key": "value"})
library_id = "lib_123"
document_id = "doc_456"
response = client.add_chunk(library_id, document_id, chunk)
print(response)  # Chunk details

# Get a chunk
chunk_id = "chunk_789"
response = client.get_chunk(chunk_id)
print(response)  # Chunk details

# Update a chunk
updated_chunk = Chunk(content="Updated chunk text", metadata={"key": "new_value"})
response = client.update_chunk(chunk_id, updated_chunk)
print(response)  # Updated chunk details

# Delete a chunk
client.delete_chunk(chunk_id)
```

### 4. Searching Libraries

Perform a search across all libraries with a query and optional metadata filters.

```python
query_text = "test query"
metadata_filters = {"category": "test"}
results = client.search_all_libraries(query_text, metadata_filters)
print(results)  # List of search results
```

## Error Handling

The SDK raises an `APIError` for HTTP errors, providing the status code and error details.

```python
from vectordb.exceptions import APIError

try:
    response = client.get_library("non_existent_id")
except APIError as e:
    print(f"Error {e.status_code}: {e.detail}")
```

## Debugging

The SDK includes debug logging for requests and responses, printing the method, URL, headers, parameters, data, and response details. To disable or customize this, modify the `_request` method in `VectorDBClient`.

## Models

The SDK uses Pydantic models for data validation:

- `Library`: Represents a library with fields like `name` and `description`.
- `Document`: Represents a document with fields like `title` and `content`.
- `Chunk`: Represents a chunk with fields like `content` and `metadata`.

You can extend these models by defining additional fields in your `Library`, `Document`, or `Chunk` classes, as long as they align with the API's expectations.