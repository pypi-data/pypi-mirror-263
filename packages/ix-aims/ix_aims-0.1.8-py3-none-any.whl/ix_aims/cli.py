import typer
from typing_extensions import Annotated

from ix_aims.lib import auto_ix


@typer.run
def main(
        work_order: Annotated[
            str,
            typer.Argument(help="The work order number in format ##_####_##")
        ]):
    """For ACO WORK_ORDER, setup iX Capture with the correct configuration and
    calibration parameters."""
    auto_ix(work_order)


if __name__ == '__main__':
    main()
