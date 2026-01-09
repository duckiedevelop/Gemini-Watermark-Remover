import sys
import os
import cv2
import numpy as np

if len(sys.argv) < 2:
    print("Drag and drop a file onto the script.")
    input()
    sys.exit()

f_path = sys.argv[1]
print(f"Fixing: {f_path}")

img = cv2.imread(f_path)
if img is None:
    sys.exit("Bad file")

h, w = img.shape[:2]

# Config
if w > 1024 and h > 1024:
    mask, sz, pad = "96.png", 96, 64
else:
    mask, sz, pad = "48.png", 48, 32

if not os.path.exists(mask):
    sys.exit(f"Missing {mask}")

# Get alpha
bg = cv2.imread(mask)
a_map = np.max(bg, axis=2) / 255.0

# Coords
y, x = h - pad, w - pad
y_start, x_start = y - sz, x - sz

# Crop and math
crop = img[y_start:y, x_start:x].astype(float)
a_map = np.clip(a_map, 0, 0.999) # prevent div/0

# (Pixel - Alpha*255) / (1-Alpha)
norm = 1.0 - a_map
res = np.zeros_like(crop)

for i in range(3):
    res[:,:,i] = (crop[:,:,i] - (a_map * 255.0)) / norm

# Save
img[y_start:y, x_start:x] = np.clip(res, 0, 255)
out = f_path.replace(".png", "_clean.png").replace(".jpg", "_clean.jpg")
cv2.imwrite(out, img)

print("Done.")