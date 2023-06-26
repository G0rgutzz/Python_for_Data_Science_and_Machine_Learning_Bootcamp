import pandas as pd

sal = pd.read_csv('Salaries.csv')
print(sal)
print(sal.head(3))
print(sal.info())
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])  # more advanced method, argmax() is also possible
print(sal.loc[sal['TotalPayBenefits'].idxmin()])
print(sal.loc[sal['TotalPayBenefits'].idxmax()])
print(sal.groupby('Year').mean(numeric_only=True)['BasePay'])
print(sal['JobTitle'].nunique())
print(sal['JobTitle'].value_counts().head(5))  # head() gives the number of rows from data frame
# print(sal[sal['Year'] == 2013]['JobTitle'].nunique())
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))


def chief(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(lambda x: chief(x))))

sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['TotalPayBenefits', 'title_len']].corr())
