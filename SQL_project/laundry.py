import pandas as pd
import koreanize_matplotlib
import numpy as np

df = pd.read_excel('laundry.xlsx')
print(df)

df = df.loc[:,['번호', '소재지전체주소', '사업장명']]
print(df)

df['region'] = df['소재지전체주소'].str.extract(r'(대구광역시\s+\S+(?:구|군)\s+\S+(?:동|로|읍|면))')
print(df)

df = df.drop(columns = '소재지전체주소')
print(df)

conditions = [
    df['region'].str.contains('중구'),
    df['region'].str.contains('동구'),
    df['region'].str.contains('서구'),
    df['region'].str.contains('남구'),
    df['region'].str.contains('북구'),
    df['region'].str.contains('수성구'),
    df['region'].str.contains('달서구'),
    df['region'].str.contains('달성군'),
    df['region'].str.contains('군위군')
]

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

df['dong_id'] = np.select(conditions, values, default = None)

df = df.rename(columns = {'번호' : 'number', '사업장명' : 'name'})

df.to_csv('laundry_daegu.csv', index = False)