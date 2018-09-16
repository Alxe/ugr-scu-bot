
from datetime import datetime as dt

from telegram.ext import Updater, Dispatcher, Job, JobQueue

from ugr_scu_bot.scraper import Scraper
from ugr_scu_bot.formatter import Formatter
from ugr_scu_bot.const import TEST_CHANNEL_ID, DAILY_NOTIFICATION_TIME

from abc import ABC, abstractmethod

class BaseBot(ABC):

  def __init__(self, *args, **kwargs):
    self._scraper = Scraper()
    self._formatter = Formatter()

  @abstractmethod
  def run(self, *args, **kwargs):
    pass

class TestBot(BaseBot):
  pass

class TelegramBot(BaseBot):

  def __init__(self, token, channel_id=TEST_CHANNEL_ID):

    super().__init__()

    self._updater = Updater(token=token)
    self._dispatcher = self._updater.dispatcher
    self._jobqueue = self._updater.job_queue

    self._channel_id = channel_id

  def _daily_report(self, bot, job):
    weekday = dt.today().weekday()

    daily_menu = self._scraper.weekday(weekday)

    day_message = self._formatter.format_day(weekday)

    for (name, items) in daily_menu.items():
      menu_message = self._formatter.format_menu(name, items)
      bot.send_message(chat_id=self._channel_id,
                        text="\n".join([day_message, menu_message]),
                        parse_mode="Markdown")

  def _weekly_report(self, bot, job):
    for weekday in {0, 1, 2, 3, 4, 5}:
      daily_menu = self._scraper.weekday(weekday)

      day_message = self._formatter.format_day(weekday)

      for (name, items) in daily_menu.items():
        menu_message = self._formatter.format_menu(name, items)
        bot.send_message(chat_id=self._channel_id,
                          text="\n".join([day_message, menu_message]),
                          parse_mode="Markdown")

  def run(self, **kwargs):
    """
    Start the bot
    """
    self._jobqueue.run_daily(self._daily_report,
                              time=DAILY_NOTIFICATION_TIME,
                              days={0, 1, 2, 3, 4, 5})

    self._updater.start_polling()
    self._updater.idle()