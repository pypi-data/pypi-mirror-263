import csv
import json
import math
import os
import time
import cv2
from matplotlib.ticker import MaxNLocator
import torch
from tqdm import tqdm
import matplotlib.pyplot as plt
from ultralytics import YOLO
from typing import Optional, List, Dict, Tuple
import numpy as np
from PIL import Image
import seaborn as sns
import pandas as pd

from .data_handling import export_to_csv
from .model_operations import process_image, segregate_images
from .utils import custom_sort_key
from .theme import console, INFO_STYLE, SUCCESS_STYLE
from .labels_operations import (
    Label,
    convert_to_pixels,
    extract_label_files,
    extract_label_sizes,
    read_labels,
    read_yolo_labels,
)


def evaluate_dataset(
    test_images_folder: str,
    model_path: Optional[str] = None,
    num_images: int = 100,
    verbose: bool = False,
    print_results: bool = False,
    copy_images: bool = False,
) -> List[dict]:
    """
    Main function to execute the YOLO model analysis script.

    Args:
    model_path (str): Path to the model weights file.
    test_images_folder (str): Path to the test images folder.
    num_images (int): Number of images to separate for additional augmentation.
    verbose (bool): Enable verbose output for model predictions.
    print_results (bool): Print the sorted image data results.
    copy_images (bool): Copy images to a separate folder for additional augmentation.

    Returns:
    List[dict]: A list of dictionaries containing sorted image data based on the evaluation.
    """

    start_time = time.time()

    images = [
        os.path.join(test_images_folder, file)
        for file in os.listdir(test_images_folder)
        if file.endswith(".jpg") or file.endswith(".png")
    ]

    if model_path is None or not os.path.exists(model_path):
        console.print(
            "Model path not provided or not found. Using default YOLO model.",
            style=INFO_STYLE,
        )
        model = YOLO("yolov8n")
    else:
        model = YOLO(model_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    image_data_list = []
    predictions_dict = {}

    for image_path in tqdm(images, desc="Processing Images"):
        image_data, predictions = process_image(image_path, model, verbose=verbose)
        image_data_list.append(image_data)
        predictions_dict[image_path] = predictions

    sorted_image_data = sorted(image_data_list, key=custom_sort_key, reverse=True)

    if copy_images:
        segregate_images(image_data_list, predictions_dict, num_images=num_images)

    if print_results:
        export_to_csv(sorted_image_data)

    end_time = time.time()
    duration = end_time - start_time
    console.print(
        f"Script executed successfully in {duration:.2f} seconds.", style=SUCCESS_STYLE
    )

    return sorted_image_data


def calculate_bb_area(label: Label) -> float:
    """
    Calculate the surface area of a bounding box from a Label object.

    The Label object contains class_id, center_x, center_y, width, and height.
    This function calculates the surface area of the bounding box defined by the
    width and height in the Label object.

    Args:
    label (Label): A Label object representing the bounding box and class ID.

    Returns:
    float: The fractional surface area of the bounding box, as a proportion of the total image area.
    """

    area = label.width * label.height

    return area


def plot_bb_distribution(label_paths: List[str], save: bool = False) -> None:
    """
    Plots the distribution of bounding box areas from a list of YOLO label file paths.

    Args:
        label_paths (List[str]): A list of paths to YOLO label files.
        save (bool): If True, saves the plot to a file named 'bbox_distribution.png' in
                     the 'pythonpix_results' directory. Defaults to False.
    """
    areas = []

    for path in label_paths:
        labels = read_yolo_labels(path)
        for label in labels:
            area = calculate_bb_area(label) * 100
            areas.append(area)

    plt.figure(figsize=(10, 6))
    plt.hist(areas, bins=30, color="blue", alpha=0.7)
    plt.title("Distribution of Bounding Box Areas")
    plt.xlabel("Area (% of original image)")
    plt.ylabel("Frequency")

    if save:
        os.makedirs("pythopix_results", exist_ok=True)
        plt.savefig("pythopix_results/bbox_distribution.png")

    plt.show()


def plot_label_size_distribution(
    input_folder: str,
    allowed_classes: List[int] = [0],
    save: bool = False,
    show: bool = True,
    scatter: bool = False,
) -> None:
    """
    Plots the distribution of label widths and heights in pixels from YOLO label files for specified allowed classes.

    This function reads YOLO label files in the specified input folder, extracts
    the widths and heights of bounding boxes in pixels for the allowed classes, and plots their distributions in
    two subplots. Additionally, it prints the average width and height. If the save flag is set, it saves the plot to a specified path.

    Parameters:
    - input_folder (str): Path to the folder containing images and YOLO label files.
    - allowed_classes (List[int], optional): A list of class IDs for which bounding box sizes should be calculated.
    - save (bool): If True, saves the plot to 'pythopix_results/figs/label_size_distribution.png'. Defaults to False.
    - show (bool): If True, shows the plot. Defaults to True
    - scatter (bool): If True, shows scatter points. Default to False

    Returns:
    - None
    """

    label_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.endswith(".txt")
    ]

    widths, heights = extract_label_sizes(label_files, allowed_classes=allowed_classes)

    average_width = np.mean(widths) if widths else 0
    average_height = np.mean(heights) if heights else 0
    std_dev_width = np.std(widths) if widths else 0
    std_dev_height = np.std(heights) if heights else 0
    variance_width = np.var(widths) if widths else 0
    variance_height = np.var(heights) if heights else 0
    range_width = np.ptp(widths) if widths else 0  # Peak-to-peak (max-min)
    range_height = np.ptp(heights) if heights else 0

    print(
        f"Average Width: {average_width:.2f} pixels, Standard Deviation: {std_dev_width:.2f}, Variance: {variance_width:.2f}, Range: {range_width}"
    )
    print(
        f"Average Height: {average_height:.2f} pixels, Standard Deviation: {std_dev_height:.2f}, Variance: {variance_height:.2f}, Range: {range_height}"
    )

    plt.figure(figsize=(6, 4))
    plt.hist(widths, bins=30, color="blue", alpha=0.7)
    plt.title("Label Width Distribution in Pixels")
    plt.xlabel("Width (pixels)")
    plt.ylabel("Frequency")
    if save:
        os.makedirs("pythopix_results/figs", exist_ok=True)
        plt.savefig("pythopix_results/figs/label_width_distribution.png")
    if show:
        plt.show()

    plt.figure(figsize=(6, 4))
    plt.hist(heights, bins=30, color="green", alpha=0.7)
    plt.title("Label Height Distribution in Pixels")
    plt.xlabel("Height (pixels)")
    plt.ylabel("Frequency")
    if save:
        plt.savefig("pythopix_results/figs/label_height_distribution.png")
    if show:
        plt.show()

    data = pd.DataFrame({"Width": widths, "Height": heights})
    g = sns.jointplot(data=data, x="Width", y="Height", kind="kde", space=0, fill=True)
    if scatter:
        g.plot_joint(plt.scatter, color="b", s=5, alpha=0.6)

    g.set_axis_labels("Width (pixels)", "Height (pixels)", fontsize=12)
    g.figure.suptitle("Width vs Height Label Distribution")
    if save:
        g.figure.savefig("pythopix_results/figs/width_vs_height_kde_distribution.png")
    if show:
        plt.show()


