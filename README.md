# Gemini-Watermark-Remover
A high performance Python tool designed to losslessly remove watermarks from Nano Banana (Gemini) generated images.

Unlike AI inpainting tools that "guess" what pixels should look like, this script uses **mathematical reversal** to recover the exact original pixel values underneath the watermark.

## Features
* **Zero Quality Loss**: Recovers the original pixels mathematically rather than blurring or inpainting.
* **Drag & Drop**: Simply drag your image onto the script to process it.
* **Auto Detection**: Automatically detects image resolution to apply the correct watermark mask (Small vs. Large).
* **Local Processing**: Runs 100% offline. No grubby companies to hold your images.

# Before
![Before](https://raw.githubusercontent.com/duckiedevelop/Gemini-Watermark-Remover/refs/heads/main/before1.png)
# After
![After](https://raw.githubusercontent.com/duckiedevelop/Gemini-Watermark-Remover/refs/heads/main/after1.png)
## Prerequisites

1.  **Python** (3.9 or newer, tested on 3.11.5)
2.  **Required Libraries**:
    ```bash
    pip install opencv-python numpy
    ```

## Installation

1.  Download `gemini.py`
2.  **Critical Step**: You must place the alpha mask files in the same directory as the script.
    * `48.png`: The mask for standard resolution images.
    * `96.png`: The mask for high-resolution images (>1024px).
    *(Ensure these files are named exactly `48.png` and `96.png` as the script expects those names)*.
    
## The Math
Credit to [Jad](https://github.com/journey-ad) for the logic/math of the removal

### Compositing Formula: Watermarked = (Logo * Alpha) + (Original * (1 - Alpha))
Watermarked: The pixel value with the watermark (The input image).

Logo: The watermark color value (White = 255).

Alpha: The transparency value (0.0 to 1.0) derived from the mask files.

Original: The raw pixel value we want to recover.

To get the "original" image, basic reverse engineering must take place

### Reverse Engineered Formula: Original = (Watermarked - (Logo * Alpha)) / (1 - Alpha)


## Usage

**Method 1: Drag and Drop (Windows)**
Download your image directly from the Gemini website. Do not right click and save the image. This prevents the watermark removal process
Simply drag your `.jpg` or `.png` file and drop it directly onto the Python script icon.

**Method 2: Command Line**
```bash
python gemini.py input_image.png
