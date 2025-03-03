import logging

# Configure the logger
logging.basicConfig(
    filename='command_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_command(command_name, user):
    logging.info(f"Command: {command_name} executed by {user}")