def plot_label_ratios(
    input_folder: str,
    allowed_classes: List[int] = [0],
    save: bool = False,
    show: bool = True,
) -> None:
    """
    Plots and optionally saves the distribution of label aspect ratios (width/height)
    in a dataset, as extracted from YOLO label files, for specified allowed classes.

    This function reads each label file, finds the corresponding image file to
    obtain actual dimensions, calculates the aspect ratio of the bounding boxes,
    and generates a histogram of these ratios.

    Parameters:
    - input_folder (str): Path to the folder containing images and their corresponding YOLO label files.
    - allowed_classes (List[int], optional): A list of class IDs for which bounding box aspect ratios should be calculated.
    - save (bool, optional): If set to `True`, the plot is saved to 'pythopix_results/figs/label_ratios.png'. Defaults to `False`.
    - show (bool): If True, shows the plot. Defaults to True

    Returns:
    - None: Based on the `save` parameter, the function either displays the plot or saves it to a specified directory.
    """

    label_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.endswith(".txt")
    ]
    widths, heights = extract_label_sizes(label_files, allowed_classes=allowed_classes)

    ratios = [
        w / h if h != 0 else 0 for w, h in zip(widths, heights)
    ]  # Avoid division by zero

    average_aspect_ratio = sum(ratios) / len(ratios) if ratios else 0
    print(f"Average Aspect Ratio: {average_aspect_ratio:.2f}")

    plt.figure(figsize=(8, 6))
    plt.hist(ratios, bins=30, color="purple", alpha=0.7)
    plt.title("Label Aspect Ratio Distribution")
    plt.xlabel("Aspect Ratio (Width/Height)")
    plt.ylabel("Frequency")
    plt.grid(True)

    if save:
        os.makedirs("pythopix_results/figs", exist_ok=True)
        plt.savefig("pythopix_results/figs/label_ratios.png")

    if show:
        plt.show()


