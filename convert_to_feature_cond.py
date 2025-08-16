import scipy.io as scio
import numpy as np
import glob
import os

# Set your input and output directories
input_dir = 'NTU_Fi_HAR/train_amp/fall'
output_dir = 'dataset/wifi/raw'
os.makedirs(output_dir, exist_ok=True)

for file in glob.glob(f'{input_dir}/*.mat'):
    data = scio.loadmat(file)
    # Try to find a suitable variable for 'feature'. Adjust 'amp' if needed.
    if 'amp' in data:
        feature = data['amp'].astype(np.complex64)
    else:
        # If 'amp' is not present, skip this file
        print(f"Skipping {file}: no 'amp' variable found.")
        continue
    # Create a dummy 'cond' variable with the same shape as 'feature'
    cond = np.zeros_like(feature, dtype=np.complex64)
    out_file = os.path.join(output_dir, os.path.basename(file))
    scio.savemat(out_file, {'feature': feature, 'cond': cond})
    print(f"Converted {file} -> {out_file}")
