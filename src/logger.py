import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a logs directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Create the full path for the log file inside the logs directory
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example of logging an info message
logging.info("Logging setup complete.")
