#Hii!! RB 
# RB aka RouteRover Bot

#1 import
from typing import Final
from telegram import Update
import googlemaps
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#2 constant
TOKEN: Final='token_key'
BOT_USERNAME: Final='@RouteRover_Bot'
GOOGLE_MAPS_API_KEY = 'api_key'
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)


#3 Bot commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm RB! Your ticket to a smooth journey, navigating paths!.")

async def shortest_path_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please send your current location.")
    context.user_data['current_location'] = True

#4 Location Handling
async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location
    chat_id = update.message.chat_id


    if 'current_location' in context.user_data:
        context.user_data['current_location'] = False
        context.user_data['start_location'] = (location.latitude, location.longitude)
        await update.message.reply_text("Current location set. Now, please send your destination location.")
    else:
        context.user_data['end_location'] = (location.latitude, location.longitude)
        await update.message.reply_text("Destination location set. Calculating the shortest path...")

        # Get directions from current location to destination
        directions = gmaps.directions(
            origin=context.user_data['start_location'],
            destination=context.user_data['end_location'],
            mode="driving",  # You can change the travel mode if needed
        )

        if directions:
            # Extract and format information about the shortest path
            distance = directions[0]['legs'][0]['distance']['text']
            duration = directions[0]['legs'][0]['duration']['text']
            steps = "\n".join(step['html_instructions'] for step in directions[0]['legs'][0]['steps'])
            reply_text = f"Shortest Path:\nDistance: {distance}\nDuration: {duration}\nSteps:\n{steps}"
        else:
            reply_text = "Unable to calculate the shortest path."

        await update.message.reply_text(reply_text)
        
        
#5  Error Handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


#6 Main Execution
if __name__ == '__main__':
    print('Bot is starting')
    app = Application.builder().token('token_key').build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('shortestpath', shortest_path_command))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))
    app.add_handler(MessageHandler(filters.ERROR, error))

    app.run_polling(poll_interval=3)
