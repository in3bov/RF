import scipy.io as scio
import numpy as np
import os

os.makedirs('dataset/wifi/raw', exist_ok=True)
feature = np.random.randn(64, 90).astype(np.complex64)  # Example shape, adjust as needed
cond = np.zeros_like(feature, dtype=np.complex64)
scio.savemat('dataset/wifi/raw/example_valid.mat', {'feature': feature, 'cond': cond})
print('Created dataset/wifi/raw/example_valid.mat with shape', feature.shape)
