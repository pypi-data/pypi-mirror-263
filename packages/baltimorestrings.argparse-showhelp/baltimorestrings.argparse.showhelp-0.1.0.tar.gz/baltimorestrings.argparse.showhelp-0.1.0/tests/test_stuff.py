from baltimorestrings.argparse_showhelp import ArgumentParserDisplayHelpOnError, argparse_quick_build
from unittest.mock import MagicMock, patch
from pathlib import Path
import json
import pytest


def load_results(path: Path) -> str:
    if not (path.exists() and path.is_file()):
        raise FileNotFoundError(f"unable to get {path}")
    with open(str(path)) as file:
        json_raw = file.read()
        try:
            return json.loads(json_raw)["output"]
        except (ValueError, json.JSONDecodeError) as e:
            raise ValueError(f"Unable to process data in {path}, {repr(e)}, {e}")



def test_parser(test_folder):
    """
    Just a simple integration test.

    Tests:
    - that argparse is raising the error for missing an arg
    - that our class is calling the help display
    - that the formatter isn't removing newlines (https://docs.python.org/3/library/argparse.html#argparse.RawDescriptionHelpFormatter)
    """
    parser: ArgumentParserDisplayHelpOnError = ArgumentParserDisplayHelpOnError("testthing")
    parser.add_argument("string", help="With RawTextFormatter\n,\nthese\nnewlines won't be deleted.")
    parser._print_message = MagicMock(autospec=ArgumentParserDisplayHelpOnError._print_message)
    with pytest.raises(SystemExit):
        parser.parse_args([])

    output_from_argparse = parser._print_message.call_args_list[0][0][0]

    assert parser._print_message.called == True
    assert output_from_argparse == load_results(test_folder / "expected_output.json")

def test_quick_build():
    with pytest.raises(NotImplementedError):
        argparse_quick_build()
