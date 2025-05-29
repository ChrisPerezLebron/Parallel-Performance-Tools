import hatchet as ht
import sys

X = int(sys.argv[1])

gf = ht.GraphFrame.from_caliper("lushesh-64core.json")

gf = gf.load_imbalance(metric_column="time", verbose=True)

df = gf.dataframe

df = df.sort_values(by=['time.imbalance'], ascending=False)

# print(df)
# print(df.columns)

#TODO: check piazza to see if 1st from top means index [1] 
    #Piazza @198 no first from top is 0th index 
row = df.iloc[X-1] 
# print(row)d'
print(row['time.ranks'])