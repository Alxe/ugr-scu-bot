"""
Bot
"""
from datetime import datetime as dt

from telegram.ext import Updater, Dispatcher, Job, JobQueue

from ugr_scu_bot.scraper import Scraper
from ugr_scu_bot.formatter import Formatter
from ugr_scu_bot.constants import CHANNEL_ID, DAILY_NOTIFICATION_TIME

class Bot(object):
    """
    Bot class
    """
    def __init__(self, token=None, channel_id=CHANNEL_ID):
        self._updater = Updater(token=token)
        self._dispatcher = self._updater.dispatcher
        self._jobqueue = self._updater.job_queue

        self._scraper = Scraper()
        self._formatter = Formatter()

        self._channel_id = channel_id

    def _daily_report(self, bot, job):
        weekday = dt.today().weekday()

        daily_scrap = self._scraper.scrape_weekday(weekday)

        day_message = self._formatter.format_day(weekday)

        for (name, items) in daily_scrap.items():
            menu_message = self._formatter.format_menu(name, items)
            bot.send_message(chat_id=self._channel_id,
                             text="\n".join([day_message, menu_message]),
                             parse_mode="Markdown")

    def run(self):
        """
        Start the bot
        """
        self._jobqueue.run_daily(self._daily_report,
                                 time=DAILY_NOTIFICATION_TIME,
                                 days=(0, 1, 2, 3, 4, 5))

        self._updater.start_polling()
        self._updater.idle()
        