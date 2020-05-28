from fastapi import BackgroundTasks
import time
from pydantic import EmailStr
from fastapi import APIRouter, BackgroundTasks

router = APIRouter()


def write_log(message: str):
    time.sleep(10)
    with open("log.txt", mode="a") as log:
        log.write(message)


@router.post("/send/{email}")
async def send_notification(
        email: EmailStr, background_tasks: BackgroundTasks
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}
