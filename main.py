import os

import parametrs

import dataPreProcessing
import dataProcessing
import dataCreator

def main():

    dataCreator.main() # Поменять папку сохранения файлов
    dataPreProcessing.main()
    dataProcessing.main()


if __name__ == '__main__':
    main()