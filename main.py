import asyncio
from data_feeds import DexScreenerAPI, CoinGeckoAPI
from mev_protector import MEVExecutor
from telegram_bot import TradingAlerts
from web_dash import app

class AlphaWolfBot:
    def __init__(self):
        self.config = self.load_config()
        self.data = DexScreenerAPI() if self.config['apis']['dexscreener'] else CoinGeckoAPI()
        self.mev = MEVExecutor(self.config)
        self.telegram = TradingAlerts(self.config)
        self.running = True
        
    async def run(self):
        """Main trading loop"""
        await self.telegram.send("🤖 Bot Started")
        while self.running:
            try:
                coins = await self.data.get_trending()
                for coin in self.filter_coins(coins):
                    await self.process_coin(coin)
                await asyncio.sleep(60)
            except Exception as e:
                await self.handle_error(e)
    
    def filter_coins(self, coins):
        """Apply safety filters"""
        return [c for c in coins 
                if c['liquidity'] > 1000
                and c['age_hours'] > 2
                and not self.is_blacklisted(c)]

if __name__ == "__main__":
    bot = AlphaWolfBot()
    
    # Start web UI
    import threading
    threading.Thread(target=app.run, kwargs={'port': 5000}).start()
    
    # Start main bot
    asyncio.run(bot.run())
