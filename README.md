## Overview
This Python script generates random log messages at different logging levels (INFO, DEBUG, ERROR) and logs them to a file. It also handles interruptions (Ctrl+C) gracefully.

## Prerequisites
- Python 3.x installed on your system
- Standard Python libraries (logging, time, signal, sys, random)

## Usage
1. Clone or download the repository containing the script.
2. Ensure that Python 3.x is installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the following command:
6. The script will start generating random log messages and logging them to a file named `log_monitor.log` in the same directory.

## Testing
To test the script, you can perform the following steps:
1. Run the script as mentioned in the "Usage" section.
2. Open the `log_monitor.log` file using a text editor or viewer.
3. Observe the log messages being generated and logged at different logging levels (INFO, DEBUG, ERROR).
4. Press Ctrl+C to interrupt the script execution.
5. Check the log file for a message indicating that logging was interrupted.
6. Verify that the script exits cleanly without any errors.

## Additional Notes
- You can customize the logging behavior by modifying the script, such as changing the log message formats or adjusting the logging levels.
- Ensure that the script has write permissions to create and write to the log file in the current directory.