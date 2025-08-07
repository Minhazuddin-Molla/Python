import numpy as np
import pandas as pd
dict={"Name":["Minhaz","Misba","Swapnil","Abhirup"],"Roll No.":[19,18,36,2],"Marks":[99,96,99,100]}
d=pd.DataFrame(dict) #displays a 2-D array in spreadsheet form
d.to_csv("Friends.csv")
d.to_csv("Friends_no_index",index=False)
d.head(2)
d.tail(2)
d.describe()
