from fastapi import FastAPI

app = FastAPI()

@app.get("/dev")
def read_cv():
    message =  "Hello this is my first app in FastApi"
    return {message}

@app.get("/")
async def root():
    return {"message": "Hello World"}