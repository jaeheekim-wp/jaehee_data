a=1
a

import numpy as np
a = np.array([1, 2, 3, 4, 5]) # 숫자형 벡터 생성
b = np.array(["apple", "banana", "orange"]) # 문자형 벡터 생성
c = np.array([True, False, True, True]) # 논리형 벡터 생성
print("Numeric Vector:", a)
print("String Vector:", b)
print("Boolean Vector:", c)
type(a)

import pandas as pd
df =  pd.read_csv('data/scores.csv')
df

# 시리즈
df['name']
df.name
# 데이터프레임
df[['name']]
df.index
df.shape
df[["name","eng"]]

# 인덱스/ 컬럼명으로 추출

df.index = 'i' + df.index.astype("str")
df.head()

s1 = df.loc["i3"]
s1.values
# df.loc[0] 인덱스가 문자열일때는 번호로 뽑을 수 없음 .

df.loc[['i1','i3','i5']]

# 행열 같이 추출
df.loc["i1",'kor']
type(df.loc["i1",'kor'])

# 열 여러개
df.loc["i1",["name","kor"]]
# 행 여러개
df.loc[["i1","i2","i3"],"name"]
# 행/열 여러개
df.loc[["i1","i2","i3"],["name","kor"]]
# 모든 행에서 컬럼 추출
df.loc[:,"name"] # 시리즈
df.loc[:,["name"]] # 데이터프레임
df.loc[:,["name","math"]]

# ========
# iloc 사용

df.iloc[0]
df.iloc[[1,3,5]]

# 슬라이싱 추출
df.iloc[0:4]
# 1,3,5 행 추출
df.iloc[1:6:2]
# 1행만
df.iloc[1:2]
# 짝수
df.iloc[::2]
# 홀수
df.iloc[1::2]
# 마지막 행
df.iloc[-1]
# 마지막 두개행(리스트로)
df.iloc[[-2,-1]]
# 마지막 두개행(슬라이싱)
df.iloc[-2:]
df.iloc[0,0]
df.iloc[0,1:3]
# df.iloc[0,[1,2]] # 리스트

# 마지막행 1,3열 슬라이싱
df.iloc[-1,1:4:2]

# 모든 행,1열
df.iloc[:,1]