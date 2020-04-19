import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_histogram(image):
    result = np.zeros(256)
    for row in image:
        for col in row:
            result[col] += 1
    return result

def get_colors(histogram, n = 6):
    l = list(enumerate(histogram))
    l.sort(key = lambda t: t[1], reverse = True)
    l = l[: n + 1]
    l = list(map(lambda t: t[0], l))
    l.sort()
    return l

def closest_color(color, colors):
    for c in colors:
        if color < c:
            return c
    return colors[-1]

def apply_colors(image, colors):
    row, col = image.shape
    for i in range(row):
        for j in range(col):
            image[i][j] = closest_color(image[i][j], colors)
    return image

if __name__ == '__main__':
   image = cv2.imread('./lena.jpg', cv2.IMREAD_GRAYSCALE)
   histogram = get_histogram(image)
   colors = get_colors(histogram, 3)
   compressed = apply_colors(image, colors)
   cv2.imwrite('lena_compressed.jpg', image)
   plt.imshow(compressed, cmap = 'gray')
   plt.show()
