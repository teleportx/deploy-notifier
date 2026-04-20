from os import environ

from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer


telegram_bot_api_server = environ.get('TELEGRAM_BOT_API_SERVER')

def get_bot_api_session():
    if telegram_bot_api_server is None:
        return None

    return AiohttpSession(
        api=TelegramAPIServer(
            base=f'{telegram_bot_api_server}/bot{{token}}/{{method}}',
            file=f'{telegram_bot_api_server}/file{{path}}',
        )
    )
