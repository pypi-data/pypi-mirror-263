from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys


class ArgumentParserDisplayHelpOnError(ArgumentParser):
    """No-one ever remembers that --help exists. This'll force it out whenever argparse fails

    Also uses the raw text help formatter, which allows \n to be used
    """

    _line_length: int = 50
    _line_char: str = "-"

    def __init__(self, *args, **kwargs):
        self._error_line: str = self._line_length * self._line_char
        super().__init__(*args, **{"formatter_class": RawDescriptionHelpFormatter, **kwargs})

    def error(self, message: str):
        sys.stderr.write(f"{self._error_line}\nError: {message}\n{self._error_line}\n")
        self.print_help()
        sys.exit(1)
