from fastapi import FastAPI
#建立fastAPI物件
app = FastAPI()

@app.get("/")
def level1():
    return {"Hello": "level 1"}

@app.get("/blog/all")
def level2():
    return {"Hello": "level 2"}

@app.get("/blog/{id}")
def read_root(id: int):
    return {"Hello": f"FastAPI: {id}"}