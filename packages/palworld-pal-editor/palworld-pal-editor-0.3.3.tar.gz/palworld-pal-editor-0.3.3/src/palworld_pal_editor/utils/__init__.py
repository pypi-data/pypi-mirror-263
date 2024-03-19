from palworld_pal_editor.config import PROGRAM_PATH
from palworld_pal_editor.utils.logger import PalEditorLogger

LOGGER = PalEditorLogger.LOGGER
# LOGGER = Logger(log_directory=PROGRAM_PATH / "logs")
# LOGGER().info(f"Logs written to {PROGRAM_PATH / 'logs'}")

from palworld_pal_editor.utils.util import alphanumeric_key, clamp
from palworld_pal_editor.utils.data_provider import DataProvider