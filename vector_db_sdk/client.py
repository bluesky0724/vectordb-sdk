import requests
from .exceptions import APIError
from .models import Library, Document, Chunk

class VectorDBClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _request(self, method: str, endpoint: str, data: dict = None, params: dict = None, headers: dict = None):
        url = f"{self.base_url}{endpoint}"
        headers = headers or {"accept": "application/json", "Content-Type": "application/json"}
        print(f"Request: {method} {url}, Params: {params}, Headers: {headers}, Data: {data}")  # Debug
        try:
            response = requests.request(method, url, json=data, params=params, headers=headers)
            response.raise_for_status()
            response_data = response.json() if response.content else {}
            print(f"Response: {response.status_code}, Headers: {response.headers}, Data: {response_data}")  # Debug
            return response_data
        except requests.exceptions.HTTPError as e:
            error_detail = response.json() if response.content else str(e)
            print(f"Error: {response.status_code}, Detail: {error_detail}")  # Debug
            raise APIError(response.status_code, error_detail)

    def create_library(self, library: Library) -> dict:
        return self._request("POST", "/libraries", data=library.model_dump())

    def get_library(self, library_id: str) -> dict:
        return self._request("GET", f"/libraries/{library_id}")
    
    def update_library(self, library_id: str, library: Library) -> dict:
        return self._request("PATCH", f"/libraries/{library_id}", data=library.model_dump())
    
    def delete_library(self, library_id: str):
        return self._request("DELETE", f"/libraries/{library_id}")

    def add_document(self, library_id: str, document: Document) -> dict:
        return self._request("POST", "/documents", data=document.model_dump(), params={"library_id": library_id})
    
    def get_document(self, library_id: str, document_id: str) -> dict:
        return self._request("GET", f"/documents/{document_id}", params={"library_id": library_id})
    
    def delete_document(self, library_id: str, document_id: str):
        return self._request("DELETE", f"/documents/{document_id}", params={"library_id": library_id})
    
    def update_document(self, library_id: str, document_id: str, document: Document) -> dict:
        return self._request("PATCH", f"/documents/{document_id}", data=document.model_dump(), params={"library_id": library_id})

    def add_chunk(self, library_id: str, document_id: str, chunk: Chunk) -> dict:
        return self._request(
            "POST",
            "/chunks/",
            data=chunk.model_dump(),
            params={"library_id": library_id, "document_id": document_id},
        )
    
    def get_chunk(self, chunk_id: str) -> dict:
        return self._request("GET", f"/chunks/{chunk_id}")
    
    def update_chunk(self, chunk_id: str, chunk: Chunk) -> dict:
        return self._request(
            "PATCH",
            f"/chunks/{chunk_id}",
            data=chunk.model_dump()
        )

    def delete_chunk(self, chunk_id: str):
        return self._request("DELETE", f"/chunks/{chunk_id}")
    
    def search_all_libraries(self, query_text: str, metadata_filters: dict) -> list:
        data = {"query_text": query_text, "metadata_filters": metadata_filters}
        return self._request("POST", "/search", data=data)