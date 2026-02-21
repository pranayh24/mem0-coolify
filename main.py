from fastapi import FastAPI
from mem0 import Memory

app = FastAPI(title="Mem0 Service")

memory = Memory()

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
