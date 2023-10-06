# Logging used for complete understanding of workflow configurations of our application over time.

# There are 5 basic levels of logging:
# DEBUG(provides detailed information),
# INFO(confirmation that everything's good as expected),
# WARNING(something unexpected happen yet software still works),
# ERROR(software stopped working),
# CRITICAL(serious error)
# HERE ANYTHING BELOW THE STATED LEVEL WILL BE LOGGED INCLUDING THE CURRENT LOG LEVEL.

import os
import logging
import sys

logging_str = (
    "[%(asctime)s: %(name)s: %(levelname)s: %(module)s: %(message)s: %(lineno)d]"
)
log_dir = "logs"

os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir, "running_logs.log")


# logging.FileHandler(log_filepath).setLevel(logging.DEBUG) -> .setLevel only log those statements to the log file with .DEBUG level


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    # filename='logs/running_logs.log'
    handlers=[
        logging.FileHandler(log_filepath),  # Display the format in the log file
        logging.StreamHandler(sys.stdout),  # Display the format on the terminal
    ],
)

logger = logging.getLogger(__name__)

