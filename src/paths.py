from pathlib import Path
from typing import Final

DIR_PJ: Final = Path(__file__).resolve().parent.parent
DIR_OUT: Final = DIR_PJ / "out"


if not DIR_PJ.exists():
    DIR_PJ.mkdir(parents=True)
