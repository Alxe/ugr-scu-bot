"""
Formatter
"""

from ugr_scu_bot.constants import WEEKDAY_MAP

class Formatter(object):
    """
    Formatter class
    """

    def format_day(self, weekday):
        """
        Format day given a weekday integer
        """

        return '*{}*'.format(WEEKDAY_MAP[weekday].upper())

    def format_menu(self, name, items):
        """
        Format {menu : [item]}
        """

        menu_list = []
        menu_list.append("_>> {}_".format(name))

        for i in items:
            i_type, i_name, i_allergens = i

            menu_format = "- {type}: {name}"
            if not i_allergens: # Allergens is not empty
                menu_format += "\n(Alérgenos: {allergens})"

            menu_string = menu_format.format(type=i_type, name=i_name, allergens=i_allergens)
            menu_list.append(menu_string)

        return "\n".join(menu_list)

    def format_extra(self, extra):
        """
        Format extra info
        """

        pass
