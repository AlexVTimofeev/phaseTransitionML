import glob # Go throw all files in directory
import re
import pandas as pd

import parametrs

startCount = 255

"""
В качестве features мы используем среднее значение энергий и их стандартное отклонение (6 фич) и отношения max/min из rdf
"""



def main():
    rows = ['c{}'.format(i) for i in range(13)] # 11, если добавлять положение равновесия
    df = pd.DataFrame(columns=rows)
    
    for logFile, rdfFile in zip(
        glob.glob(parametrs.processedDataPath + 'log.*temp*.csv'),
        glob.glob(parametrs.processedDataPath + '*.rdf')): 
        # Берем температуру и давление из названия файлов
        temp = re.search(r'.*emp(.+)\.press',rdfFile).group(1)
        press = re.search(r'press(.+)\.rdf',rdfFile).group(1)

        df_t = pd.read_csv(logFile,delimiter=' ',index_col='Step')
        df_rfd = pd.read_table(rdfFile,skiprows=[0,1,2,3,4], delimiter=' ',names=['Row','c_1[1]','c_1[2]','c_1[3]'],index_col='Row')

        # df_rfd = df_rfd.loc[df_rfd['c_1[2]'] != 0.000000]
        df_rfd = df_rfd['c_1[2]']

        data = [temp,press]
        # data += [df_rfd.max()/df_rfd.min()]
        data += [
            df_rfd.max()/df_rfd[df_rfd.argmax():].min(),
            df_rfd.max(),
            df_rfd.argmax(),
            df_rfd[df_rfd.argmax():].min(),
            df_rfd[df_rfd.argmax():].argmin()
            ]
       
        for energy in ['PotEng','KinEng','TotEng']:
            data += [df_t[energy][startCount:].mean(),df_t[energy][startCount:].std()]

        # data += [df_t['c_2[4]'].max(),df_t['c_3[4]'].max()] # add it


        df.loc[len(df)] = data
    
    df.to_csv(parametrs.outpitFile)


if __name__ == "__main__":
    main()