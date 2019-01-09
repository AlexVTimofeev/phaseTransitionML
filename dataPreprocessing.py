from shutil import copy2
import glob # Go throw all files in directory
import numpy as np
import pandas as pd
import re

import parametrs 

#processedDataPath = 'processedData/'
#unprocessedDataPath = 'data/'

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
    auxiliary_file = parametrs.processedDataPath + path[4:-5] + '.csv'
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

    for logFile in glob.glob(parametrs.unprocessedDataPath + 'log.*'):
        writeCSV(logFile)

    if parametrs.unprocessedDataPath != parametrs.processedDataPath:
        for rdfFile in glob.glob(parametrs.unprocessedDataPath + '*.rdf'):
            newRdfPath = parametrs.processedDataPath + rdfFile[len(parametrs.unprocessedDataPath):]
            copy2(rdfFile, newRdfPath)

if __name__ == "__main__":
    main()