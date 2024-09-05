import os
import schedule
import time
import markovify
import webserver
from threading import Thread
from dotenv import load_dotenv
from src.utils.exemples import exemples
from src.builder import Builder
from src.social import Social
from src.post import Post

# Intilializing the builder
builder = Builder()

# ------ Services ------ #

# social
load_dotenv()
SOCIAL_USERNAME = os.getenv('SOCIAL_USERNAME')
SOCIAL_PASSWORD = os.getenv('SOCIAL_PASSWORD')
social_api = Social(SOCIAL_USERNAME, SOCIAL_PASSWORD)
builder.set_social(social_api)

# post
model = markovify.Text(exemples, state_size=2)
post_generator = Post(model)
builder.set_post(post_generator)

# ------ Build ------ #
bot = builder.build()

# Function to run scheduled tasks
def run_schedule():
    schedule.every(14).minutes.do(bot.run)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Run the scheduler in a separate thread
schedule_thread = Thread(target=run_schedule)
schedule_thread.start()

# Start the Flask server
webserver.keep_alive()