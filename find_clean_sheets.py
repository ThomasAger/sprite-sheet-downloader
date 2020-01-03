import os
import numpy as np
import cv2
from google_image_downloader import getFns

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

    all_colours, counts = np.unique(np.asarray(all_colours), return_counts = True, axis=0)

    top_count = 0
    top_id = 0
    for i in range(len(counts)):
        if counts[i] > top_count  :
            top_id = i
            top_count = counts[i]

    if top_count > (np.sum(counts) / 2):
        return True


#img = cv2.imread("downloads/sonic sprite sheet/2.10831.png")
#print(detectSimpleBackgroundFast(img))
#exit()
def getFolders(folder_path):
    file_names = []
    onlyfiles = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) is False]
    for i in onlyfiles:
        file_names.append(i)
    return file_names, folder_path


if __name__ == '__main__':

    all_folders, output_folder = getFolders("downloads/")

    for i in range(len(all_folders)):
        if os.path.exists("cleaned/" + all_folders[i]) is False:
            all_fns, fn_folder = getFns(output_folder + all_folders[i])
            for j in range(len(all_fns)):
                img = cv2.imread(output_folder + all_folders[i] + "/" + all_fns[j])

                if img is None:
                    print(output_folder + all_folders[i] + "/" + all_fns[j])
                    continue
                if detectSimpleBackgroundFast(img):
                    try:
                        if os.path.exists("cleaned/" + all_folders[i]) is False:
                            os.mkdir("cleaned/" + all_folders[i])
                        cv2.imwrite("cleaned/" + all_folders[i] + "/" + all_fns[j], img)
                    except:
                        print("cleaned/" + all_fns[j])
