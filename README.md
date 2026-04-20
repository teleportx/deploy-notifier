# Deploy notifier
API interface for send deploy status notification in telegram chat. 

## Using

Send a `POST` request to `/` with body:
```json
{
 "app_name": "cool app",
 "message": "text sent with deploy message",
 "success": true
}
```
And specify header `Authorization` with `AUTH` env.

Get result:

![image](https://github.com/user-attachments/assets/875c4d9a-7bec-476a-935a-46e6813a5ef0)


## Installation

`docker-compose.yml`
```yml
services:
  bot:
    image: teleportx/deploy-notifier:latest
    environment:
      - TOKEN=<TELEGRAM_TOKEN>
      - CHAT_ID=<TELEGRAM_CHAR_ID_HERE>
      - AUTH=<PASSWORD_TO_ACCESS_TO_THE_API>
    restart: unless-stopped
    ports:
      - 19098:80
```

### Env
- `TOKEN` - Telegram bot token. Obtain in [BotFather](https://t.me/BotFather).
- `CHAT_ID` - Telegram chat id.
- `THREAD_ID` _(optional)_ - Telegram char thread id.
- `AUTH` - Password to use this API.
