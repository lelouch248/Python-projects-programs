import numpy as np
import cv2

img = np.zeros((800, 800, 3))
# img[y coordinates,x coordinates]
for y in range(0, 710, 100):
    if (y // 100) % 2 == 0:
        count = 0
    else:
        count = 1
    for x in range(0, 710, 100):
        if (x // 100) % 2 == 0 and count == 0:
            img[x:x + 100, y:y + 100] = 255, 255, 255

        if (x // 100) % 2 == 1 and count == 1:
            img[x:x + 100, y:y + 100] = 255, 255, 255

cv2.imshow('checker board', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
