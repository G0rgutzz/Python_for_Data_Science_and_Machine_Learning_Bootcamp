import pandas as pd

a = pd.read_csv('Ecommerce Purchases')
ecom = pd.DataFrame(a)
print(ecom.head())
print(ecom.info())
print(len(ecom.columns))  # amount of columns
print(len(ecom.index))  # amount of rows
print(ecom['Purchase Price'].mean())  # average
print(ecom['Purchase Price'].max())  # max
print(ecom['Purchase Price'].min())  # min
print(len(ecom[ecom['Language'] == 'en']))  # language en
print(len(ecom[ecom['Job'] == 'Lawyer']))  # job title lawyer
print(ecom['AM or PM'].value_counts())
'''  # value counts makes it easier than those 2 below
print(len(ecom[ecom['AM or PM'] == 'AM']))  # bought on AM
print(len(ecom[ecom['AM or PM'] == 'PM']))  # bought on PM
'''
print(ecom['Job'].value_counts().head(5))
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
print(len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)]))
print(len(ecom[ecom['CC Exp Date'].apply(lambda e: e[3:] == '25')]))
print(ecom['Email'].apply(lambda m: m.split('@')[1]).value_counts().head(5))

