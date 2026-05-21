from src.api_server import create_app

if __name__ == "__main__":
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)