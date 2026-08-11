import numpy as np
import rasterio

def load_and_slice_tensor(filepath):
    """
    Loads a 45-channel Cloud Optimized GeoTIFF (COG) and slices it into modalities.
    """
    print(f"Loading tensor from {filepath}...")
    
    # Load the 45-channel tensor tile
    with rasterio.open(filepath) as src:
        # Read all bands and transpose to (Height, Width, Channels)
        tensor = src.read().transpose(1, 2, 0)
    
    print(f"Tensor loaded successfully with shape: {tensor.shape}")

    # Slice the tensor into distinct physical modalities
    sar_inputs = tensor[:, :, 0:4]       # Channels 1-4: Sentinel-1 Bi-Temporal
    optical_inputs = tensor[:, :, 4:16]  # Channels 5-16: Sentinel-2 MSI
    derived_indices = tensor[:, :, 16:24]# Channels 17-24: NBR, GLCM
    meteo_vectors = tensor[:, :, 24:28]  # Channels 25-28: ERA5 Variables
    
    print("Slicing complete:")
    print(f"- SAR Shape: {sar_inputs.shape}")
    print(f"- Optical Shape: {optical_inputs.shape}")
    print(f"- Meteorology Shape: {meteo_vectors.shape}")
    
    return sar_inputs, optical_inputs, meteo_vectors

if __name__ == "__main__":
    # Replace with the path to your downloaded sample file
    # load_and_slice_tensor('../data/sample_pyrocb_tile_001.tif')
    print("Ready to process COG files.")
