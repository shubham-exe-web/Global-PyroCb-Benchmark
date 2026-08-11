import numpy as np

def optical_only_baseline(tensor_batch):
    """
    Simulates optical algorithm isolation by masking SAR and Meteorological channels.
    Forces the model to predict using only occluded optical/SWIR bands.
    
    Args:
        tensor_batch: A numpy array of shape (Batch, Height, Width, 45)
    Returns:
        Masked tensor batch of the same shape.
    """
    print("Applying occlusion mask to tensor batch...")
    # Zero-out Channels 1-4 (SAR) 
    tensor_batch[:, :, :, 0:4] = 0.0
    # Zero-out Channels 17-45 (Derived Indices, Meteorology, Baselines)
    tensor_batch[:, :, :, 16:45] = 0.0
    
    print("Masking complete. Model will rely solely on Channels 5-16.")
    return tensor_batch

if __name__ == "__main__":
    # Test with a dummy tensor
    dummy_batch = np.random.rand(1, 512, 512, 45)
    masked_batch = optical_only_baseline(dummy_batch)
