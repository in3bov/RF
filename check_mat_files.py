import scipy.io as scio
import glob

missing_feature = []
missing_cond = []

for file in glob.glob('dataset/wifi/raw/*.mat'):
    data = scio.loadmat(file)
    if 'feature' not in data:
        print(f"Missing 'feature' in: {file}")
        missing_feature.append(file)
    if 'cond' not in data:
        print(f"Missing 'cond' in: {file}")
        missing_cond.append(file)

print(f"\nTotal files missing 'feature': {len(missing_feature)}")
print(f"Total files missing 'cond': {len(missing_cond)}")
