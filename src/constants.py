"""Defines different constants being used in the project
"""

import sys

INFO_MESSAGE_FORMAT = "%(message)s"
DEBUG_MESSAGE_FORMAT = \
    "%(levelname)s|%(filename)s:%(lineno)s|%(asctime)s|%(message)s"

DATE_FORMAT = "%H:%M:%S"

HELP_EPILOG = f"""
Examples:
{sys.argv[0]} 'Winterallee 3'
Output: {{'street': 'Winterallee', 'housenumber': '3'}}

{sys.argv[0]} 'Musterstrasse 45'
Output: {{'street': 'Musterstrasse', 'housenumber': '45'}}

{sys.argv[0]} 'Auf der Vogelwiese 23 b'
Output: {{'street': 'Auf der Vogelwiese', 'housenumber': '23 b'}}

{sys.argv[0]} 'Königsbrücker Str. 21 - 29'
Output: {{'street': 'Königsbrücker Str.', 'housenumber': '21 - 29'}}

{sys.argv[0]} 'Karl-Weysser-Str. 9'
Output: {{'street': 'Karl-Weysser-Str.', 'housenumber': '9'}}

{sys.argv[0]} '4, rue de la revolution'
Output: {{'street': 'rue de la revolution', 'housenumber': '4'}}

{sys.argv[0]} 'Calle 39 No 1540'
Output: {{'street': 'Calle 39', 'housenumber': 'No 1540'}}
"""

STREET_GROUP_NAME = "street"
NUMBER_GROUP_NAME = "number"
REGEX_1 = \
    r'^(?P<street>[a-zA-ZäöüÄÖÜẞß]+(?:(?:\s|-)[a-zA-ZäöüÄÖÜẞß]+)*\.?)\,?\s' \
    r'(?P<number>(?:(?:\d)+\s?[a-zA-Z]{0,1})|(?:\d+\s?-\s?\d+))$'
"""The previous regex is expected to match addresses with the following format:
Winterallee 3
Musterstrasse 45
Blaufeldweg 123B
Am Bächle 23
Auf der Vogelwiese 23 b
Lange Str. 8
Königsbrücker Str. 21 - 29
Karl-Weysser-Str. 9
Calle Aduana, 29
"""

REGEX_2 = r'^(?P<number>[\d]+),?\s(?P<street>[a-zA-Z]+(?:\s[a-zA-Z]+)*)$'
"""The previous regex is expected to math addresses with the following format:
4, rue de la revolution
200 Broadway Av
"""

REGEX_3 = \
    r'^(?P<street>.+\d+)\s(?P<number>(?:No|no|nr|Nr)\.?\s\d+\s?[a-zA-Z]?)$'
"""The previous regex is expected to math addresses with the following format
between others:
Calle 39 No 1540
Calle 39 Nr. 1540
"""
