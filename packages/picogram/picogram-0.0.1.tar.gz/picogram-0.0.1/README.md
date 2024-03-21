# picogram
small api library for telegram bot api


Installation:
```shell
pip install picogram
```


Example:

```python
from picogram import Bot

bot = Bot(token='your_token')


@bot.message()
def start_message(message: dict):
    bot.send_message(chat_id=message['chat']['id'], text='Hello!')


if __name__ == '__main__':
    bot.run_polling()
```
