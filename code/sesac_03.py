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


import numpy as np
a = np.array([1, 2, 3, 4, 5]) # 숫자형 벡터 생성
b = np.array(["apple", "banana", "orange"]) # 문자형 벡터 생성
c = np.array([True, False, True, True]) # 논리형 벡터 생성
print("Numeric Vector:", a)
print("String Vector:", b)
print("Boolean Vector:", c)
type(a)


# 행렬 인덱싱
 ## 인덱싱(Indexing) :  행렬의 특정 원소에 접근하는 방법
 ## 순서쌍 문법은 [row, col]

mat_a[0, 0]
mat_a[1, 1]
mat_a[2, 3]
mat_a[0:2, 3]
mat_a[1:3, 1:4]

# 행자리, 열자리 비어있는 경우 전체 행, 또는 열 선택
mat_a[3, ]
mat_a[3,:]
mat_a[3,::2] #열 전체 중 2스텝으로 추출

# 짝수 행만 선택하려면?
mat_b = np.arange(1, 101).reshape((20, -1))
mat_b[1::2,:] 
 ##행은 1부터 끝까지 2스텝으로, 열은 전체 

# 리스트로 직접 지정해 선택 추출
mat_b[[1, 4, 6, 14], ]

# 인덱싱/슬라이싱으로 선택 추출 

mat_b[:,1]                  # 벡터
mat_b[:,1].reshape((-1, 1)) # 행렬
mat_b[:,(1,)]               # 행렬
mat_b[:,[1]]                # 행렬
mat_b[:,1:2]                # 행렬