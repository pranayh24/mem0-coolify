from fastapi import FastAPI
from mem0 import Memory
import os

app = FastAPI(title="Mem0 Service")

memory = Memory.from_config({
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "url": os.getenv("QDRANT_URL", "http://qdrant:6333"),
        },
    }
})

@app.get("/")
def health():
    return {"status": "mem0 running"}

@app.post("/remember")
def remember(text: str, user_id: str = "default"):
    memory.add(text, user_id=user_id)
    return {"status": "stored"}

@app.get("/recall")
def recall(query: str, user_id: str = "default"):
    results = memory.search(query, user_id=user_id)
    return {"results": results}
