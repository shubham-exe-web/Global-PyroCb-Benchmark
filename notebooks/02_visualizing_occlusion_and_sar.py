import numpy as np
import matplotlib.subplots as plt

def visualize_occlusion_vs_sar():
    """Generates a visualization contrasting optical occlusion with SAR penetration."""
    tile_size = 512
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Multi-Modal Visibility Under Extreme Atmospheric Occlusion', fontsize=16)

    # Mock Data: Severe Smoke (Optical)
    optical_rgb = np.clip(np.random.uniform(0.7, 0.9, (tile_size, tile_size, 3)) + 
                          np.random.normal(0, 0.05, (tile_size, tile_size, 3)), 0, 1)
    
    # Mock Data: SAR Backscatter (Structural Deformation)
    sar_vv = np.linspace(0.2, 0.8, tile_size).reshape(-1, 1) * np.ones((1, tile_size))
    sar_vv += np.random.normal(0, 0.1, (tile_size, tile_size))
    y, x = np.ogrid[:tile_size, :tile_size]
    mask_condition = ((x - 256)**2 / 160**2 + (y - 256)**2 / 220**2) <= 1
    sar_vv[mask_condition] -= 0.35 
    
    truth_mask = np.zeros((tile_size, tile_size))
    truth_mask[mask_condition] = 1

    axes[0].imshow(optical_rgb)
    axes[0].set_title('A: Sentinel-2 Optical Composite\n(Complete Signal Extinction)')
    axes[0].axis('off')

    axes[1].imshow(sar_vv, cmap='gray')
    axes[1].set_title('B: Sentinel-1 SAR Backscatter\n(Clear Structural Burn Scar)')
    axes[1].axis('off')

    axes[2].imshow(sar_vv, cmap='gray')
    axes[2].imshow(truth_mask, cmap='Reds', alpha=0.4)
    axes[2].set_title('C: Validated Active Fire Label\n(Topologically Aligned)')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_occlusion_vs_sar()
