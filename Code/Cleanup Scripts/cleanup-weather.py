import pandas as pd
import gzip
import os

# Define column names based on the provided structure
COLUMN_NAMES = ['ID', 'YEAR/MONTH/DAY', 'ELEMENT', 'DATA VALUE', 'M-FLAG', 'Q-FLAG', 'S-FLAG', 'OBS-TIME']

# Function to read gzipped CSV and return a DataFrame
def read_gzipped_csv(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        df = pd.read_csv(file, header=None, names=COLUMN_NAMES)
    return df

# Function to filter DataFrame based on California station IDs
def filter_california_stations(df, california_ids):
    return df[df['ID'].isin(california_ids)]

# Load California station IDs from a text file
def load_california_ids(file_path):
    with open(file_path, 'r') as file:
        # Adjusted to load IDs correctly based on the assumption that 'CA' appears in the line to indicate California stations
        california_ids = [line.strip() for line in file if line.startswith('US1CA') ]
    return california_ids

# Main processing function
def process_files(csv_directory, id_file_path):
    california_ids = load_california_ids(id_file_path)
    
    for filename in os.listdir(csv_directory):
        if filename.endswith('.gz'):
            original_path = os.path.join(csv_directory, filename)
            print(f'Processing {original_path}...')
            
            df = read_gzipped_csv(original_path)
            filtered_df = filter_california_stations(df, california_ids)
            
            # Define new filename with '_clean' postfix
            new_filename = os.path.splitext(filename)[0] + '_clean.csv' # Removed '.gz' and added '_clean.csv'
            new_path = os.path.join(csv_directory, new_filename)
            
            # Save filtered data to new CSV
            filtered_df.to_csv(new_path, index=False)
            print(f'Saved filtered data to {new_path}')


csv_directory = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/' 
id_file_path = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/weather-stations-worldwide-unclean.txt' 
process_files(csv_directory, id_file_path)
