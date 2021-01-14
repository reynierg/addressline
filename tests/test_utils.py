import sys

import pytest

from src import utils

tests_data = [
    ("Winterallee 3",              ("Winterallee",          "3")),
    ("Musterstrasse 45",           ("Musterstrasse",        "45")),
    ("Am Bächle 23",               ("Am Bächle",            "23")),
    ("Karl-Weysser-Str. 9",        ("Karl-Weysser-Str.",    "9")),
    ("Blaufeldweg 123B",           ("Blaufeldweg",          "123B")),
    ("Auf der Vogelwiese 23 b",    ("Auf der Vogelwiese",   "23 b")),
    ("Königsbrücker Str. 21 - 29", ("Königsbrücker Str.",   "21 - 29")),
    ("Calle Aduana, 29",           ("Calle Aduana",         "29")),
    ("Calle 39 No 1540",           ("Calle 39",             "No 1540")),
    ("4, rue de la revolution",    ("rue de la revolution", "4")),
    ("200 Broadway Av",            ("Broadway Av",          "200")),
    ("Invalid",                    ("UNKNOWN",              "UNKNOWN")),
]

tests_ids = [
    "test_german_address_one_word_one_digit",
    "test_german_address_one_word_two_digits",
    "test_german_address_two_words_and_umlaut",
    "test_german_address_two_words_separated_by_dash",
    "test_german_address_one_word_digits_with_letter",
    "test_german_address_three_word_digits_letter",
    "test_german_address_with_numbers_range",
    "test_spanish_address_with_comma",
    "test_spanish_address_with_number_in_the_street_name",
    "test_french_address",
    "test_american_address",
    "test_not_recognized_address"
]


@pytest.mark.parametrize("address_line,expected_address_parts",
                         tests_data,
                         ids=tests_ids)
def test_extract_address_parts(address_line, expected_address_parts) -> None:
    """Verifies that address line is correctly parsed

    Parameters
    ----------
    address_line : str
        Address line that contains the street name and house number
    expected_address_parts: tuple
        Contains the street name and the street number that are expected to
        be extracted.
    """

    assert utils.extract_address_parts(address_line) == \
           utils.build_address_dict(*expected_address_parts)


def test_build_address_dict() -> None:
    """Verifies that an address dict is build correctly"""

    dummy_street_name = "MyStreet"
    dummy_house_number = "9"
    expected_dict = {
        "street": dummy_street_name,
        "housenumber": dummy_house_number
    }
    assert utils.build_address_dict(dummy_street_name, dummy_house_number) == \
           expected_dict


def test_init_argparse_supplying_address() -> None:
    """Verifies that the ArgParser parses correctly a supplied address line"""

    _test_init_argparse_supplying_address()


def test_init_argparse_with_verbose_activated() -> None:
    """Verifies that the ArgParser parses correctly the -v argument"""

    _test_init_argparse_supplying_address(True)


def _test_init_argparse_supplying_address(verbose: bool = False) -> None:
    """Verifies that the ArgParser parses correctly a supplied address line

    Parameters
    ----------
    verbose : bool, optional
        Specifies if the -v argument must be used (default is False)
    """

    # save the original sys.argv content, before customize it with
    # arguments being passed to the ArgsParser:
    sys_argv = sys.argv[::]
    sys.argv = [sys_argv[0]]
    if verbose:
        sys.argv.append("-v")

    test_address = "Lange Str. 5"
    sys.argv.append(test_address)
    args = utils.init_argparse().parse_args()
    # restore original sys.argv content:
    sys.argv = sys_argv

    address_line = getattr(args, "address_line")
    assert test_address == address_line
