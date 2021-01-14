"""Addressline

This script allows the user to print to the console the parts of an address
extracted from an address line provided

This file can also be imported as a module and contains the following
functions:

    * main - the main function of the script
"""

import logging
import typing

from src import constants
from src import utils


def main() -> typing.Dict[str, str]:
    """Program entrypoint

    Returns
    -------
    typing.Dict[str, str]
        contains the street name and house number
    """

    parser = utils.init_argparse()
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(format=constants.DEBUG_MESSAGE_FORMAT,
                            level=logging.DEBUG,
                            datefmt=constants.DATE_FORMAT)
    else:
        logging.basicConfig(format=constants.INFO_MESSAGE_FORMAT,
                            level=logging.INFO)

    address_parts = utils.extract_address_parts(args.address_line)
    logging.info("Output: %s", address_parts)
    return address_parts


if __name__ == "__main__":
    main()  # pragma: no cover
