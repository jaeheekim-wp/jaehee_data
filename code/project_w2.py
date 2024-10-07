import pandas as pd
import numpy as pd
import seaborn as sns
import matplotlib as plt

# 데이터 불러오기
data = pd.read_csv("data/data_week2.csv", encoding='cp949')
data.head()
data.info()
data.describe()
