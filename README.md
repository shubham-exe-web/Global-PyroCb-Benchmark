# The Global PyroCb Benchmark 🔥🛰️

[![Dataset](https://img.shields.io/badge/Dataset-Zenodo-blue.svg)](https://zenodo.org/records/21610178)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A 45-Channel Multi-Modal Orbital Dataset for Active Mega-Fire Mapping Under Extreme Atmospheric Occlusion.

## 📖 Overview
As mega-fires become more severe globally, there is a critical need for robust Earth Observation (EO) training datasets. Standard multi-spectral imagery routinely fails during extreme pyrocumulonimbus (pyroCb) events due to absolute atmospheric occlusion by carbonaceous smoke. 

To address this machine learning bottleneck, we introduce **The Global PyroCb Benchmark**. This dataset is a state-of-the-art, multi-sensor data cube specifically engineered for active fire mapping when optical sensors are blinded. It contains 1,500 densely annotated geospatial tiles of recent mega-fires across the Canadian Boreal forests, California, and Australia.

## 🧊 The 45-Channel Tensor Architecture
Each sample is a geographic bounding box of 5.12 × 5.12 km, formatted as a `(512, 512, 45)` float32 tensor precisely co-registered at a 10m spatial resolution.

| Channel Range | Sensor / Modality | Specific Variables |
| :--- | :--- | :--- |
| **Channels 1-4** | Sentinel-1 SAR | Bi-Temporal backscatter (VV/VH at $t_{pre}$ and $t_{active}$) |
| **Channels 5-16** | Sentinel-2 MSI | Multi-Spectral optical and SWIR bands (B1-B12) |
| **Channels 17-24** | Derived Indices | Normalized Burn Ratio (NBR), GLCM variance, structural indices |
| **Channels 25-28** | ERA5 Meteorology | Wind velocities (u/v), Ambient Temperature, Soil Moisture |
| **Channels 29-45** | Optical Baselines | Multi-temporal pre-fire vegetation health parameters |
| **Target Mask** | Ground Truth | Manually curated binary mask of the active fire perimeter |

## 🚀 Quickstart & Usage Examples

The dataset is provided in serialized **TFRecord** format for TensorFlow integration and **Cloud Optimized GeoTIFF (COG)** format for PyTorch/general geospatial workflows.

### 1. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/yourusername/Global-PyroCb-Benchmark.git](https://github.com/yourusername/Global-PyroCb-Benchmark.git)
cd Global-PyroCb-Benchmark
pip install -r requirements.txt
