import pandas as pd

"""Here if we used:
data= {
    "A" :[18, 19, None, 30, 23, 45],
    "B" :[None, 12, 15, 53],
    "C" :[124, 12, 15, None, 53, 52]
}
Then we get array size mismatch error. Using Series automatically fills missing values with None when making df

"""
data= {
    "A" :pd.Series([18, 19, None, 30, 23, 45]),
    "B" :pd.Series([None, 12, 15, 53]),
    "C" :pd.Series([124, 12, 15, None, 53, 52])
}

df= pd.DataFrame(data)
print("Data Frame with Missing Values \n",df)

df_cleaned=df.dropna()
print("\nData Frame that shows Rows with No missing Values Only\n",df_cleaned)

"""We can fill missing values with any string/number based on parameter content below"""
df_fill_with_zero=df.fillna(0)
print("\nData Frame that fills missing values with Zero\n",df_fill_with_zero)

df_filled_with_mean=df.fillna(df.mean())
print("\nData Frame that fills missing values with mean\n",df_filled_with_mean)