import pandas as pd

fields = ["Symbol", "Exchange"]
df = pd.read_csv("nosctr.csv", skipinitialspace=True, usecols=fields)

#print(df.head()) # print first 5 rows
#print(df.Symbol)
#print(df.Exchange)

# Row Offset -2
# offset by -2 from csv row number
#print(df.Symbol[97] + ":" + df.Exchange[97])
# so the range is:  0 to row_count - 2

row_count = len(df.axes[0])
#print(df.Symbol[0])


# if exchange is NASD, output NASDAQ
def normalize(str):
    if str == "NASD":
        return "NASDAQ"
    else:
        return str

result = ""
for i in range(0, row_count-1): # up to but not including , so -1 already
    if i != row_count-2:
        result += normalize(df.Exchange[i]) + ":" + str(df.Symbol[i]) + ","
    elif i == row_count-2:
        result += normalize(df.Exchange[i]) + ":" + str(df.Symbol[i])


file = open("nosctr2 27 jan 2021", "w")
file.write(result)
file.close()



