import scipy.io as scio
import glob

count = 0
for file in glob.glob('dataset/wifi/raw/*.mat'):
    data = scio.loadmat(file)
    if 'feature' in data and data['feature'].size > 0:
        print(f"{file}: feature shape = {data['feature'].shape}")
        count += 1
print(f"Total files with non-empty feature: {count}")
