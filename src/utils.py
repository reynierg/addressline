"""Provides functionality for decorate a method to logs its execution, for
extract the different parts of an address from an address line and for
initialize the arguments parser being used.

This file can be imported as a module and contains the following functions:

    * log - decorates the specified function, to log data about its execution
    * build_address_dict - returns a dict with the specified street name and
    house number
    * extract_address_parts - extract the street name and house number from a
    address line
    * init_argparse - initialize an ArgParser with the allowed arguments, and
    description message
"""

import argparse
import functools
import logging
import re
import typing

from src import constants


def log(func):
    """Used for decorate a function to log when it's called.

    Parameters
    ----------
    func : typing.Callable
        function to logs data related to his invocation

    Returns
    -------
    typing.Callable
        function that logs the called function's details and execute it
    """

    function_name = func.__name__
    args_names = func.__code__.co_varnames[:func.__code__.co_argcount]

    @functools.wraps(func)
    def wrapper(*args):
        args_metadata = ", ".join("%s=%r" % item for item
                                  in zip(args_names, args[:len(args_names)]))
        logging.debug("%s(%s)", function_name, args_metadata)
        return func(*args)

    return wrapper


@log
def build_address_dict(street_name: str, house_number: str) \
        -> typing.Dict[str, str]:
    """Builds a dict with the street name and house number

    Parameters
    ----------
    street_name : str
        Street name
    house_number: str
        House number

    Returns
    -------
    typing.Dict[str, str]
        a dict with the following structure:
        {
            "street": "Street name",
            "housenumber": "House number"
        }
    """

    return {
        "street": street_name,
        "housenumber": house_number
    }


@log
def extract_address_parts(address_line: str) -> typing.Dict[str, str]:
    """Extracts the street name and house number from a string line

    Parameters
    ----------
    address_line : str
        Contains a street name and number

    Returns
    -------
    typing.Dict[str, str]
        a dict with the following structure:
        {
            "street": "Street name",
            "housenumber": "House number"
        }
    """

    match = \
        re.match(constants.REGEX_1, address_line) or \
        re.match(constants.REGEX_2, address_line) or \
        re.match(constants.REGEX_3, address_line)

    if match:
        logging.info("A regular expression matched the specified address line")
        return build_address_dict(match.group(constants.STREET_GROUP_NAME),
                                  match.group(constants.NUMBER_GROUP_NAME))

    logging.info("None of the 3 regular expressions matched the address line")
    return build_address_dict("UNKNOWN", "UNKNOWN")


def init_argparse() -> argparse.ArgumentParser:
    """Initialize an arguments parser, to parse the command line's arguments

    Returns
    -------
    argparse.ArgumentParser
        arguments parser to be used to process command line arguments
    """

    parser = argparse.ArgumentParser(
        description='Receive a street line as input and extracts the street '
                    'name and the house number',
        epilog=constants.HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='be verbose')

    parser.add_argument('address_line',
                        metavar='address_line',
                        type=str,
                        help='the address line to extract the street name and '
                             'house number from')

    return parser
