from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn
from environment import VERSION


app = FastAPI()


@app.get("/")
def get_health() -> ORJSONResponse:
    return ORJSONResponse(content={"version": VERSION})


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
