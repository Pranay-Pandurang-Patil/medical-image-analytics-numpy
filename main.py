import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# -----------------------------------
# CREATE OUTPUT FOLDER
# -----------------------------------

os.makedirs("output", exist_ok=True)

# -----------------------------------
# MAIN WINDOW
# -----------------------------------

root = tk.Tk()

root.title("Medical Image Analytics System")

root.geometry("900x650")

root.configure(bg="#1e1e1e")

# -----------------------------------
# GLOBAL VARIABLE
# -----------------------------------

selected_image_path = None

# -----------------------------------
# TITLE
# -----------------------------------

heading = tk.Label(
    root,
    text="Medical Image Analytics using NumPy",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1e1e1e"
)

heading.pack(pady=5)

subheading = tk.Label(
    root,
    text="AI-style Medical Scan Processing Dashboard",
    font=("Arial", 11),
    fg="#bbbbbb",
    bg="#1e1e1e"
)

subheading.pack(pady=(0,10))

# -----------------------------------
# IMAGE FRAME
# -----------------------------------

image_frame = tk.Frame(
    root,
    bg="#2b2b2b",
    bd=3,
    relief="ridge"
)

image_frame.pack(pady=10)

image_label = tk.Label(
    image_frame,
    bg="#2b2b2b"
)

image_label.pack(padx=10, pady=10)

# -----------------------------------
# INFO LABEL
# -----------------------------------

info_label = tk.Label(
    root,
    text="No image selected",
    font=("Arial", 11),
    fg="white",
    bg="#1e1e1e"
)

info_label.pack(pady=5)

# -----------------------------------
# REPORT TITLE
# -----------------------------------

report_title = tk.Label(
    root,
    text="Analysis Report",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#1e1e1e"
)

report_title.pack(pady=(10,5))

# -----------------------------------
# REPORT BOX
# -----------------------------------

report_frame = tk.Frame(
    root,
    bg="#2b2b2b",
    bd=3,
    relief="ridge"
)

report_frame.pack(pady=5)

report_scroll = tk.Scrollbar(report_frame)

report_scroll.pack(
    side=tk.RIGHT,
    fill=tk.Y
)

report_box = tk.Text(
    report_frame,
    width=65,
    height=6,
    font=("Consolas", 11),
    bg="#121212",
    fg="#00ff99",
    insertbackground="white",
    relief="flat",
    yscrollcommand=report_scroll.set
)

report_box.pack(
    side=tk.LEFT,
    padx=10,
    pady=10
)

report_scroll.config(
    command=report_box.yview
)

# -----------------------------------
# SELECT IMAGE FUNCTION
# -----------------------------------

