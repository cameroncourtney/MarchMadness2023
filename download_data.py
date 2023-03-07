import os
import urllib.request
import urllib.parse
import csv


# Failed Script to download Bartovik data. Kept getting HTTP as Responses.
# Web page is updated dynamically through JavaScript, so this solution would not work.
# Found a Chrome Extension that allowed me to easily download the data I wanted.
# Base URL
url_base = "dummyBaseUrl"
download_dir = "dummyDirectory"

# Define the years and types of CSV files to download
years = [str(y) for y in range(2015, 2016) if y != 2020]
types = ['P', 'PC']

# Loop over the years and types and download the CSV files
for year in years:
    for type in types:
        # Construct the URL for the CSV file
        url = url_base.format(year, type)

        # Encode the URL to handle any special characters in the URL
        encoded_url = urllib.parse.quote(url, safe=':/?&=')

        # Construct the filename for the CSV file
        filename = os.path.join(download_dir, f'{year}-{type}.csv')

        # Download the CSV file and save it to disk
        urllib.request.urlretrieve(encoded_url, filename)

        # Print a message indicating that the file was downloaded
        print(f"Downloaded {filename}")

        # Read in the CSV file and write it to a new file
        with open(filename, 'r') as input_file, open(f'{year}-{type}-copy.csv', 'w') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            for row in reader:
                writer.writerow(row)

        # Print a message indicating that the file was processed
        print(f"Processed {filename}")