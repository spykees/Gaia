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

4. Rename the .env.exemple in [.env](http://_vscodecontentref_/1)  in the root directory of the project and change all the id or token needed

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. The bot will connect to your Discord server and respond to messages and commands as described in the features section.

## Code Overview

The main functionality of the bot is implemented in [main.py](http://_vscodecontentref_/2). Here is a brief overview of the key parts:

- **Bot Initialization**: The bot is initialized with specific intents and a command prefix.
- **Event Handlers**: The bot has event handlers for [on_ready](http://_vscodecontentref_/3) and [on_message](http://_vscodecontentref_/4) events.
- **Commands**: The bot has a [ping](http://_vscodecontentref_/5) command that responds with "Pong".

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.