from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def receive_sms(request: Request):
    data = await request.json()
    print("DaisySMS", data)
    return {"status": "success"}

@app.get("/")
def home():
    return {"message": "DaisySMS webhook ✅"}
