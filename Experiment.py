import pandas as pd
import random
d = {
'First' : random.sample(range(1, 10000000), 8),'Second' : random.sample(range(-10000000, -1), 8),"Text" :
[
'The dfgAlteryx','Analytics',
'Achieving your financial goals is no easy task. It is complicated and takes time. How successful you are will depend on the choices you make, today and If prompted for the company name, enter  to register. Cont or  with questions Lastttttttttttt','Awards recognize','the','outstanding','achievements','of'
]


}

AA = pd.DataFrame(d)
ColumnNames = list(AA.columns)
print(ColumnNames)
for Column in range(0,len(ColumnNames)):
	for ValueInColumn in AA.ix[:,Column].values:
		print(ValueInColumn)
