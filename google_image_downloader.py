from google_images_download import google_images_download   #importing the library
import input_output as inp

response = google_images_download.googleimagesdownload()   #class instantiation


terms = "sprite sheet"
subjects = inp.import1dArray("data/wikipedia/snes_clean.txt")

arguments = {"keywords":"mario sprite sheet,zelda sprite sheet,sonic sprite sheet,final fantasy sprite sheet, metal slug sprite sheet,yoshi sprite sheet,kirby sprite sheet,chrono trigger sprite sheet, donkey kong country sprite sheet, secret of mana sprite sheet, earthbound sprite sheet, street fighter sprite sheet, castlevania sprite sheet,F-zero sprite sheet, contra sprite sheet, super ghouls n ghosts sprite sheet, teenage mutant ninja turtles sprite sheet","limit":100,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images