""" A small demo of using Git submodules to bring in and clean the NSF Awards data, 
    while keeping the files versioned in XetHub. 
"""

import os
import pandas as pd

# if the file is executed as a script
if __name__ == "__main__":

    # Loop over the files in the /raw directory
    directory = os.fsencode("nsf-awards/raw")

    # check if the nsf-awards/clean directory exists, if not create it
    if not os.path.exists("nsf-awards/clean"):
        os.makedirs("nsf-awards/clean")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # load the parquet file into a pandas dataframe
        df = pd.read_parquet("nsf-awards/raw/" + filename)

        # drop all nas in the dataframe inplace
        df.dropna(inplace=True)

        # save the dataframe as a parquet file in the /clean directory
        df.to_parquet("nsf-awards/clean/" + filename)