def calculate_segmented_metrics(
    folder_path: str,
    model: YOLO = None,
    model_path: str = None,
    segment_number: int = 4,
    save_data: bool = False,
) -> Dict[str, Dict[str, float]]:
    """
    Processes a folder of images, dividing bounding boxes into segments based on their sizes,
    calculates metrics for each segment, and counts the total number of labels per segment.

    Args:
    folder_path (str): Path to the folder containing images and corresponding YOLO label files.
    model (YOLO, optional): An instance of the YOLO model. If None, model is loaded from model_path.
    model_path (str, optional): Path to load the YOLO model, used if model is None.
    segment_number (int, optional): Number of segments to divide the bounding boxes into based on their sizes.
    save_data (bool, optional): If True, exports the metrics to a JSON file.

    Returns:
    Dict[str, Dict[str, float]]: A dictionary where the key is the segment range (e.g., '0-0.25'),
    and the value is a dictionary containing the counts of false positives, false negatives, total box loss, and total label count for that segment.
    """

    if model is None:
        if model_path is not None:
            model = YOLO(model_path)
        else:
            print("Model path not provided or not found. Using default YOLO model.")
            model = YOLO("yolov8n")

    label_files = extract_label_files(folder_path, label_type="txt")

    all_bb_areas = []
    for label_file in label_files:
        labels = read_yolo_labels(label_file)
        for label in labels:
            area = calculate_bb_area(label)
            all_bb_areas.append(area)

    max_area = max(all_bb_areas)
    min_area = min(all_bb_areas)
    segment_size = (max_area - min_area) / segment_number
    segments = [
        (
            round(min_area + i * segment_size, 2),
            round(min_area + (i + 1) * segment_size, 2),
        )
        for i in range(segment_number)
    ]

    metrics_by_segment = {
        f"{seg[0]:.2f}-{seg[1]:.2f}": {
            "false_positives_count": 0,
            "false_negatives_count": 0,
            "total_box_loss": 0,
            "label_count": 0,
        }
        for seg in segments
    }

    for label_file in tqdm(label_files, desc="Calculating metrics"):
        image_file = label_file.replace(".txt", ".png")
        labels = read_yolo_labels(label_file)

        for label in labels:
            area = calculate_bb_area(label)
            for seg in segments:
                if seg[0] <= area < seg[1]:
                    segment_key = f"{seg[0]:.2f}-{seg[1]:.2f}"
                    image_data, _ = process_image(image_file, model, verbose=False)
                    metrics_by_segment[segment_key]["false_positives_count"] += float(
                        image_data.false_positives
                    )
                    metrics_by_segment[segment_key]["false_negatives_count"] += float(
                        image_data.false_negatives
                    )
                    metrics_by_segment[segment_key]["total_box_loss"] += float(
                        image_data.box_loss
                    )
                    metrics_by_segment[segment_key]["label_count"] += 1

    for segment, data in metrics_by_segment.items():
        data["total_box_loss"] = round(data["total_box_loss"], 2)
        data["average_false_positives_count"] = round(
            data["false_positives_count"] / data["label_count"], 2
        )
        data["average_false_negatives_count"] = round(
            data["false_negatives_count"] / data["label_count"], 2
        )
        data["average_box_loss"] = round(
            data["total_box_loss"] / data["label_count"], 2
        )

    if save_data:
        os.makedirs("pythopix_results", exist_ok=True)
        output_file_path = "pythopix_results/segmented_metrics.json"
        with open(output_file_path, "w") as json_file:
            json.dump(metrics_by_segment, json_file, indent=4)

        print(f"Metrics saved to {output_file_path}")

    return metrics_by_segment


