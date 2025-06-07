import os
import pandas as pd
from googleapiclient.discovery import build

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"  # Your API key
API_VERSION = 'v3'

# Initialize the YouTube API client
youtube = build('youtube', API_VERSION, developerKey=API_KEY)

def get_channel_stats(youtube, channel_id):
    """
    Fetches channel statistics (name, subscribers, views, videos) for a given channel ID.
    """
    try:
        request = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        )
        response = request.execute()

        if response['items']:
            data = {
                'channel_name': response['items'][0]['snippet']['title'],
                'total_subscribers': response['items'][0]['statistics'].get('subscriberCount', 'N/A'),
                'total_views': response['items'][0]['statistics'].get('viewCount', 'N/A'),
                'total_videos': response['items'][0]['statistics'].get('videoCount', 'N/A'),
            }
            return data
        else:
            print(f"No data found for channel ID: {channel_id}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching data for channel ID {channel_id}: {e}")
        return None

# Read CSV into dataframe
df = pd.read_csv("C:/Users/DEKATECH/Steph_pro/youtube_data_united-kingdom.csv")

# Extract channel IDs and remove potential duplicates
channel_ids = df['NOMBRE'].str.split('@').str[-1].unique()

# Initialize a list to keep track of channel stats
channel_stats = []

# Loop over the channel IDs and get stats for each
for channel_id in channel_ids:
    stats = get_channel_stats(youtube, channel_id)
    if stats is not None:
        channel_stats.append(stats)

# Convert the list of stats to a dataframe
stats_df = pd.DataFrame(channel_stats)

# Reset indices for both dataframes
df.reset_index(drop=True, inplace=True)
stats_df.reset_index(drop=True, inplace=True)

# Concatenate the dataframes horizontally
combined_df = pd.concat([df, stats_df], axis=1)

# Drop the 'channel_name' column from stats_df (since 'NOMBRE' already exists)
# combined_df.drop('channel_name', axis=1, inplace=True)

# Save the merged dataframe back into a CSV file
combined_df.to_csv('C:/Users/DEKATECH/Steph_pro/updated_youtube_data_uk.csv', index=False)

# Display the first 10 rows of the combined dataframe
print(combined_df.head(10))