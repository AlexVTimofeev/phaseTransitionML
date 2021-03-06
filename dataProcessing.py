import glob # Go throw all files in directory
import re
import pandas as pd

import parametrs

startCount = 255

def main():
    rows = ['c{}'.format(i) for i in range(65)]
    df = pd.DataFrame(columns=rows)
    
    for logFile, rdfFile in zip(
        glob.glob(parametrs.processedDataPath + 'log.*temp*.csv'),
        glob.glob(parametrs.processedDataPath + '*.rdf')): 
        # Берем температуру и давление из названия файлов
        temp = re.search(r'.*emp(.+)\.press',rdfFile).group(1)
        press = re.search(r'press(.+)\.rdf',rdfFile).group(1)

        df_t = pd.read_csv(logFile,delimiter=' ',index_col='Step')
        df_t = df_t.drop(columns=['Temp','Press'])
        df_rfd = pd.read_table(rdfFile,skiprows=[0,1,2,3,4], delimiter=' ',names=['Row','c_1[1]','c_1[2]','c_1[3]'],index_col='Row')
        # ???

        df_t = df_t[startCount:].describe()
        df_rfd = df_rfd.describe()

        data = [temp,press]
        for i in range(1,8):
            data += list(df_t.iloc[i])   
        for i in range(1,8):
            data += list(df_rfd.iloc[i])
        df.loc[len(df)] = data
    
    df.to_csv(parametrs.outpitFile)

if __name__ == "__main__":
    main()