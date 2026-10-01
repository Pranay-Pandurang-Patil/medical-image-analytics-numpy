# Medical Image Analytics using NumPy

A beginner-friendly medical image analysis project that demonstrates how **NumPy** can be used for basic image processing and pixel-level analysis.

The project works with X-ray images and performs several operations using NumPy arrays.

## Features

- X-ray image loading
- Grayscale image processing
- Pixel intensity analysis
- Mean, minimum, maximum and standard deviation calculation
- Contrast enhancement
- Basic edge detection
- Difference map generation
- Bright-region segmentation
- Pixel intensity histogram analysis
- Text-based analysis report
- Simple graphical interface

## Technologies Used

- Python
- NumPy
- Pillow
- Matplotlib
- Tkinter

## Project Structure

```text
medical-image-analytics-numpy/
│
├── images/
│   ├── xray1.png
│   └── xray2.png
│
├── output/
│   ├── bright_regions.png
│   ├── contrast_image.png
│   ├── difference_map.png
│   ├── edge_image.png
│   └── report.txt
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Pranay-Pandurang-Patil/medical-image-analytics-numpy.git
```

Move into the project directory:

```bash
cd medical-image-analytics-numpy
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

Use the GUI to select an X-ray image and perform the available image analysis operations.

## What I Learned

This project was built to practice practical NumPy array operations, including:

- Working with multidimensional arrays
- Pixel-level image manipulation
- Array normalization
- Statistical calculations
- Boolean masking
- Difference operations
- Basic image segmentation
- Generating analysis results from numerical data

## Purpose

The main goal of this project is to understand how NumPy can be applied to a real-world image-processing problem without relying on high-level computer vision libraries such as OpenCV.

## Note

This project is intended for educational purposes and does not provide medical diagnosis or clinical analysis.

## License

This project is licensed under the MIT License.
```
