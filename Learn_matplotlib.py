#기본 그래프
#plt.plot() 함수를 사용하여 리스트 [1, 2, 3, 4]를 그래프 상에 표시합니다.
'''import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()'''

#막대 그래프 그리기
#np.arange() 함수를 사용하여 0부터 2까지의 배열을 만들고, plt.bar() 함수를 사용하여 각 값의 막대를 그립니다.
'''import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)

plt.show()'''

#스캐터차트 그리기
#np.random.rand() 함수를 사용하여 0부터 1까지의 난수를 생성하고, plt.scatter() 함수를 사용하여 이를 산포도로 그립니다.
'''import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x, y)
plt.show()'''

#스캐터차트 이쁘게 꾸미기
#s와 c 매개변수를 사용하여 마커의 크기와 색상을 지정하고,
#alpha 매개변수를 사용하여 투명도를 조절합니다.
#cmap 매개변수를 사용하여 색상 맵을 지정하고, plt.colorbar() 함수를 사용하여 색상 막대를 추가합니다.
'''import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30 * np.random.rand(n))**2
colors = np.random.rand(n)

plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
plt.colorbar()
plt.show()'''

#박스 플롯 그리기
#np.random.normal() 함수를 사용하여 정규 분포에서 난수를 생성하고, ax.boxplot() 함수를 사용하여 이를 박스 플롯으로 그립니다.
'''import matplotlib.pyplot as plt
import numpy as np
# 1. 기본 스타일 설정
plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 12

# 2. 데이터 준비
np.random.seed(0)
data_a = np.random.normal(0, 2.0, 1000)
data_b = np.random.normal(-3.0, 1.5, 500)
data_c = np.random.normal(1.2, 1.5, 1500)

# 3. 그래프 그리기
fig, ax = plt.subplots()

ax.boxplot([data_a, data_b, data_c])
ax.set_ylim(-10.0, 10.0)
ax.set_xlabel('Data Type')
ax.set_ylabel('Value')

plt.show()'''

#원 그래프 그리기
#plt.pie() 함수를 사용하여 비율과 라벨을 지정하고, autopct 매개변수를 사용하여 각 항목의 비율을 표시합니다.
'''import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()'''