def select_image():

    global selected_image_path

    file_path = filedialog.askopenfilename(
        title="Select Medical Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if file_path:

        selected_image_path = file_path

        preview_image = Image.open(file_path)

        preview_image = preview_image.resize((180,180))

        tk_image = ImageTk.PhotoImage(preview_image)

        image_label.configure(image=tk_image)

        image_label.image = tk_image

        info_label.configure(
            text=f"Selected Image:\n{os.path.basename(file_path)}"
        )

# -----------------------------------
# PROCESS IMAGE FUNCTION
# -----------------------------------

def process_image():

    global selected_image_path

    if selected_image_path is None:

        messagebox.showerror(
            "Error",
            "Please select an image first"
        )

        return

    # -----------------------------------
    # LOAD IMAGE
    # -----------------------------------

    image = Image.open(selected_image_path)

    gray_image = image.convert("L")

    img_array = np.array(gray_image)

    # -----------------------------------
    # EDGE DETECTION
    # -----------------------------------

    edges = np.abs(
        np.diff(
            img_array.astype(np.int32),
            axis=1
        )
    )

    edges = edges * 10

    edges = np.clip(edges, 0, 255)

    edges = edges.astype(np.uint8)

    # -----------------------------------
    # CONTRAST ENHANCEMENT
    # -----------------------------------

    min_pixel = np.min(img_array)

    max_pixel = np.max(img_array)

    contrast_array = (
        (img_array - min_pixel)
        /
        (max_pixel - min_pixel)
    ) * 255

    contrast_array = contrast_array.astype(np.uint8)

    # -----------------------------------
    # BRIGHT REGION DETECTION
    # -----------------------------------

    threshold = 200

    bright_regions = img_array > threshold

    bright_regions = (
        bright_regions.astype(np.uint8) * 255
    )

    # -----------------------------------
    # IMAGE STATISTICS
    # -----------------------------------

    mean_brightness = np.mean(img_array)

    maximum_pixel = np.max(img_array)

    minimum_pixel = np.min(img_array)

    std_deviation = np.std(img_array)

    # -----------------------------------
    # SAVE OUTPUTS
    # -----------------------------------

    Image.fromarray(edges).save(
        "output/edge_image.png"
    )

    Image.fromarray(contrast_array).save(
        "output/contrast_image.png"
    )

    Image.fromarray(bright_regions).save(
        "output/bright_regions.png"
    )

    # -----------------------------------
    # GENERATE REPORT
    # -----------------------------------

    report = f"""
MEDICAL IMAGE ANALYSIS REPORT
---------------------------------

Image Shape:
{img_array.shape}

Datatype:
{img_array.dtype}

Mean Brightness:
{mean_brightness:.2f}

Maximum Pixel Value:
{maximum_pixel}

Minimum Pixel Value:
{minimum_pixel}

Standard Deviation:
{std_deviation:.2f}

Threshold Used:
{threshold}

Interpretation:
- Image processed successfully
- Edge detection completed
- Contrast enhancement completed
- Bright region segmentation completed
- Histogram analysis completed

Project:
Medical Image Analytics using NumPy
"""

    with open(
        "output/report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    # -----------------------------------
    # SHOW REPORT IN GUI
    # -----------------------------------

    report_box.delete("1.0", tk.END)

    report_box.insert(
        tk.END,
        report
    )

    # -----------------------------------
    # DISPLAY OUTPUTS
    # -----------------------------------

    plt.figure(figsize=(18,5))

    # Original image
    plt.subplot(1,4,1)

    plt.imshow(img_array, cmap='gray')

    plt.title("Original")

    plt.axis("off")

    # Edge detection
    plt.subplot(1,4,2)

    plt.imshow(edges, cmap='gray')

    plt.title("Edges")

    plt.axis("off")

    # Contrast enhanced
    plt.subplot(1,4,3)

    plt.imshow(contrast_array, cmap='gray')

    plt.title("Contrast")

    plt.axis("off")

    # Bright regions
    plt.subplot(1,4,4)

    plt.imshow(bright_regions, cmap='gray')

    plt.title("Bright Regions")

    plt.axis("off")

    plt.show()

    # -----------------------------------
    # HISTOGRAM
    # -----------------------------------

    plt.figure(figsize=(10,5))

    plt.hist(
        img_array.flatten(),
        bins=256,
        range=[0,255],
        color='gray',
        edgecolor='black',
        alpha=0.8
    )

    plt.title(
        "Pixel Intensity Histogram"
    )

    plt.xlabel(
        "Pixel Intensity"
    )

    plt.ylabel(
        "Number of Pixels"
    )

    plt.xlim(0,255)

    plt.grid(True)

    plt.show()

    # -----------------------------------
    # SUCCESS MESSAGE
    # -----------------------------------

    messagebox.showinfo(
        "Success",
        "Image processed successfully!\n\nOutputs saved inside output folder."
    )

# -----------------------------------
# BUTTON FRAME
# -----------------------------------

button_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

button_frame.pack(pady=10)

# -----------------------------------
# SELECT BUTTON
# -----------------------------------

select_button = tk.Button(
    button_frame,
    text="Select Medical Image",
    font=("Arial", 11, "bold"),
    bg="#00b894",
    fg="white",
    activebackground="#00d1a0",
    padx=18,
    pady=8,
    bd=0,
    cursor="hand2",
    command=select_image
)

select_button.grid(
    row=0,
    column=0,
    padx=10
)

# -----------------------------------
# PROCESS BUTTON
# -----------------------------------

process_button = tk.Button(
    button_frame,
    text="Process Image",
    font=("Arial", 11, "bold"),
    bg="#0984e3",
    fg="white",
    activebackground="#2d9cff",
    padx=18,
    pady=8,
    bd=0,
    cursor="hand2",
    command=process_image
)

process_button.grid(
    row=0,
    column=1,
    padx=10
)

# -----------------------------------
# OPEN OUTPUT FOLDER BUTTON
# -----------------------------------

output_button = tk.Button(
    button_frame,
    text="Open Output Folder",
    font=("Arial", 11, "bold"),
    bg="#6c5ce7",
    fg="white",
    activebackground="#7d6cff",
    padx=18,
    pady=8,
    bd=0,
    cursor="hand2",
    command=lambda: os.startfile("output")
)

output_button.grid(
    row=0,
    column=2,
    padx=10
)

# -----------------------------------
# RUN APPLICATION
# -----------------------------------

root.mainloop()