def plot_metrics_by_segment(
    metrics_path: str,
    save: bool = False,
    image_height: int = None,
    image_width: int = None,
    avg: bool = True,
) -> None:
    """
    Plots and optionally saves three bar charts for the given metrics by segment.
    There will be one chart for false positives, one for false negatives, and one for box loss.

    Args:
        metrics_path (str): Path to the JSON file containing metrics.
        save (bool, optional): If True, saves the plots to the 'pythopix_results' folder. Defaults to False.
        image_height (int, optional): Height of the images in pixels.
        image_width (int, optional): Width of the images in pixels.
        avg(bool) : If set, instead of metrics count avg values will be shown on y axis. Default to True
    """
    false_positives_key = (
        "average_false_positives_count" if avg else "false_positives_count"
    )

    false_negatives_key = (
        "average_false_negatives_count" if avg else "false_negatives_count"
    )

    box_loss_key = "average_box_loss" if avg else "total_box_loss"

    with open(metrics_path, "r") as file:
        metrics_by_segment = json.load(file)

    if image_height is not None and image_width is not None:
        image_area = image_height * image_width
        segments = [
            f"{int(float(seg.split('-')[0]) * image_area)}-{int(float(seg.split('-')[1]) * image_area)}"
            for seg in metrics_by_segment.keys()
        ]
    else:
        segments = [
            f"{float(seg.split('-')[0])*100:.2f}-{float(seg.split('-')[1])*100:.2f}%"
            for seg in metrics_by_segment.keys()
        ]
    false_positives = [
        metrics[false_positives_key] for metrics in metrics_by_segment.values()
    ]
    false_negatives = [
        metrics[false_negatives_key] for metrics in metrics_by_segment.values()
    ]
    box_losses = [metrics[box_loss_key] for metrics in metrics_by_segment.values()]

    if save:
        os.makedirs("pythopix_results", exist_ok=True)

    # Plotting False Positives
    plt.figure(figsize=(10, 6))
    plt.bar(segments, false_positives, color="#56baf0")
    plt.xlabel(
        "Segments"
        + (
            " (area in pixels)"
            if image_height is not None and image_width is not None
            else " (% of original image)"
        )
    )
    plt.ylabel("False Positives")
    plt.title("False Positives by Segment")
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("pythopix_results/false_positives_by_segment.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(segments, false_negatives, color="#a3e38c")
    plt.xlabel(
        "Segments"
        + (
            " (area in pixels)"
            if image_height is not None and image_width is not None
            else " (% of original image)"
        )
    )
    plt.ylabel("False Negatives")
    plt.title("False Negatives by Segment")
    if not avg:
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("pythopix_results/false_negatives_by_segment.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.bar(segments, box_losses, color="#050c26")
    plt.xlabel(
        "Segments"
        + (
            " (area in pixels)"
            if image_height is not None and image_width is not None
            else " (% of original image)"
        )
    )
    plt.ylabel("Box Loss")
    plt.title("Box Loss by Segment")
    plt.xticks(rotation=45)
    plt.tight_layout()
    if save:
        plt.savefig("pythopix_results/box_loss_by_segment.png")
    plt.show()


def plot_multiple_metrics_by_segment(
    metrics_paths: list,
    save: bool = False,
    image_height: int = None,
    image_width: int = None,
    labels: list = None,
    avg: bool = True,
) -> None:
    """
    Plots and optionally saves separate bar charts for false positives, false negatives, and box loss
    from multiple metrics files for each segment, with segments optionally displayed in pixel size.
    Custom labels for the legend can be provided.

    Args:
        metrics_paths (list): Paths to the JSON files containing metrics.
        save (bool, optional): If True, saves the plots to the 'pythopix_results' folder. Defaults to False.
        image_height (int, optional): Height of the images in pixels.
        image_width (int, optional): Width of the images in pixels.
        labels (list, optional): Custom labels for each metrics file in the legend.
        avg(bool) : If set, instead of metrics count avg values will be shown on y axis. Default to True
    """

    false_positives_key = (
        "average_false_positives_count" if avg else "false_positives_count"
    )

    false_negatives_key = (
        "average_false_negatives_count" if avg else "false_negatives_count"
    )

    box_loss_key = "average_box_loss" if avg else "total_box_loss"

    all_metrics = []
    for path in metrics_paths:
        with open(path, "r") as file:
            metrics = json.load(file)
            all_metrics.append(metrics)

    if labels is None or len(labels) != len(metrics_paths):
        labels = [f"Metrics {i+1}" for i in range(len(metrics_paths))]

    if image_height is not None and image_width is not None:
        image_area = image_height * image_width
        segments = [
            f"{int(float(seg.split('-')[0]) * image_area)}-{int(float(seg.split('-')[1]) * image_area)}"
            for seg in all_metrics[0].keys()
        ]
    else:
        segments = [
            f"{float(seg.split('-')[0])*100:.2f}-{float(seg.split('-')[1])*100:.2f}%"
            for seg in all_metrics[0].keys()
        ]

    data_sets = {
        "False Positives/Labels" if avg else "False Positives": [
            [metrics[seg][false_positives_key] for seg in metrics]
            for metrics in all_metrics
        ],
        "False Negatives/Labels" if avg else "False Negatives": [
            [metrics[seg][false_negatives_key] for seg in metrics]
            for metrics in all_metrics
        ],
        "Box Loss/Labels" if avg else "Box Loss": [
            [metrics[seg][box_loss_key] for seg in metrics] for metrics in all_metrics
        ],
    }

    colors = ["#56baf0", "#a3e38c", "#ff6347"]
    n_groups = len(segments)
    bar_width = 0.2
    opacity = 0.8

    for data_label, data_values in data_sets.items():
        fig, ax = plt.subplots(figsize=(10, 6))
        index = np.arange(n_groups)

        for i, (data_set, label) in enumerate(zip(data_values, labels)):
            ax.bar(
                index + i * bar_width,
                data_set,
                bar_width,
                alpha=opacity,
                color=colors[i % len(colors)],
                label=label,
            )

        ax.set_xlabel(
            "Segments"
            + (
                " (pixels)"
                if image_height is not None and image_width is not None
                else " (% of original image)"
            )
        )
        ax.set_ylabel(data_label)
        ax.set_title(f"{data_label} by Segment")
        ax.set_xticks(index + bar_width / 2 * (len(metrics_paths) - 1))
        ax.set_xticklabels(segments)
        ax.legend(loc="upper right")
        if not avg:
            ax.yaxis.set_major_locator(
                MaxNLocator(integer=True if "Loss" not in data_label else False)
            )
        plt.xticks(rotation=45)
        plt.tight_layout()

        if save:
            save_path = f"pythopix_results/{data_label.replace('/', '_').lower()}_by_segment.png"
            if not os.path.exists("pythopix_results"):
                os.makedirs("pythopix_results")
            plt.savefig(save_path)
        plt.show()


def save_segmented_metrics_to_csv(
    metrics_by_segment: Dict[str, Tuple[float, float, float]]
) -> None:
    """
    Saves the metrics by segment data to a CSV file.

    Args:
    metrics_by_segment (Dict[str, Tuple[float, float, float]]): Metrics data segmented by bounding box sizes.
    save (bool, optional): If True, saves the data to a CSV file in the 'pythopix_results' folder. Defaults to False.
    """
    os.makedirs("pythopix_results", exist_ok=True)
    file_path = os.path.join("pythopix_results", "metrics_by_segment.csv")

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Segments", *metrics_by_segment.keys()])

        false_positives = ["False Positives"] + [
            metrics[0] for metrics in metrics_by_segment.values()
        ]
        false_negatives = ["False Negatives"] + [
            metrics[1] for metrics in metrics_by_segment.values()
        ]
        box_loss = ["Box Loss"] + [
            metrics[2] for metrics in metrics_by_segment.values()
        ]

        # Writing data rows
        writer.writerow(false_positives)
        writer.writerow(false_negatives)
        writer.writerow(box_loss)


def visualize_bounding_boxes(
    image_path: str,
    save_fig: bool = False,
    big_labels: bool = False,
    extra_area_percentage: int = 10,
) -> None:
    """
    Displays an image with its bounding boxes as defined in its corresponding YOLO label file,
    optionally with extra area around each box if big_labels is True.
    Can also save the image if save_fig is True.

    Args:
    - image_path (str): Path to the image file.
    - save_fig (bool, optional): If True, saves the image with bounding boxes to a designated folder
                                 instead of displaying it. Defaults to False.
    - big_labels (bool, optional): If True, adds extra area around the bounding boxes. Defaults to False.
    - extra_area_percentage (int, optional): The percentage of the extra area to add around each bounding box. Defaults to 10.

    Returns:
    - None
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image not found at {image_path}")
        return

    height, width, _ = image.shape
    label_path = image_path.replace(".jpg", ".txt").replace(".png", ".txt")

    if not os.path.exists(label_path):
        print(f"No corresponding label file found for {image_path}")
        return

    with open(label_path, "r") as file:
        for line in file:
            class_id, x_center, y_center, bbox_width, bbox_height = [
                float(x) for x in line.split()
            ]

            # Convert to pixel coordinates
            x = int((x_center - bbox_width / 2) * width)
            y = int((y_center - bbox_height / 2) * height)
            w = int(bbox_width * width)
            h = int(bbox_height * height)

            if big_labels:
                extra_w = int(w * extra_area_percentage / 100)
                extra_h = int(h * extra_area_percentage / 100)
                x = max(0, x - extra_w // 2)
                y = max(0, y - extra_h // 2)
                w = min(width, w + extra_w)
                h = min(height, h + extra_h)

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if save_fig:
        output_folder = "pythopix_results/figs"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        base_filename = os.path.splitext(os.path.basename(image_path))[0]
        output_filename = os.path.join(
            output_folder, f"bbox_on_image_{base_filename}.png"
        )
        cv2.imwrite(output_filename, image)
        print(f"Image saved as {output_filename}")
    else:
        cv2.imshow("Image with Bounding Boxes", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def analyze_image_dimensions(input_folder: str, plot: bool = False, save: bool = False):
    """
    Analyzes the dimensions of PNG images in a specified folder.

    Parameters:
    - input_folder (str): The path to the folder containing the PNG images.
    - plot (bool): If True, plots the width and height distribution of the images.

    This function goes through all PNG images in the specified folder, optionally
    plots their width and height distribution if `plot` is True, and prints out the
    average width and height of the images.
    """
    widths = []
    heights = []

    for file in os.listdir(input_folder):
        if file.endswith(".png"):
            img_path = os.path.join(input_folder, file)
            with Image.open(img_path) as img:
                width, height = img.size
                widths.append(width)
                heights.append(height)

    plt.figure(figsize=(12, 6))

    ax1 = plt.subplot(1, 2, 1)
    plt.hist(widths, bins=20, color="skyblue")
    plt.title("Width Distribution")
    plt.xlabel("Width")
    plt.ylabel("Frequency")
    ax1.ticklabel_format(useOffset=False, style="plain")

    ax2 = plt.subplot(1, 2, 2)
    plt.hist(heights, bins=20, color="lightgreen")
    plt.title("Height Distribution")
    plt.xlabel("Height")
    ax2.ticklabel_format(useOffset=False, style="plain")

    plt.tight_layout()

    if save:
        save_path = "pythopix_results/figs"
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        plt.savefig(f"{save_path}/image_dimensions.png")
    if plot:
        plt.show()

    avg_width = np.mean(widths) if widths else 0
    avg_height = np.mean(heights) if heights else 0
    print(f"Average Width: {avg_width:.2f}")
    print(f"Average Height: {avg_height:.2f}")


def bbox_iou(box1, box2, xywh=True, GIoU=False, DIoU=False, CIoU=False, eps=1e-7):
    """
    Calculate Intersection over Union (IoU) of box1(1, 4) to box2(n, 4).

    Args:
        box1 (torch.Tensor): A tensor representing a single bounding box with shape (1, 4).
        box2 (torch.Tensor): A tensor representing n bounding boxes with shape (n, 4).
        xywh (bool, optional): If True, input boxes are in (x, y, w, h) format. If False, input boxes are in
                               (x1, y1, x2, y2) format. Defaults to True.
        GIoU (bool, optional): If True, calculate Generalized IoU. Defaults to False.
        DIoU (bool, optional): If True, calculate Distance IoU. Defaults to False.
        CIoU (bool, optional): If True, calculate Complete IoU. Defaults to False.
        eps (float, optional): A small value to avoid division by zero. Defaults to 1e-7.

    Returns:
        (torch.Tensor): IoU, GIoU, DIoU, or CIoU values depending on the specified flags.
    """

    # Get the coordinates of bounding boxes
    if xywh:  # transform from xywh to xyxy
        (x1, y1, w1, h1), (x2, y2, w2, h2) = box1.chunk(4, -1), box2.chunk(4, -1)
        w1_, h1_, w2_, h2_ = w1 / 2, h1 / 2, w2 / 2, h2 / 2
        b1_x1, b1_x2, b1_y1, b1_y2 = x1 - w1_, x1 + w1_, y1 - h1_, y1 + h1_
        b2_x1, b2_x2, b2_y1, b2_y2 = x2 - w2_, x2 + w2_, y2 - h2_, y2 + h2_
    else:  # x1, y1, x2, y2 = box1
        b1_x1, b1_y1, b1_x2, b1_y2 = box1.chunk(4, -1)
        b2_x1, b2_y1, b2_x2, b2_y2 = box2.chunk(4, -1)
        w1, h1 = b1_x2 - b1_x1, b1_y2 - b1_y1 + eps
        w2, h2 = b2_x2 - b2_x1, b2_y2 - b2_y1 + eps

    # Intersection area
    inter = (b1_x2.minimum(b2_x2) - b1_x1.maximum(b2_x1)).clamp_(0) * (
        b1_y2.minimum(b2_y2) - b1_y1.maximum(b2_y1)
    ).clamp_(0)

    # Union Area
    union = w1 * h1 + w2 * h2 - inter + eps

    # IoU
    iou = inter / union
    if CIoU or DIoU or GIoU:
        cw = b1_x2.maximum(b2_x2) - b1_x1.minimum(
            b2_x1
        )  # convex (smallest enclosing box) width
        ch = b1_y2.maximum(b2_y2) - b1_y1.minimum(b2_y1)  # convex height
        if CIoU or DIoU:  # Distance or Complete IoU https://arxiv.org/abs/1911.08287v1
            c2 = cw**2 + ch**2 + eps  # convex diagonal squared
            rho2 = (
                (b2_x1 + b2_x2 - b1_x1 - b1_x2) ** 2
                + (b2_y1 + b2_y2 - b1_y1 - b1_y2) ** 2
            ) / 4  # center dist ** 2
            if (
                CIoU
            ):  # https://github.com/Zzh-tju/DIoU-SSD-pytorch/blob/master/utils/box/box_utils.py#L47
                v = (4 / math.pi**2) * (
                    torch.atan(w2 / h2) - torch.atan(w1 / h1)
                ).pow(2)
                with torch.no_grad():
                    alpha = v / (v - iou + (1 + eps))
                return iou - (rho2 / c2 + v * alpha)  # CIoU
            return iou - rho2 / c2  # DIoU
        c_area = cw * ch + eps  # convex area
        return (
            iou - (c_area - union) / c_area
        )  # GIoU https://arxiv.org/pdf/1902.09630.pdf
    return iou  # IoU


def show_fg_mask(
    image_path: str,
    label_path: str,
    top_k: int = 13,
    transparent: bool = True,
    grid_size: int = 50,
):
    if not os.path.exists(label_path):
        raise FileNotFoundError(f"The label file {label_path} does not exist.")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The image file {image_path} does not exist.")

    gt_boxes = read_labels(label_path)
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image from {image_path}.")

    img_height, img_width = image.shape[:2]
    converted_labels = []
    for label_data in gt_boxes:
        class_id, label = label_data
        x1, y1, w, h = convert_to_pixels(label, img_width, img_height)
        converted_labels.append((x1, y1, x1 + w, y1 + h))

    gt_boxes_tensor = torch.tensor(converted_labels, dtype=torch.float32)

    anchors = []
    cell_width, cell_height = img_width // grid_size, img_height // grid_size
    for x in range(grid_size):
        for y in range(grid_size):
            center_x, center_y = (
                x * cell_width + cell_width // 2,
                y * cell_height + cell_height // 2,
            )
            anchors.append(
                [
                    center_x - cell_width / 2,
                    center_y - cell_height / 2,
                    center_x + cell_width / 2,
                    center_y + cell_height / 2,
                ]
            )

    anchors_tensor = torch.tensor(anchors, dtype=torch.float32)

    iou_scores = torch.zeros((len(anchors), len(gt_boxes_tensor)))
    for i, anchor in enumerate(anchors_tensor):
        ious = bbox_iou(anchor.unsqueeze(0), gt_boxes_tensor, xywh=False)
        iou_scores[i] = ious

    iou_scores_masked_for_topk = iou_scores.masked_fill(iou_scores == 0, float("-inf"))
    top_k_values, top_k_indices = torch.topk(
        iou_scores_masked_for_topk, top_k, dim=0, largest=True
    )

    for i, anchor in enumerate(anchors):
        pt1 = (int(anchor[0]), int(anchor[1]))
        pt2 = (int(anchor[2]), int(anchor[3]))

        is_top_k_and_non_zero = (iou_scores[i].unsqueeze(0) == top_k_values) & (
            iou_scores[i] > 0
        )

        if transparent:
            if is_top_k_and_non_zero.any():
                max_iou_score = iou_scores[i].max().item()
                iou_score_text = f"{max_iou_score:.2f}"
                text_position = ((pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2)
                cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)
                cv2.putText(
                    image,
                    iou_score_text,
                    text_position,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )
            else:
                cv2.rectangle(image, pt1, pt2, (0, 0, 255), 1)
        else:
            if not is_top_k_and_non_zero.any():
                cv2.rectangle(image, pt1, pt2, (0, 0, 0), cv2.FILLED)

    cv2.imshow("Image with Grid, Anchors, FG Mask, and GT Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
