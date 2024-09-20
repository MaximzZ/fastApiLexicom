from fastapi import FastAPI, HTTPException
from app.schemas import WriteDataRequest

from app.redis_client import redis_client
from app.routes import router

app = FastAPI()
app.include_router(router)


# Эндпоинт для записи или обновления данных
@app.post("/write_data")
def write_data(request: WriteDataRequest):
    redis_client.hset(request.phone, "address", request.address)
    return {"message": "Data saved successfully"}

# Эндпоинт для проверки данных
@app.get("/check_data")
def check_data(phone: str):
    address = redis_client.hget(phone, "address")
    if address:
        return {"phone": phone, "address": address.decode()}
    raise HTTPException(status_code=404, detail="Phone number not found")
