import os

from animeSexAnalyzer import sex_rating
from os import listdir
from os.path import isfile, join
import shutil

from datetime import datetime

import json

_DEFAULT_FILE_EXTENSION = '.png'


def sortImages(mypath:str):
    onlyfiles = find_all_matching_files_in_given_folder(mypath, _DEFAULT_FILE_EXTENSION)
    for element in onlyfiles:
        rating = sex_rating(join(mypath, element))
        folder_name = rating[0]
        if not os.path.exists(join(mypath, folder_name)):
           os.makedirs(join(mypath, folder_name))
        shutil.move(join(mypath, element), join(mypath, folder_name, element))
        print(rating[0][0].upper() + " - " + element)
        
        

def find_all_matching_files_in_given_folder(directory, file_extension):
    only_files = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith(file_extension)]
    return only_files
