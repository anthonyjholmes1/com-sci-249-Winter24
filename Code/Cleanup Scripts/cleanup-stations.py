import pandas as pd
import os

def filter_california_stations(input_file, output_file):
    # Define the column indices based on the provided specifications
    # Adjust indices as needed, Python uses 0-based indexing
    columns_spec = [
        (0, 11),  # ID
        (12, 20), # LATITUDE
        (21, 30), # LONGITUDE
        (31, 37), # ELEVATION
        (38, 40), # STATE
        (41, 71), # NAME
        (72, 75), # GSN FLAG
        (76, 79), # HCN/CRN FLAG
        (80, 85)  # WMO ID
    ]
    column_names = ['ID', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'STATE', 'NAME', 'GSN_FLAG', 'HCN_CRN_FLAG', 'WMO_ID']
    
    # Read the file with fixed-width columns
    df = pd.read_fwf(input_file, colspecs=columns_spec, header=None, names=column_names)
    
    # Filter for stations in California, USA
    ca_stations = df[(df['ID'].str.startswith('US')) & (df['STATE'] == 'CA')]
    
    # Write the filtered DataFrame to a new file
    ca_stations.to_csv(output_file, index=False)
    print(f'Filtered data written to {output_file}')

# Example usage
input_file = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/weather-stations-worldwide-unclean.txt'  # Update this path to your input file's location
output_file = 'california_stations.csv'   # Desired path for the output file
filter_california_stations(input_file, output_file)

