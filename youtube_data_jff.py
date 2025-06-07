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
    
df = pd.read_csv('.../youtube_data_united-kingdom.csv')
column_translations = {
    'NOMBRE': 'Channel Name',
    'SEGUIDORES': 'Total Subscribers',
    'TP': 'Engagement Rate',
    'PAÍS': 'Country',
    'TEMA DE INFLUENCIA': 'Influence Topic',
    'ALCANCE POTENCIAL': 'Total Views',
    'GUARDAR': 'Save',
    'INVITAR A LA CAMPAÑA': 'Invite to Campaign'
}
df.rename(columns=column_translations, inplace=True)
df[['Channel Name', 'Channel ID']] = df['Channel Name'].str.split(' @', expand=True)
df['Total Subscribers'] = df['Total Subscribers'].apply(convert_to_numeric)
df['Total Views'] = df['Total Views'].apply(convert_to_numeric)
df['Country'] = "United Kingdom"
df['Invite to Campaign'] = "View Profile"
df['Engagement Rate'] = df['Engagement Rate'].str.replace('%', '')
df['Engagement Rate'] = pd.to_numeric(df['Engagement Rate'], errors='coerce')
df.drop(columns=['Influence Topic', 'Save'], inplace=True)
df.to_csv('.../cleanedjff_youtube_data_united-kingdom.csv', index=False)