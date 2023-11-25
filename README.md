# Discord Self-Bot

## Introduction

This is a simple self-bot script written in Python using the Discord.py-self dev environment library. The self-bot monitors messages in a specified server and channel and reacts to messages that contain a specific keyword.

## Features

- Listens to messages in a Discord server and channel.
- Reacts to messages containing a specified keyword with a custom emoji.

## Prerequisites

- Python 3.x installed on your machine.
- Discord.py-self library installed use

# install 

$ git clone https://github.com/dolfies/discord.py-self
$ cd discord.py-self
$ python3 -m pip install -U .[voice]

- Your discord account token

## Setup

1. Clone or download the script to your local machine.

2. Create a `.env` file in the same directory as the script with the following content:

    ```
    TOKEN= your_discord_token
    SERVER= your_server_id
    CHANNEL= your_channel_id
    TARGET= 'your_target_keyword'
    EMOJI= 'your_reaction_emoji'
    ```

    Replace `your_discord_token`, `your_server_id`, `your_channel_id`, `your_target_keyword`, and `your_reaction_emoji` with your actual Discord account token, server ID, channel ID, target keyword, and reaction emoji, respectively.

3. Install the required Python libraries:

    ```bash
    pip install python-dotenv
    ```

4. Run the script:

    ```bash
    python3 react.py
    ```

## Bot Behavior

- The self-bot will print a message to the console when it successfully logs in.
- It will listen to messages in the specified server and channel.
- When a message contains the specified keyword, the self-bot will print a message to the console and react to the message with the specified emoji.

## Important Note

- Ensure that your self-bot has the necessary permissions in the server and channel where it operates.
- Be cautious when sharing your Discord account token and other sensitive information.

## Troubleshooting

- If the self-bot is not reacting as expected, check the console for any error messages.
- Verify that the self-bot has the required permissions and is added to the correct server and channel.

