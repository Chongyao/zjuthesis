#!/usr/bin/env python3
import os
import sys
from PIL import Image, ImageChops

TARGET_DIR = "intermediate_renders_coolwarm"


def trim(im):
    im = im.convert("RGBA")

    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox:
        im = im.crop(bbox)

    datas = im.getdata()
    new_data = []
    for item in datas:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    im.putdata(new_data)
    return im


def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory not found: {TARGET_DIR}")
        sys.exit(1)

    count = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.lower().endswith(".png"):
                full_path = os.path.join(root, file)
                try:
                    img = Image.open(full_path)
                    trimmed_img = trim(img)

                    # Overwrite original
                    trimmed_img.save(full_path)
                    print(
                        f"Trimmed: {full_path} | Size: {img.size} -> {trimmed_img.size}"
                    )
                    count += 1
                except Exception as e:
                    print(f"Error processing {full_path}: {e}")

    print(f"\nFinished trimming {count} images.")


if __name__ == "__main__":
    main()
