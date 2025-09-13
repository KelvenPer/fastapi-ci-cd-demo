from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_rout():
    return {"ok": True, "msg": "Hello from FastAPI on Docker"}