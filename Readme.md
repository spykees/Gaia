# Gaia Bot

Gaia Bot is a Discord bot built using the `nextcord` library. It responds to messages and commands in a Discord server. This is a simple project for now !

## Features

- Responds to messages starting with "Hello" or "hello" with a greeting.
- Implements a simple anti-spam mechanism to prevent repeated triggering within a short period.
- Responds to the `!ping` command with "Pong".
- List cogs with `!listmods` command
- Reload specified cog with `!reload`cogname

## Requirements

- Python 3.10+
- `nextcord` library
- `python-dotenv` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/Gaia.git
    cd Gaia
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Rename the .env.exemple to .env  in the root directory of the project and change all the id or token needed

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. The bot will connect to your Discord server and respond to messages and commands as described in the features section.

## Code Overview

The main functionality of the bot is implemented in main.py. Here is a brief overview of the key parts:

- **Bot Initialization**: The bot is initialized with specific intents and a command prefix.
- **Event Handlers**: The bot has event handlers for on_ready and on_message events.
- **Commands**: 
    - The bot has a ping command that responds with "Pong".
    - The bot has a listmods command to list all modules loaded.
    - The bot has a reload command to reload a specific modules.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.