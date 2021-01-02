# Private-Redirect-Bot
This simple python Bot will redirect the messages sent to him in private to your chat/channel

### Libraries used:
* [Python-telegram-bot library](https://github.com/python-telegram-bot/python-telegram-bot)

* logging to console or file, with logs rotating by TimedRotatingFileHandler

### Configs:

Bot's Settings are in the file **my_private_bot/config.py:**

* put **your TOKEN_BOT** (you should get a one from @BotFather) 
* put **YOUR_TELEGRAM_CHAT_ID** - id of your Telegram chat/channel where you want the bot will redirect received messages
  
You can get YOUR_TELEGRAM_CHAT_ID in some different ways, for example:

* add the bot to your chat, send any message in the chat and then call a request in the browser: **https://api.telegram.org/bot<YOUR_TOKEN_BOT>/getUpdates**
  (the bot should be at the stopped state and webhooks disabled)
    
* adding to your chat/channel some 3rd party bot (@getidsbot, @RawDataBot, etc. ),
  send any message to the chat and the bot will provide you message data.
  
Then look up for: 
```  
chat":{"id":-1234567890 - this is your chat ID
```
