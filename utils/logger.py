import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure the general logger
logging.basicConfig(
    filename='logs/infos.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Configure the command logger
command_logger = logging.getLogger('commands')
command_handler = logging.FileHandler('logs/commands.log')
command_handler.setLevel(logging.INFO)
command_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
command_logger.addHandler(command_handler)

def log_command(command_name, user, target=None, reason=None):
    log_message = f"Command: {command_name} executed by {user}"
    if target:
        log_message += f", Target: {target}"
    if reason:
        log_message += f", Reason: {reason}"
    command_logger.info(log_message)
