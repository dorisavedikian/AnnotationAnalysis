
import csv
import string
import pandas as pd

df = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Annotation_Analysis/ToAssign.csv")
df['WhiteTerm'] = df['WhiteTerms.english'].str.split(';')
df['StopTerm'] = df['StopTerms.english'].str.split(';')
df_new = df.explode('WhiteTerm')[['WhiteTerm', 'PrefLabel']].reset_index(drop=True).copy()
df_new1 = df.explode('StopTerm')[['StopTerm', 'PrefLabel']].reset_index(drop=True).copy()
df_new['PrefLabel'] = df_new['PrefLabel'].astype(str) + ', To Assign'
df_new1['PrefLabel'] = df_new1['PrefLabel'].astype(str) + ', To Assign'
df2 = df_new1.dropna(axis=0, subset=['StopTerm'])

df3 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Annotation_Analysis/ToReplace.csv")
df3['WhiteTerm'] = df3['WhiteTerms.english'].str.split(';')
df3['StopTerm'] = df3['StopTerms.english'].str.split(';')
df3_new = df3.explode('WhiteTerm')[['WhiteTerm','PrefLabel']].reset_index(drop=True).copy()
df3_new1 = df3.explode('StopTerm')[['StopTerm', 'PrefLabel']].reset_index(drop=True).copy()
df3_new['PrefLabel'] = df3_new['PrefLabel'].astype(str) + ', To Replace'
df3_new1['PrefLabel'] = df3_new1['PrefLabel'].astype(str) + ', To Replace'
df4 = df3_new1.dropna(axis=0, subset=['StopTerm'])

writer = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Annotation_Analysis/ToAssign&ToReplace_Adjusted.xlsx', engine = 'xlsxwriter')
df_new.to_excel(writer, sheet_name='WhiteTerm_ToAssign', index=False)
df2.to_excel(writer, sheet_name='StopTerm_ToAssign', index=False) 
df3_new.to_excel(writer, sheet_name='WhiteTerm_ToReplace', index=False)
df4.to_excel(writer, sheet_name='StopTerm_ToReplace', index=False) 
writer.close()

