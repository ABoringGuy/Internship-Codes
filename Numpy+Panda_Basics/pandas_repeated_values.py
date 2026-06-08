import pandas as pd

data={
    "A":pd.Series([1, 2, 2, 3, 3, 4]),
    "B":pd.Series([5, 6, 6, 7, 8, 8])
    }

df=pd.DataFrame(data)
print("Original Data:\n",df)
print("\n Duplicated Data are: \n", df[df.duplicated()].to_string())

