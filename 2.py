import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
np.random.seed(0)
X = np.linspace(-5, 5, 100)
y = 2 * X + 3 + np.random.normal(scale=2, size=len(X))

# 경사하강법 함수 정의
def gradient_descent(X, y, a_init=0, b_init=0, alpha=0.01, max_iter=1000, tol=1e-6):
    a = a_init
    b = b_init
    for i in range(max_iter):
        y_pred = a*X + b
        error = y_pred - y
        cost = np.mean(error**2)

        #grad_a와 grad_b는 각각 비용 함수의 기울기를 나타내는 변수
        '''
        grad_a = np.mean(error*X) : a에 대한 편미분 값을 계산합니다.
        error는 예측값과 실제값의 차이인 오차이며, X는 입력 변수입니다.
        즉, error와 X를 곱한 값들의 평균을 grad_a에 저장합니다.
        grad_b = np.mean(error) : b에 대한 편미분 값을 계산합니다.
        error의 평균 값을 grad_b에 저장합니다.'''
        grad_a = np.mean(error*X) #a에 대한 편미분 값
        grad_b = np.mean(error) #b에 대한 편미분 값
        a -= alpha * grad_a
        b -= alpha * grad_b
        if cost < tol:
            break
    return a, b, cost

# 모델 파라미터 추정
a_hat, b_hat, cost = gradient_descent(X, y)

# 결과 출력
print("추정된 모델 파라미터: a_hat={:.2f}, b_hat={:.2f}, cost={:.2f}".format(a_hat, b_hat, cost))

# 데이터와 추정된 모델 그리기
plt.scatter(X, y, s=10)
plt.plot(X, a_hat*X + b_hat, color='r')
plt.show()
