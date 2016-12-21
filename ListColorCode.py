from PIL import Image
import numpy as np

image = Image.open("256_colors_bg.png")
ans = {}
count = 0
for y in range(8, 436, 17):
    for x in range(40, 630, 64):
        ans[image.getpixel((x, y))] = count
        count += 1

print(len(ans))
print("[")
for key, value in sorted(ans.items()):
    print("%3d : [%3d %3d %3d]" % (value, key[0], key[1], key[2]))
print("]")
