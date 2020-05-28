from fastapi import BackgroundTasks
import time
from pydantic import EmailStr
from . import api_router


def write_log(message: str):
    time.sleep(10)
    with open("log.txt", mode="a") as log:
        log.write(message)


@api_router.post("/send/{email}")
async def send_notification(
        email: EmailStr, background_tasks: BackgroundTasks
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}
