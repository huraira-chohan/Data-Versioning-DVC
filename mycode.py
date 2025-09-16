import pandas as pd
import os

data = {"Name":['Huraira','Arshad','Ali'],
        "Age":[19,18,17],
        "City":["Isl","Lhr","Krachi"]}


df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path  =  os.path.join(data_dir,'Sample Csv File')

df.to_csv(file_path,index=False)

print(f'Your file has been saved to {file_path}')