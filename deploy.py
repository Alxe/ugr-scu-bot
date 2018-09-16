"""Deployment file"""

import os
import logging

import ugr_scu_bot.bot as scu_bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

scu_bot.TelegramBot(token=os.environ['TelegramBotToken']).run()
