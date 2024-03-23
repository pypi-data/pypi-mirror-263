import ast
from typing import Generator, List, Tuple

MSG = "MXL001 File has too many lines ({actual}). Maximum allowed is {max}."
DEFAULT_MAX_LINES = 300


class MaxLinesPlugin:
    name = "flake8_max_lines"
    version = "0.0.2"

    max_lines = DEFAULT_MAX_LINES

    @classmethod
    def add_options(cls, option_manager):
        option_manager.add_option(
            "--max-lines",
            type=int,
            metavar="n",
            default=DEFAULT_MAX_LINES,
            parse_from_config=True,
            help="enforces a maximum number of lines in a file"
            "For example, ``--max-lines=500``. (Default: %(DEFAULT_MAX_LINES))"
        )

    @classmethod
    def parse_options(cls, options):
        cls.max_lines = options.max_lines

    def __init__(self, lines: List[str], total_lines: int, tree: ast.AST):
        self.lines = lines
        self.total_lines = total_lines

    def get_file_length(self) -> int:
        # [this logic to check newline at end of file](./test_plugin.py#L27)

        physical_line = self.lines[-1]
        stripped_last_line = physical_line.rstrip("\r\n")
        return (
            self.total_lines
            if stripped_last_line == physical_line
            else self.total_lines + 1
        )

    def run(self) -> Generator[Tuple[int, int, str, None], None, None]:
        actual_lines = self.get_file_length()
        max_lines = self.max_lines
        if actual_lines > max_lines:
            message = MSG.format(actual=actual_lines, max=max_lines)
            yield actual_lines, 0, message, None
