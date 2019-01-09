import os

import parametrs

import dataPreProcessing
import dataProcessing
import dataCreator

def main():

    dataCreator.main()
    dataPreProcessing.main()
    dataProcessing.main()


if __name__ == '__main__':
    main()