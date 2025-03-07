import os
import pickle
import glob

import os
import glob

# define target directory
base_dir = "./logs/RMaxTS_results"

# store all found pkl file paths
pkl_files = []

# traverse all directories in target directory
for root, dirs, files in os.walk(base_dir):
    # find all pkl files in each directory
    for file in files:
        if file.endswith(".pkl"):
            # add pkl file path to list
            pkl_files.append(os.path.join(root, file))

# # Load all pkl files from all directories
results = []
for pkl_file in pkl_files:
    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)
        for d in data:
            print(d['formal_statement'], d['proof_code'])

print(f"\nTotal number of pkl files loaded: {len(results)}")
