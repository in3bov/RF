import scipy.io as scio
import glob

sample_rate = 512  # Change this if your model uses a different sample_rate
short_files = []

for file in glob.glob('dataset/wifi/raw/*.mat'):
    data = scio.loadmat(file)
    if 'feature' in data:
        shape = data['feature'].shape
        if shape[0] < sample_rate:
            short_files.append(file)

# Write the list to a file
with open('short_files.txt', 'w') as f:
    for file in short_files:
        f.write(file + '\n')

print(f"Total files with feature shorter than sample_rate: {len(short_files)}")
print("List saved to short_files.txt")
