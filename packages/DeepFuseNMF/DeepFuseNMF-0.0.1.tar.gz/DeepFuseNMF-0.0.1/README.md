# Interpretable super-resolution dimension reduction of spatial transcriptomics data by DeepFuseNMF

## Overview

![alt](Overview.jpg)

DeepFuseNMF is based on a multi-modal neural network that takes advantage of the high-dimensionality of transcriptomics
data and the super-resolution of image data to achieve interpretable super-resolution dimension reduction. 
The high-dimensional expression data enable refined functional annotations and the super-resolution image data help to
enhance the spatial resolution.

Based on the super-resolution embedding and the reconstruction of gene expressions, DeepFuseNMF can then perform
super-resolution downstream analyses, such as spatial domain detection, gene expression recovery, and identification of
embedding-associated genes as well as super-resolution cluster-associated genes.

## Installation
Please install `DeepFuseNMF` from pypi with:

```bash
pip install deepfusenmf
```

Or clone this repository and use

```bash
pip install -e .
```

in the root of this repository.

## Quick start
Prepare your data and run the following command:

```bash
python run_DeepFuseNMF.py --config config.json --device 0 --verbose
```

`config.json` is a JSON file that contains the paths to the input data and the output directory. The JSON file should look like this:
```json
{
    "settings": {
        "root_path": "your_root_path",
        "project": "your_project_name"
    },
    "sections": [
        {
            "name": "name of section A",
            "image_path": "image path of section A",
            "spot_coord_path": "spot coordinate path of section A",
            "spot_exp_path": "spot expression path of section A"
        },
        { // multi-sections is supported
            "name": "name of section B",
            "image_path": "image path of section B",
            "spot_coord_path": "spot coordinate path of section B",
            "spot_exp_path": "spot expression path of section B"
        }
    ],
    "paras": {
        "scale_factor": [2, 2], // the scale factor of the input images, integer for single section, list for multi-sections
        "radius": [65, 65] // the radius of the spots, integer for single section, list for multi-sections
    }
}
```
All parameters of `run_DeepFuseNMF.py` are optional. The following are the:

- `--config` or `-c`: the path to the configuration file
- `--rank` or `-r`: the rank / number of components of the NMF model, default is 20
- `--seed` or `-s`: the random seed, default is 123
- `--device` or `-d`: the device to run the model, e.g., 0, 1, 2, etc, default is 0
- `--save_score`: whether to save the model, default is `True`
- `--spot_wise`: whether to save the spot-wise results, use `--spot_wise` to save the spot-wise results
- `--verbose`: whether to print the log information, use `--verbose` to print the log information

Please refer to the `Tutorial/Tutorial.ipynb` and `configs/README.md` for more details.