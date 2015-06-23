from __future__ import print_function
import os, sys
from PIL import Image
import time

band_size = 30

if not len(sys.argv) > 3:
    raise SystemExit("Usage: %s src1 [src2] .. dest" % sys.argv[0])

images = map(Image.open, sys.argv[1:-1])
mh = min(i.size[1] for i in images)
w = 0
out_images = []

for img in images:
    if img.size[1] > mh:
        rat = float(img.size[0]) / float(img.size[1]) 
        out = img.resize((int(mh * rat), mh))
    else:
        out = img
    w += out.size[0]
    out_images.append(out)

w += (len(images) -1) * band_size

result = Image.new("RGBA", (w, mh))

x = 0
for i in out_images:
    result.paste(i, (x, 0))
    x += i.size[0] + band_size 

result.save(sys.argv[-1])

print("SUCCESS !!!!")
print(str(sys.argv[1:-1]) + " are merged in " + sys.argv[-1])