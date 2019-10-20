import pandas as pd
dict = {'Name' : ['Sachin','Sumit','Satyam','Akshay','Prit','Vaibhav']}
brics = pd.DataFrame(dict)
brics.index = ['GE','RE','SE','ME','PE','KE']
csv_dataframe = pd.read_csv('C:\Users\arya\Desktop\\Python_excel_sheets\\dataframe_sheet.xlsx')
print(csv_dataframe)
# print(brics)