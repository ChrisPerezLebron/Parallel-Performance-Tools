import hatchet as ht
import sys
# print("we did hatchet")

#TODO: N set dynamically from first command arg
n = int(sys.argv[1])

gf = ht.GraphFrame.from_caliper("lushesh-1core.json")
# print(gf.dataframe)
# print(gf.dataframe.columns)
df = gf.dataframe[["name", "time"]]
df = df.sort_values(by=['time'], ascending=False)

for index, row in df.iterrows():
    # print(row['type'])
    print(f"{row['name']} {row['time']}") 
    n -= 1
    if n == 0: 
        break 


# print(df)
# print(df.columns)

