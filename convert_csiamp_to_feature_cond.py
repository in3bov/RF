import os
import glob
import scipy.io as scio
import numpy as np

# Set your input and output directories here
input_dir = 'dataset/wifi/raw'  # Change if your .mat files are elsewhere
output_dir = 'dataset/wifi/converted'  # Converted files will be saved here

os.makedirs(output_dir, exist_ok=True)

mat_files = glob.glob(os.path.join(input_dir, '*.mat'))

for file in mat_files:
    data = scio.loadmat(file)
    if 'CSIamp' in data:
        feature = data['CSIamp'].astype(np.complex64)
        cond = np.zeros_like(feature, dtype=np.complex64)
        out_file = os.path.join(output_dir, os.path.basename(file))
        scio.savemat(out_file, {'feature': feature, 'cond': cond})
        print(f"Converted {file} -> {out_file}")
    else:
        print(f"Skipped {file}: 'CSIamp' key not found.")
