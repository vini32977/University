import pandas as pd
df1=pd.DataFrame({'Name':['Snigdha','Smayan','Satvik'],
                  'age':[20,19,18],
                  'grade':['A','C','A']},
                  index=[1,2,3])
df2=pd.DataFrame({'Name':['Mary','Nirmala','Shantala'],
                  'age':[23,39,28],
                  'grade':['B','C','A']},
                  index=[4,5,6])
result=pd.concat([df1,df2])
print(result)