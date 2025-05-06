import pandas as pd

def convert_to_numeric(value):
    if pd.isna(value):
        return None
    if 'M' in value:
        return float(value.replace('M', '')) * 1000000
    elif 'K' in value:
        return float(value.replace('K', '')) * 1000
    else:
        return float(value)

# Load the dataset
df = pd.read_csv('.../youtube_data_united-kingdom.csv')

# Split the 'NOMBRE' column into 'Channel Name' and 'Channel ID'
df[['Channel Name', 'Channel ID']] = df['NOMBRE'].str.split(' @', expand=True)

# Rename columns for clarity
df.rename(columns={'SEGUIDORES': 'Total Subscribers', 'ALCANCE POTENCIAL': 'Total Views'}, inplace=True)

# Extract the required columns
cleaned_df = df[['Channel Name', 'Total Subscribers', 'Total Views']]

# Handle missing or invalid data (if any)
cleaned_df['Total Subscribers'] = df['Total Subscribers'].apply(convert_to_numeric)
cleaned_df['Total Views'] = df['Total Views'].apply(convert_to_numeric)

# Since the dataset does not contain 'Total Videos', we will add a placeholder column
cleaned_df['Total Videos'] = None

# Save the cleaned data to a new CSV file
cleaned_df.to_csv('.../cleaned_youtube_data_united-kingdom.csv', index=False)

print("Cleaned data saved to 'cleaned_youtube_data_united-kingdom.csv'")