import logging
import time
import signal
import sys
import random

# Configure logging
logging.basicConfig(filename='log_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the function to handle signal interruption (Ctrl+C)
def signal_handler(sig, frame):
    logging.info("Logging interrupted. Exiting.")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Main loop to log messages
while True:
    try:
        # Randomly select a log level
        log_level = random.choice(log_levels)
        # Get the log message format for the selected log level
        log_message = formats[log_level]
        # Log the message
        logging.log(log_level, log_message)
        # Sleep for a short interval
        time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        signal_handler(signal.SIGINT, None)










