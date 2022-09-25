import sys
import pandas as pd
def extract_rows(path, number,outpath):
    try:
        data=read_csv(path)
        output = data[:number]
        output.to_csv(outpath,index=False)
        print("extraction successful")
    except:
        print(f"The file does not have {number} entries, returning entire file.")
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path, sep=",", encoding='utf-8')
        return data
    except Exception:
        print("Something went wrong when trying to open the csv file!")
        sys.exit(2)
def sort(df_path,column):
    df = read_csv(df_path)
    df2=df.sort_values(by=column)
    df2.to_csv(df_path.replace(".csv",f"_{column}_sort.csv"),index=False)

