import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == '__main__':
    # 命令为: python -m uvicorn main:app --reload
    uvicorn.run(app="main:app", host="0.0.0.0", port=5454, reload=True,workers=10)