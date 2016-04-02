AA = pd.DataFrame(d)
ColumnNames = list(AA.columns)
print(ColumnNames)
for Column in range(0,len(ColumnNames)):
for ValueInColumn in AA.ix[:,Column].values:
print(ValueInColumn)
