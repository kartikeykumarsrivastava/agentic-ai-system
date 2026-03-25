from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "Eligibility service running"}