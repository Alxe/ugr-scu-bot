from ugr_scu_bot.bot import Bot

import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

Bot(token=os.environ['BotToken']).run()