#тест

# Подключаем библиотеки
import numpy as np
import math as m
import matplotlib.pyplot as plt
t1=np.arange(-10, 0, 0.1)
f1=-t1
t2=np.arange(0, m.pi, 0.1)
f2=np.sin(t2)
t3=np.arange(m.pi, 2*m.pi, 0.1)
f3=np.array(len(t3)*[0])
t4=np.arange(2*m.pi, 3*m.pi, 0.1)
f4=np.sin(t4)
t5=np.arange(3*m.pi, 5*m.pi, 0.1)
f5=t5-3*m.pi
plt.plot(t1,f1,t2,f2,t3,f3,t4,f4,t5,f5, 'o-r', alpha=0.7)
# Оформляем легенду
plt.title('Графики')
plt.grid(1)
plt.xlabel('Время, t')
plt.ylabel('Напряжение, U')
plt.legend('12345')


*второй график*

# Подключаем библиотеки
import numpy as np
import math as m
import matplotlib.pyplot as plt
t=np.arange(0, 3*m.pi, 0.5)
f=m.e**(-0.2*t) * np.sin(t) +  m.e**(-0.1*t) * np.cos(t)
plt.plot(t,f,'o-m',label='1')
plt.xlabel('t')
plt.ylabel('f')
# Оформляем легенду
plt.title('Графики')
plt.grid()
plt.legend()
x = [m.pi/2, m.pi, 2*m.pi]
y = [0.730403, 0.481715, 2.07592]
x = [0.5]
y = [1.26]
plt.plot(x, y, marker='o', c='g')
plt.annotate('Maximum voltage', xy=(1, 1.2))