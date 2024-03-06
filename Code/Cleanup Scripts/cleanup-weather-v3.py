import pandas as pd
import gzip
import os

def read_station_info(station_info_path):
    # Define column specifications
    col_specification = [(0, 11), (12, 20), (21, 30)]
    col_names = ['ID', 'LATITUDE', 'LONGITUDE']

    # Read the station info file, skipping the header row
    station_info_df = pd.read_fwf(station_info_path, colspecs=col_specification, names=col_names, header=None, skiprows=1)

    # Remove non-numeric characters from latitude and longitude columns
    station_info_df['LATITUDE'] = station_info_df['LATITUDE'].str.extract(r'([-+]?\d*\.\d+|\d+)').astype(float)
    station_info_df['LONGITUDE'] = station_info_df['LONGITUDE'].str.extract(r'([-+]?\d*\.\d+|\d+)').astype(float)

    return station_info_df

def process_gzipped_csvs(csv_directory, station_info_path):
    # Load station information
    station_info_df = read_station_info(station_info_path)

    # Iterate through each gzipped file in the directory
    for filename in os.listdir(csv_directory):
        if filename.endswith('.gz'):
            # Construct full file path
            file_path = os.path.join(csv_directory, filename)
            print(f'Processing {file_path}...')
            
            # Gunzip and read CSV
            with gzip.open(file_path, 'rt') as gz_file:
                data_df = pd.read_csv(gz_file, names=['ID', 'YEAR/MONTH/DAY', 'ELEMENT', 'DATA VALUE', 'M-FLAG', 'Q-FLAG', 'S-FLAG', 'OBS-TIME'])
            
            # Merge to filter by ID and add latitude and longitude
            merged_df = pd.merge(data_df, station_info_df, on='ID', how='inner')
            
            # Construct new filename with '_clean' postfix
            new_filename = os.path.splitext(filename)[0] + '_clean.csv'
            new_path = os.path.join(csv_directory, new_filename)
            
            # Save filtered and enriched data to new CSV
            merged_df.to_csv(new_path, index=False)
            print(f'Saved filtered data to {new_path}')

# Example usage
csv_directory = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/'  # Update this path
station_info_path = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/california_stations.csv'  # Update this path
process_gzipped_csvs(csv_directory, station_info_path)
