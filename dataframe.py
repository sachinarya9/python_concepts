import pandas as pd

d = {'a':['Sachin','Vaibhav'], 'b':['Abhishek','Shubham']}
# d = ['Sachin','Arya']
data_frame = pd.DataFrame(d, index = ['one','two'])
print(data_frame)