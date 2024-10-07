import numpy as np


a = 0
b = 3
while a<11 :
    if b == 5:
        print(a)
    a+=1
    b+=1
  
# 여러 항목을 제거하는 방법
fruits = ["apple", "banana", "cherry", "apple", "banana"]
# 제거할 항목 리스트
items_to_remove = ["banana", "apple"]
# 반복문을 사용하여 항목 제거
for item in items_to_remove:
    while item in fruits:
        fruits.remove(item)
# print("remove() 후 리스트:", fruits)
fruits


my_df = pd.DataFrame({
'실수변수': pd.Series(dtype='float'),
'정수변수': pd.Series(dtype='int'),
'범주형변수': pd.Series(dtype='category'),
'논리변수': pd.Series(dtype='bool'),
'문자열변수': pd.Series(dtype='str')
})



