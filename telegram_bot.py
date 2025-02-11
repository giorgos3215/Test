from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

class TradingAlerts:
    def __init__(self, config):
        self.bot = Bot(token=config['telegram']['bot_token'])
        self.updater = Updater(token=config['telegram']['bot_token'])
        
        # Add commands
        self.updater.dispatcher.add_handler(
            CommandHandler('stop', self.stop_bot)
            
    async def send(self, msg):
        await self.bot.send_message(
            chat_id=self.config['telegram']['chat_id'],
            text=msg
        )
