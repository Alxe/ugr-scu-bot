"""
Deployment file
"""

import os
import logging

from ugr_scu_bot.bot import Bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

Bot(token=os.environ['BotToken']).run()
