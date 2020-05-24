from fastapi import APIRouter, BackgroundTasks

from api.api_v1.endpoints import items

api_router = APIRouter()
api_router.include_router(items.router, tags=["items"])


def write_log(message: str):
    import time
    time.sleep(10)
    with open("log.txt", mode="a") as log:
        log.write(message)


@app.post("/send-notification/{email}")
async def send_notification(
        email: str, background_tasks: BackgroundTasks
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}
