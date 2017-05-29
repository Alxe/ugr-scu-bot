from .constants import WEEKDAY_DAYOFWEEK

class Formatter:
    def format_day(self, weekday) -> str:
        return "*{:^-10}*".format(WEEKDAY_DAYOFWEEK[weekday].upper())
    
    def format_menu(self, name, items) -> str:
        menu_list = []
        menu_list.append("_>> {:^-10}_".format(name))

        for m in items:
            m_type, m_name, m_allergens = m

            menu_format = "{type:>4}: {name}" 
            if len(m_allergens) > 0:
                menu_format += " ({allergens})"

            menu_string = menu_format.format(type=m_type, name=m_name, allergens=m_allergens)
            
            menu_list.append(menu_string)

        return "\n".join(menu_list)

    def format_extra(self, extra):
        pass