"""
Constants
"""

from datetime import time

CHANNEL_ID = '@ugr_scu'

WEEKDAY_MAP = {
    0 : 'Lunes',
    1 : 'Martes',
    2 : 'Miércoles',
    3 : 'Jueves',
    4 : 'Viernes',
    5 : 'Sábado',
}

DAILY_NOTIFICATION_TIME = time(hour=9, tzinfo=None)
