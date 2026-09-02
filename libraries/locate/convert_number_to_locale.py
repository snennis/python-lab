"""This Function converts a given number (int OR float) into the
   correct format of the current locale of the user."""

# library imports
import locale

def convert_number_to_locale(number: int or float):

    locale.setlocale(locale.LC_ALL, '')