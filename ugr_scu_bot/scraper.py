# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

from .constants import WEEKDAYS, WEEKDAY_DAYOFWEEK

class Scraper:
    def __init__(self):
        pass
        
    def _retrieve_scrap(self, url='http://scu.ugr.es/') -> BeautifulSoup:
        with urlopen(url) as scrap:
            return BeautifulSoup(scrap, 'html.parser')

    def scrape_weekday(self, weekday):
        scrap = self.scrape()

        return scrap[WEEKDAY_DAYOFWEEK[weekday]]

    def scrape(self):
        scrap = self._retrieve_scrap()

        # Expected data value follows the format:
        # { day : { menu : [(type, name, allergens)] } }
        data = {}

        # Status tracking
        current_day  = None
        current_menu = None

        # For each 'tr' tag in the table
        for row in scrap.table.find_all('tr'):
            is_day_row   = False
            is_menu_row  = False

            # Workaround against non-valid rows
            if row is None or row.td is None:
                continue

            first_col = row.td
            first_col_text = first_col.get_text().strip().capitalize()

            # Check if current row is a 'day' row
            for day in WEEKDAYS:
                # If the day is contained in the text, we are in a day row
                if day in first_col_text:
                    current_day  = day
                    current_menu = None
                    is_day_row   = True
                    is_menu_row  = False

                    # As we've found a valid day, we exit the day-loop
                    break

            # If row is a 'day' row, add to the data, else, continue processing
            if is_day_row:
                data[current_day] = {}

            else:
                # Check if current row is a 'menu' row
                is_menu_row = ('Menú' in first_col_text)

                if is_menu_row:
                    # 'row' is expected to have one col, the name of the menu 
                    current_menu = first_col_text.capitalize()
                elif current_menu is None:
                    current_menu = 'Menú'            
                
                if not is_menu_row:
                    if current_menu not in data[current_day]:
                        data[current_day][current_menu] = []

                    cols = row.find_all('td')

                    item_tuple = ((
                        cols[0].get_text().strip(), # type
                        cols[1].get_text().strip(), # name
                        cols[2].get_text().strip(), # allergens
                            ))
            
                    data[current_day][current_menu].append(item_tuple)

            
        return data