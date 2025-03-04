# Gaia Bot

Gaia Bot is a Discord bot built using the `nextcord` library. It responds to messages and commands in a Discord server. This project includes multi-language support and various moderation commands.

## Features

- Responds to messages starting with "hello", "Hello", "coucou", "Coucou", "salut", or "Salut" with a greeting.
- Implements a simple anti-spam mechanism to prevent repeated triggering within a short period.
- Multi-language support for commands and responses.
- Moderation commands:
  - `!kick <username> <reason>`: Kicks a member from the server with an optional reason.
  - `!ban <username> <reason>`: Bans a member from the server with an optional reason.
- Admin commands:
  - `!listmods`: Lists all available cogs.
  - `!reload <cog>`: Reloads the specified cog.
  - `!setmodo <username>`: Adds a member to the moderator role.
- All Moderation commands like kick ban are log with date and time, username of the modo, name of target and reason

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

4. Rename the `.env.example` to `.env` in the root directory of the project and update the necessary IDs and tokens.

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. The bot will connect to your Discord server and respond to messages and commands as described in the features section.

## Code Overview

The main functionality of the bot is implemented in `main.py`. Here is a brief overview of the key parts:

- **Bot Initialization**: The bot is initialized with specific intents and a command prefix.
- **Event Handlers**: The bot has event handlers for `on_ready`, `on_message`, and `on_member_join` events.
- **Commands**: 
  - The bot has moderation commands (`kick`, `ban`).
  - The bot has admin commands (`listmods`, `reload`, `setmodo`).

## Multi-language Support

The bot supports multiple languages for commands and responses. The translations are stored in JSON files located in the `lng` directory. You can add or update translations by modifying these files.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Transaltion
- FR Shark
- EN Shark

## License

This project is licensed under the MIT License. See the LICENSE file for more details.