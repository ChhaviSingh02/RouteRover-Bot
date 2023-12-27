# RouteRover-Bot
The RouteRover Bot is a project that leverages the Telegram messaging platform to provide users with the shortest path between two locations. Utilizing the Google Directions API, the bot interacts with users by prompting them to share their current location and destination.

# Overview
RouteRover Bot (RB) is a Telegram bot designed to provide users with a seamless experience in seeking efficient routes and navigating paths. Whether you're looking for the shortest route between locations or exploring the capabilities of a navigation bot, RouteRover is here to assist you.

# Features
Shortest Path Calculation: Utilizes the Google Maps API to calculate the shortest path between the user's provided current location and destination.
User Interaction: Accepts user input through Telegram commands and location sharing for a user-friendly experience.
Real-time Navigation: Provides real-time updates on the calculated route, including distance, duration, and step-by-step instructions.

# Getting Started
Prerequisites
Telegram Bot Token:

Obtain a Telegram Bot Token by creating a new bot on Telegram through BotFather.
Google Maps API Key:

Acquire a Google Maps API Key to enable route calculations. Follow the Google Cloud documentation for API key creation.
Installation
Clone the repository:
git clone https://github.com/your_username/RouteRover-Bot.git
Install dependencies:
pip install -r requirements.txt
Set up your configuration:

Replace 'api_key' in the code with your Google Maps API Key.
Replace 'YOUR_BOT_TOKEN' with your Telegram Bot Token.
Usage
Run the bot:

python main.py
Interact with the bot on Telegram:

Use the /start command to initiate the conversation.
Use /shortestpath to calculate the shortest path.
Share your current location and destination with the bot for navigation.

