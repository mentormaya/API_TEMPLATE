import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="app.main:api", host="localhost", port=8000, reload=True)