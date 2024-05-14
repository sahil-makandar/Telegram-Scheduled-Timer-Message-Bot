# Telegram Scheduled Timer Message Bot

## About
This is a Telegram bot that sends messages at regular set time intervals. The bot is built using the Telegram Bot API and the Schedule library for scheduling tasks.

## Installation

1. **Clone Repository**: 
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/mahaboobsabGoa/Telegram-Scheduled-Timer-Message-Bot.git
     ```

2. **Navigate to Repository**: 
   - Change directory to the cloned repository:
     ```bash
     cd telegram-scheduled-message-bot
     ```

3. **Install Dependencies**: 
   - Install the required Python dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Telegram Bot**: 
   - Create a new bot on Telegram and obtain the bot token.
   - Replace `"<telegram-bot-token>"` in the code with your actual bot token.

## Usage

1. **Start Bot**: 
   - Run the bot script to start sending messages at regular intervals:
     ```bash
     python bot.py
     ```

2. **Customize Time Interval**: 
   - Modify the `schedule.every(5).seconds.do(sayhi)` line in the code to set your desired time interval.
   - The example provided sends a message every 5 seconds. You can adjust this interval according to your preference.

3. **Interact with the Bot**: 
   - The bot sends messages to the specified chat ID at the set time intervals.
