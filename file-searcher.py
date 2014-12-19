#-------------------------------------------------------------------------------
# Name:        File Searcher
# Purpose:     This program takes the folder path & a word to
#              be searched as input and outputs all the file names in that
#              folder where that word is found.
# Author:      ABHISHEK CHAKRAVARTY
#
# Created:     19-12-2014
#-------------------------------------------------------------------------------
from os import listdir
from os.path import isfile, join

def get_filder():
    folder = raw_input("enter full folder path: ")
    print folder
    return folder

def get_files(folder):
    files = [f for f in listdir(folder) if isfile(join(folder,f))]
    return files

def list_files(files):
    word = raw_input("enter word to be searched: ")
    result = []
    flag = 0 #use this to stop iterating a file at the point the word is found
    for f in files:
        opened_file = open(f)
        while True and flag == 0:
            line = opened_file.readline()
            if len(line) == 0:
                break
            else:
                line = line.split()
                for w in line:
                    if w == word:
                        result.append(f)
                        flag = 1
                        break
        flag = 0 #make this 0 again for the next file.
    return result

if __name__ == '__main__':
    folder = get_filder()
    files = []
    files = get_files(folder)
    result = list_files(files)
    total = len(result)
    print 'total '+str(total)+' file(s) have been found.'
    for r in result:
        print r

