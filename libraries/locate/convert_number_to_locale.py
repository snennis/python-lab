"""This Function converts a given number (int OR float) into the
   correct format of the current locale of the user"""

# library imports
import locale

def convert_number_to_locale(number: int | float) -> int | float:
    # set locale to user locale
    locale.setlocale(locale.LC_ALL, '')

    # check if number is type int OR float and return the correct formatted value
    match number:
        case int():
            return int(locale.atoi(str(number)))

        case float():
            return float(locale.atof(str(number)))

        case _:
            raise locale.Error('No Number was given.')