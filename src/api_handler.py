import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

from query_rag import QueryResponse, query_rag

app = FastAPI()
handler = Mangum(app)  # Entry point for AWS Lambda


class SubmitQueryRequest(BaseModel):
    query_text: str


@app.get("/")
def index():
    return {"hii": "lemon"}


@app.post("/submit_query")
def submit_query_endpoint(request: SubmitQueryRequest) -> QueryResponse:
    query_response = query_rag(request.query_text)
    return query_response


if __name__ == "__main__":
    port = 8000
    print(f"Running the FastAPI server on port {port}")
    uvicorn.run("api_handler:app", host="0.0.0.0", port=port)
