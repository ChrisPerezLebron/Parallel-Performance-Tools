import hatchet as ht
import sys
# print("we did hatchet")

n = int(sys.argv[1])

gf8 = ht.GraphFrame.from_caliper("lushesh-8core.json")
gf64 = ht.GraphFrame.from_caliper("lushesh-64core.json")

gf8.drop_index_levels() 
gf64.drop_index_levels() 

gfDiff = gf64 - gf8
df = gfDiff.dataframe[['name', 'time']]
df = df.sort_values(by=['time'], ascending=False)
# print(df)
# print(df.columns)

for index, row in df.iterrows():
    # print(row['type'])
    print(f"{row['name']} {row['time']}") 
    n -= 1
    if n == 0: 
        break 