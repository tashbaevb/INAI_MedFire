import pandas as pd
import os

def convert_to_yolo(csv_path, output_dir, images_dir):
    data = pd.read_csv(csv_path)

    for index, row in data.iterrows():
        filename = row["filename"]
        width, height = row["width"], row["height"]
        xmin, ymin, xmax, ymax = row["xmin"], row["ymin"], row["xmax"], row["ymax"]

        x_center = ((xmin + xmax) / 2) / width
        y_center = ((ymin + ymax) / 2) / height
        bbox_width = (xmax - xmin) / width
        bbox_height = (ymax - ymin) / height

        label_path = os.path.join(output_dir, filename.replace('.jpg', '.txt'))
        with open(label_path, 'w') as f:
            f.write(f"0 {x_center} {y_center} {bbox_width} {bbox_height}\n")


if __name__ == "__main__":
    base_dir = "datasets/Wildfire-Smoke/"
    subsets = ["train", "valid", "test"]

    for subset in subsets:
        csv_path = os.path.join(base_dir, subset, "_annotations.csv")
        output_dir = os.path.join(base_dir, subset)
        images_dir = os.path.join(base_dir, subset)

        convert_to_yolo(csv_path, output_dir, images_dir)
        print(f"Конвертация завершена для {subset}")
