from shutil import copy2
import glob # Go throw all files in directory
import numpy as np
import pandas as pd
import re

processedDataPath = ''
unprocessedDataPath = ''

def read_line_special(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def parser(line):
    result = re.fullmatch('[\s|\d|\.|\-]+',line)
    if result:
        res = re.search('\d',result.string) # костыль
        if res:
            return result.string
        else:
            return None
    else:
        return None

def writeCSV(path):
    auxiliary_file = processedDataPath + path[4:-5] + '.csv'
    help_file = open(auxiliary_file,'w') # костыль - не могу сразу передавать в DataFrame str. Использовать split и int?
    help_file.write('Step PotEng KinEng TotEng Temp Press Density c_2[4] c_3[4]\n')
    with open(path,'r') as file:
        for line in read_line_special(file):
            line = parser(line)
            if line:
                line = re.sub('\s+',' ',line) # ? костыль
                line = line[1:-2] + '\n' # костыль
                help_file.write(line)
    help_file.close()

def main():

    for logFile in glob.glob(unprocessedDataPath + 'log.*'):
        writeCSV(logFile)

    if unprocessedDataPath != processedDataPath:
        for rdfFile in glob.glob(unprocessedDataPath + '*.rdf'):
            newRdfPath = processedDataPath + rdfFile[len(unprocessedDataPath):]
            copy2(rdfFile, newRdfPath)

if __name__ == "__main__":
    main()