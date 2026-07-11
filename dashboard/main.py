from fastapi import FastAPI

app = FastAPI(title="Algo Trading Bot Dashboard")


@app.get("/health")
def health_check() -> dict:
    """
    Simple endpoint to verify the server is running.
    Returns a basic status message.
    """
    return {"status": "ok", "message": "Algo Trading Bot API is running"}