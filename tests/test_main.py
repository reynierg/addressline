import sys

from src import main


def test_main() -> None:
    """Verifies that the main method behave correctly whit an address line"""

    _test_main()


def test_main_verbose() -> None:
    """Verifies that the main method behave correctly whit the -v argument"""

    _test_main(True)


def _test_main(verbose: bool = False) -> None:
    """Verifies that the main method parses correctly a supplied address line

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
    results = main.main()
    # restore original sys.argv content:
    sys.argv = sys_argv
    expected_dict = {
        "street": "Lange Str.",
        "housenumber": "5"
    }
    assert results == expected_dict
