import pandas as pd
import re

## Why pandas?
# print("There's flexibility with using Python\nHelps with working with larger datasets\n")

## Loading the data into pandas
# df1=pd.read_csv('pokemon_data.csv') #df is dataframe
# print(df1)
# df2=pd.read_excel('pokemon_data.xlsx')
# print(df2)
# df3=pd.read_csv('pokemon_data.txt', delimiter='\t') #as it would have multiple tab spaces when being read as csv, we remove those by using delimiter
# print(df3)
# print(df1.head(3)) #first 3 data
# print(df1.tail(3)) #last 3 data

## Reading data
# df=pd.read_csv('pokemon_data.csv')
# print(df.columns)
# print(df['Name']) #or df.Name
# print(df['Name'][0:5])
# print(df[['Name','Type 1','HP']])
# print(df.iloc[0:4]) #integer location or df.head(3)
# print(df.iloc[2]) #2nd row
# print(df.iloc[2,1]) #2nd row and 1st column

## Iterate through each row
# df=pd.read_csv('pokemon_data.csv')
# for index,row in df.iterrows():
#     print(index,row['Name'])

## Getting rows based on a specific condition
# df=pd.read_csv('pokemon_data.csv')
# print(df.loc[df['Type 1']=='Fire'])

## High level description of your data
# df=pd.read_csv('pokemon_data.csv')
# print(df.describe()) #mean, std dev etc.

## Sorting values
# df=pd.read_csv('pokemon_data.csv')
# print(df.sort_values('Name',ascending=False))
# print(df.sort_values(['Type 1','HP'],ascending=[1,0])) #1 is ascending and 0 is descending corresponding to Type 1 and HP respec.

## Making changes to the dataframe and saving the new dataframe
# df=pd.read_csv('pokemon_data.csv')
# df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
# print(df.head(5)) #Total column added on the side
# df=df.drop(columns=['Total']) #important to equate it to df
# print(df.head(5))
# df['Total']=df.iloc[:,4:10].sum(axis=1) #axis=1 means sum across the rows and 0 means along the columns
# ndf=df[['Total','HP','Defense']] #do this....
# print(ndf)
# cols=list(df.columns.values) #or this...
# ndf=df[[cols[4]]+[cols[6]]+[cols[12]]]
# print(ndf)
# ndf=df[cols[0:4]+[cols[-1]]+cols[4:12]] #other type of operations using cols
# df.to_csv('ndf.csv') #saving the updated df as ndf.csv
# df.to_csv('ndf.csv',index=False) #removing the index column while saving
# df.to_excel('ndf.xlsx',index=False)
# df.to_csv('ndf.txt',index=False,sep='\t') #just like delimiter while loading data into pandas, we use seperator while saving

## Filtering data
# df=pd.read_csv('pokemon_data.csv')
# print(df.loc[df['Type 1']=='Grass']) #as discussed before
# ndf1=df.loc[(df['Type 1']=='Grass')&(df['Type 2']=='Poison')&(df['HP']>70)] #and as &, or as |
# print(ndf1.iloc[:,1:5])

## Reset index
# df=pd.read_csv('pokemon_data.csv')
# ndf=df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')]
# ndf=ndf.reset_index(drop=True) #resets index to 0,1,2,so on by dropping the old indices
# print(ndf)

## RegEx filtering
# df=pd.read_csv('pokemon_data.csv')
# print(df.loc[~df['Name'].str.contains('Mega')]) #for not, use ~
# print(df.loc[df['Type 1'].str.contains('Fire|Grass',regex=True)]) #regex=True ensures that the expression is treated as a regular expression and thus operations on it are easier and powerful
# print(df.loc[df['Type 1'].str.contains('fire|grass',regex=True,flags=re.I)]) #ignores the case issue with fire and grass
# print(df.loc[df['Name'].str.contains('pi[a-z]*',regex=True)]) #all the names containing pi
# print(df.loc[df['Name'].str.contains('^pi[a-z]*',regex=True,flags=re.I)]) #all the names starting with pi


## Conditional changes
# df=pd.read_csv('pokemon_data.csv')
# df.loc[df['Type 1']=='Fire','Type 1'] = 'Flamer' #if-then-convert, changes fire to flamer
# df.loc[df['Type 1']=='Flamer','Type 1'] = 'Fire' #change back to fire if flamer, if-then-convert
# df.loc[df['Type 1']=='Fire','Legendary'] = True ; #changing legendary to true for fire type pokemons 
# df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
# df.loc[df['Total']>500, ['Generation','Legendary']] = ['TEST 1','TEST 2'] #when the total is greater than 500, both of those columns should have TEST as value by following if-then-convert

## Aggregate statistics 
# df=pd.read_csv('pokemon_data.csv')
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# ndf=df.iloc[:,4:10]
# print(ndf.groupby(['HP']).mean().sort_values('Defense',ascending=False)) #groupby the specific column and find mean for the other columns
# print(ndf.groupby(['HP']).sum()) #sum
# print(ndf.groupby(['HP']).count()) #count for number of pokemons with that HP having that specific attribute

## Working with large amounts of data
# i=1
# for df in pd.read_csv('pokemon_data.csv',chunksize=5):
#     print(f"CHUNK DF {i}") #we see that there are 160 chunks with 5 values in each chunk of df
#     print(df)
#     i=i+1
# df=pd.read_csv('pokemon_data.csv')
# ndf=pd.DataFrame(columns=df.columns) #inheriting columns from a dataframe
# for df in pd.read_csv('pokemon_data.csv',chunksize=5):
#     results=df.groupby(['Type 1']).count() #any random result formed
#     ndf=pd.concat([ndf,results]) #concat function from pandas used to merge the ndf datafram along with the random result
# print(ndf)