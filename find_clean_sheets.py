
import numpy as np

# Sample image edges to quickly detect background colour
def detectSimpleBackgroundFast(img):
    all_colours = []
    top_colours = []
    for i in range(len(img[0])):
        top_colours.append(img[0][i])

    bottom_colours = []
    for i in range(len(img[len(img) - 1])):
        bottom_colours.append(img[len(img) - 1][i])

    left_colours = []
    for i in range(len(img)):
        left_colours.append(img[i][0])

    right_colours = []
    for i in range(len(img)):
        right_colours.append(img[i][len(img[i]) - 1])

    all_colours.extend(top_colours)
    all_colours.extend(bottom_colours)
    all_colours.extend(left_colours)
    all_colours.extend(right_colours)

    all_colours, counts = np.unique(np.asarray(all_colours), return_counts = True)

    top_count = 0
    top_id = 0
    for i in range(len(counts)):
        if top_count > counts[i]:
            top_id = i
            top_count = counts[i]

    if top_count > (np.sum(counts) / 2):
        return True


