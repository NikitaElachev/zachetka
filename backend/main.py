import os

import psycopg
from fastapi import FastAPI

app = FastAPI(title="АС «Моя зачетка»")


def db():
    conn = psycopg.connect(os.environ["DATABASE_URL"], autocommit=True)
    conn.execute("CREATE TABLE IF NOT EXISTS discipline (name text PRIMARY KEY)")
    return conn


@app.get("/api/health")
def health():
    return {"status": "ok", "system": "Зачетка"}


@app.get("/api/disciplines")
def list_disciplines():
    with db() as conn:
        rows = conn.execute("SELECT name FROM discipline ORDER BY name")
        return [row[0] for row in rows]


@app.post("/api/disciplines")
def add_discipline(name: str):
    with db() as conn:
        conn.execute("INSERT INTO discipline (name) VALUES (%s)", (name,))
    return {"added": name}
