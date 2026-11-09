from fastapi import FastAPI

app = FastAPI(title="АС «Зачетка»")


@app.get("/api/health")
def health():
    return {"status": "ok", "system": "Зачетка"}
