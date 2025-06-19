import configparser
import os
import re
import json
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from nltk.tokenize import word_tokenize
import nltk
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Download NLTK data
try:
    nltk.download('punkt', quiet=True)
except Exception as e:
    logger.error(f"Failed to download NLTK data: {e}")
    exit(1)

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
phone = config['Telegram']['phone']

# Initialize Telegram client
client = TelegramClient('session_name', int(api_id), api_hash)

def preprocess_amharic(text):
    """Preprocess Amharic text: remove special characters, tokenize, and normalize."""
    if not text:
        return []
    # Remove emojis and special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Normalize: remove empty tokens and strip whitespace
    tokens = [token.strip() for token in tokens if token.strip()]
    return tokens

async def scrape_channel(channel_username, limit=100):
    """Scrape messages from a Telegram channel and preprocess text."""
    try:
        await client.start(phone)
        channel = await client.get_entity(channel_username)
        messages = []

        logger.info(f"Scraping channel: {channel_username}")
        async for message in client.iter_messages(channel, limit=limit):
            if not message.text and not message.media:
                continue  # Skip empty messages

            # Extract message data
            msg_data = {
                'message_id': message.id,
                'timestamp': str(message.date),
                'sender': str(message.sender_id) if message.sender_id else 'unknown',
                'text': message.text or '',
                'tokens': preprocess_amharic(message.text),
                'views': message.views or 0,
                'image_path': None
            }

            # Save images if present
            if message.media and hasattr(message.media, 'photo'):
                image_dir = 'images'
                os.makedirs(image_dir, exist_ok=True)
                image_path = os.path.join(image_dir, f"{channel_username}_{message.id}.jpg")
                await message.download_media(file=image_path)
                msg_data['image_path'] = image_path
                logger.info(f"Saved image: {image_path}")

            messages.append(msg_data)

        # Save messages to JSON
        output_file = f"data/{channel_username}_messages.json"
        os.makedirs('data', exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved {len(messages)} messages to {output_file}")

        return messages

    except Exception as e:
        logger.error(f"Error scraping {channel_username}: {e}")
        return []

async def main():
    """Main function to scrape multiple channels."""
    # List of Telegram channels to scrape
    channels = [
        '@Shageronlinestore',
        '@ZemenExpress',
        '@nevacomputer',
        '@meneshayeofficial',
        '@ethio_brand_collection',
        '@Leyueqa',
        '@sinayelj',
        '@Shewabrand',
        '@helloomarketethiopia',
        '@modernshoppingcenter',
        '@qnashcom',
        '@Fashiontera',
        '@kuruwear',
        '@gebeyaadama',
        '@MerttEka',
        '@forfreemarket',
        '@classybrands',
        '@marakibrand',
        '@aradabrand2',
        '@marakisat2',
        '@belaclassic',
        '@AwasMart'
    ]

    all_messages = []
    for channel in channels:
        messages = await scrape_channel(channel, limit=50)
        all_messages.extend(messages)

    # Save combined data
    with open('data/all_messages.json', 'w', encoding='utf-8') as f:
        json.dump(all_messages, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved {len(all_messages)} total messages to data/all_messages.json")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())