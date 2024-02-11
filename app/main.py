from fastapi import FastAPI
from uvicorn import run


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Health Check OK!"}


if __name__ == "__main__":
    run("app.main:app", host="0.0.0.0", port=8000, reload=False)

