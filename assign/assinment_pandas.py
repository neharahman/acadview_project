import pandas as pd
'''Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.'''
dic={'name':['Neha'],'age':[20],'mail_id':['abc12@gmail.com'],'phone_no.':['1234567890']}
df=pd.DataFrame(dic)
df.loc[1]=['mote',22,'mote1@gmail.com','9876543210']
df.loc[2]=['chotu',20,'chotu45@gmail.com','9087564312']
print(x)

'''Q.2 - 
Import the data and print the following :
a.) First 5 rows of Dataframe 
b.) First 10 rows of the Dataframe 
c.) find basic statistics on the particular dataset. 
d.) Find the last 5 rows of the dataframe 
e.) Extract the 2nd column and find basic statistics on it.
'''
df=pd.read_csv('dataset.csv')
print("First 5 rows of Dataframe ",df.head(5))
print("First 10 rows of the Dataframe ",df.head(10))
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())
print(df.tail(5))
new_data=[df.iloc[:,2].sum(),df.iloc[:,2].mean(),df.iloc[:,2].median(),df.iloc[:,2].nunique(),df.iloc[:,2].max(),df.iloc[:,2].min()]
print(new_data)
