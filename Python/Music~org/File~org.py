
"""
Title:     File ~ Org
Date:    Friday 1st May 2020
By:       Callum Clegg

Desc:    File~org - .py script that arranges music files (e.g. '.mp3')
            based from the files metadata. More specifically, their 'genre'
            tag.
"""

import os
import shutil
from tinytag import TinyTag, TinyTagException
import pathlib
from pathlib import Path

tracks = []
genres = []

#----------------------------------START----------------------------------

dump = Path(str(Path.cwd()))
home = Path.home()
music = Path().joinpath(Path.home(), 'Music')
downloads = Path().joinpath(Path.home(), 'Downloads')

abs_path = str(dump)

def main():

    retrieve()
    invalid = []
    for root, dirs, files, in os.walk(dump):
        for genre_name in dirs:
            genres.append(genre_name)
        for name in files:
            if name.endswith((".mp3", ".wav", "m4a")):
                tracks.append(name)
            else:
                invalid.append(1)
                
    directory_check(downloads)
    directory_check(Path().joinpath(home, dump))
    directory_check(music)
                
    print(str(len(invalid)) + " files not recognised")
    res = False
    while not res:
        res = True
        ans = input("Do you folders to be pedantic? (y/n)")

        if ans == 'n':
            
            org()
            request = input("Key genres to merge? (write in form genre 1, genre 2,...) ").split(",")
            
            for req in request:
                striped = req.strip()
                
                if striped in genres:
                    rm_pedantic(striped)
                    
                else:
                    print(req + " not found")
                    res = False
    
            redundant()
        
        if ans == 'y':
            res = True
            pedantic()
            org()
            break
        
        else:
            res = False
        
    print("Complete!")
    
# Checks if directory is valid 
def directory_check(folder):
    folder_path = Path(home).joinpath(folder)
    folder_check = folder_path.is_dir()
    if folder_check is True:
        print(str(folder_path) + " is a valid directory")
        return True
    else:
        print(str(folder_path) + " is NOT a valid directory")
        return False
    

# retrieves music files from downloads 
def retrieve():
    for root, dirs, files, in os.walk(downloads):
        for name in files:
            if name.endswith((".mp3", ".m4a", ".wav")):
                Path(str(downloads) + '\\' + name).replace(abs_path +'\\'+ name)
                print(name)


# organise files into representing folders (i.e. by genre) 
def org():

    for track in tracks:
        file = abs_path + '\\' + track
        try:
            temp = TinyTag.get(file)
        except:
            print("No files found in main dir.")
            break
            
        if temp.genre == "" or temp.genre == None or temp.genre == "Other":
            Path.mkdir(Path(abs_path +'\\Misc'), exist_ok=True)
            Path(file).replace(abs_path + '\Misc\\' + track)
            print("Misc folder has been updated.")
            continue
        if temp.genre in genres:
            Path(file).replace(abs_path + '\\' + temp.genre + '\\' + track)
            continue
        if temp.genre.find('/'):
            new = temp.genre.replace('/', '&')
            Path.mkdir(Path(abs_path +'\\'+ new), exist_ok=True)
            Path(file).replace(abs_path +'\\' + new + '\\' + track)
            continue
        else:  
            Path.mkdir(Path(abs_path +'\\'+ temp.genre), exist_ok=True)
            Path(file).replace(abs_path +'\\' + temp.genre + '\\' + track)
            

# Creates folder based on user input and moves file to correct genre dir 
def rm_pedantic(concatenate):
    for root, dirs, files, in os.walk(dump):
        for dir in dirs:
            
            if os.path.exists(abs_path + '\\' + concatenate) == False:
                print(concatenate + " folder does not exist.")
                break
            
            for track in tracks:

                temp = abs_path + '\\' + dir + '\\' + track
                if concatenate in dir:
                    if os.path.isfile(temp):
                        Path(temp).replace(abs_path + '\\' + concatenate + '\\' + track)

# Seperates generalising folders 
def pedantic():
    for root, dirs, files, in os.walk(dump):
        for dir in dirs:
            for track in tracks:
                
                temp = abs_path + '\\' + dir + '\\' + track
                
                if os.path.isfile(temp):
                    
                    valid = TinyTag.get(abs_path + '\\' + dir + '\\' + track)
                    if valid.genre != dir:
                        
                        if valid.genre == "" or valid.genre == None or valid.genre == "Other":
                            Path.mkdir(Path(abs_path +'\\Misc'), exist_ok=True)
                            Path(temp).replace(abs_path + '\Misc\\' + track)
                            continue
                    
                        if valid.genre is genres:
                            Path(temp).replace(abs_path + '\\' + valid.genre + '\\' + track)
                            continue
                        
                        if valid.genre.find('/'):
                            new = valid.genre.replace('/', '&')
                            Path.mkdir(Path(abs_path +'\\'+ new), exist_ok=True)
                            Path(temp).replace(abs_path +'\\' + new + '\\' + track)
                            continue
                        
                        else:
                            Path.mkdir(Path(abs_path +'\\'+ vSalid.genre), exist_ok=True)
                            Path(valid).replace(abs_path +'\\' + valid.genre + '\\' + track)
                            
    print("pedantic folders generated.")

def redundant():
    for root, dirs, files, in os.walk(dump):
        for dir in dirs:
            if not os.listdir(dir):
                Path(dir).rmdir()
                print(dir + " folder removed.")

if __name__ == "__main__":
    main()
#-----------------------------------END-----------------------------------

