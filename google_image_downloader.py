from google_images_download import google_images_download   #importing the library
import os

response = google_images_download.googleimagesdownload()   #class instantiation

def getFns(folder_path):
    file_names = []
    onlyfiles = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for i in onlyfiles:
        file_names.append(i)
    return file_names, folder_path

def importText(file_name, encoding="utf8"):
    array = []
    with open(file_name, "r", encoding=encoding) as infile:
        for line in infile:
            array.append(line.strip())
    return array

fns, folder = getFns("videogames/")

for i in range(len(fns)):
    terms = ["sprite sheet"]
    subjects = importText(folder + fns[i])
    for j in range(len(subjects)):
        for n in range(len(terms)):
            input = subjects[j] + " " + terms[n]
            if os.path.exists("downloads/" + input):
                continue
            if len(subjects[j].strip()) <= 1:
                continue
            try:
                arguments = {"keywords":input,"limit":100,"print_urls":True}   #creating list of arguments
                paths = response.download(arguments)   #passing the arguments to the function
                print(paths)   #printing absolute paths of the downloaded images
            except (NotADirectoryError, FileNotFoundError, OSError):
                continue