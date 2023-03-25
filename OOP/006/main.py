import requests
from JsonPlaceHolder_class import JsonPlaceHolder
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/posts/")
dataframe = pd.DataFrame(response.json())

idx_count = 0
param_list = []
obj_list = []

for row_idx in range(0, len(dataframe)):
    curr_row = dataframe.iloc[row_idx]
    for idx in curr_row.index:
        element = curr_row.loc[((curr_row.index)[idx_count])]
        param_list.append(element)
        idx_count+=1
    
    obj_list.append(JsonPlaceHolder(param_list[0], param_list[1], param_list[2], param_list[3]))
    param_list.clear()
    idx_count = 0

for obj in obj_list:
    obj.show()