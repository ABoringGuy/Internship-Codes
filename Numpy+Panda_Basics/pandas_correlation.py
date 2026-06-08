import pandas as pd

data=pd.read_csv("data.csv")
print(data.corr())

"""In this code snippet, we find correlation between datas inside data.csv
Value of 1=If Data A is increased so is Data B
High +ve value= If Data A is increases then it is likely chance to increase Data B
Low +ve value= If Data A is increases then it is unlikely chance to increase Data B
High -ve value= If Data A is decreases then it is likely chance to decrease Data B
Low -ve value= If Data A is decreases then it is unlikely chance to decrease Data B"""