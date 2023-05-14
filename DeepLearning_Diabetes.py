from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

diabetes = load_diabetes() #데이터 셋을 불러옵니다
x = diabetes.data[:, 2] #독립 변수(x)와 종속 변수(y) 설정하기
y = diabetes.target
w = 1.0 #가중치(w)와 편향(b) 초기화하기
b = 1.0
y_hat = x[0] * w + b #예측값(y_hat) 계산하기

for x_i, y_i in zip(x, y):
    #경사 하강법(Gradient Descent)을 이용하여 가중치(w)와 편향(b) 업데이트하기
    y_hat = x_i * w + b
    err = y_i - y_hat #오차 함수 (Error function): 미분을 이용해 최적의 모델 파라미터를 찾는 과정에서 사용됩니다.
    w_rate = x_i
    w = w + w_rate * err #가중치(w) 업데이트: 미분을 이용하여 가중치를 업데이트 합니다.
    b = b + 1 * err #편향(b) 업데이트: 미분을 이용하여 편향을 업데이트 합니다.
print(w, b)

plt.scatter(x, y)
pt1 = (-0.1, -0.1 * w + b)
pt2 = (0.15, 0.15 * w + b)
plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]]) #학습된 직선을 그린다
plt.xlabel('x')
plt.ylabel('y')
plt.show()