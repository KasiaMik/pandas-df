import pandas as pd

df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
		  columns = ["Col_A", "Col_B"])

sort_list = ["C", "D", "B", "A"]

sorterIndex = dict(zip(sort_list, range(len(sort_list))))

df['Rank'] = df['Col_A'].map(sorterIndex)

df.sort_values('Rank', inplace = True)
df.drop('Rank', 1, inplace = True)
df.reset_index(inplace = True)
df.drop('index', 1, inplace = True)

# EXCERCISE 2

new_column = ["P", "Q", "R", "S"]
insert_position = 1

df.insert(insert_position, "Col_C", new_column)

print(df.head())

"""
      col_A   col_B
0	C	3
1	D	4
2	B	2
3	A	1
"""