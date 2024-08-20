from os import environ

from aiogram import Bot
from aiogram.utils.formatting import Text, Bold, Code
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()
bot = Bot(environ.get('TOKEN'))

auth = environ.get('AUTH')

chat_id = environ.get('CHAT_ID')
thread_id = environ.get('THREAD_ID')

if thread_id is not None:
    thread_id = int(thread_id)


class SendNotifyModel(BaseModel):
    app_name: str
    message: str
    success: bool


@app.post('/', status_code=204)
async def root(request: Request, body: SendNotifyModel):
    if request.headers.get('Authorization') != auth:
        return JSONResponse({"detail": "Bad Authorizaion token"}, status_code=401)

    if body.success:
        header_text = f'✅ Success deploy '

    else:
        header_text = f'❌ Failed deploy '

    await bot.send_message(chat_id, **Text(
        Bold(header_text), Code(body.app_name), '\n',
        body.message
    ).as_kwargs(), message_thread_id=thread_id)
