import os
from pathlib import Path

__all__ = ["VERSION"]

VERSION = "0.0.1"

if os.getenv("XDG_CACHE_HOME") is not None:
    SAVE_PATH = os.getenv("XDG_CACHE_HOME") + "/spotifytranslator"
else:
    SAVE_PATH = str(Path.home()) + "/.cache/spotifytranslator"
