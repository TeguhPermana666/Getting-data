import pandas as pd
"""
Proses import dan ekspor dapat dilakukan dengan cepat dan mudah dapat membuat sebuah data dengan berbagai macam eksitensi 
"""
# data_nilai=({"Teguh":[80,90,90,98],"Komang":[90,78,100,93],"Putu":[87,79,79,100]})
# df=pd.DataFrame.from_dict(data_nilai,orient="index",columns=["Matematika","Bahasa Indonesia","Minat","Bahasa Inggris"])

#ekspor ke dalam bentuk file csv
#df.to_csv("D:/TeguhPermana_data/Data_Grouping/Ujian Hidup dan Mati.csv")

#import data
importt_data=pd.read_csv("D:/TeguhPermana_data/Data_Grouping/Ujian Hidup dan Mati.csv")
print(importt_data)