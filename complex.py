from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class Complex:
    real: float
    imag: float

    def __str__(self):
        if self.imag >= 0:
            sign = '+'
        else:
            sign = '-'
        return f'{self.real} {sign} {abs(self.imag)}i'

    def __abs__(self):
        """
        Перегрузка функции abs() - взятие по модулю
        :return: Модуль данного комплексгого числа
        """
        return (self.real**2 + self.imag**2)**0.5

    def __add__(self, other):
        """
        Перегрузка оператора "+" (Сумма двух комплексных чисел)
        :param other: Второе число
        :return: Сумма
        """
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        """
         Перегрузка оператора "-" (Разность двух комплексных чисел)
         :param other: Второе число
         :return: Разность
         """
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        """
        Перегрузка оператора "+" (Сумма двух комплексных чисел)
        :param other: Второе число
        :return: Сумма
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag + other.real
        return Complex(real, imag)


    def plot(self, fig):
        fig.plot(self.real, self.imag, 'rs')
        fig.grid(True)
        fig.text(self.real + 0.05, self.imag, f'({self.real}, {self.imag})')
        fig.plot([0, self.real], [0, self.imag], 'c-', linewidth=2 )


if __name__ == '__main__':
    c1 = Complex(5.0, -3.0)
    c2 = Complex(0, 1)
    c3 = c1 * c2
    # Оформление
    fig, ax = plt.subplots()
    plt.xlabel('Re')
    plt.ylabel('Im')
    ax.axvline(0, -6, 6, linewidth=2, color='g')
    ax.axhline(0, -6, 6, linewidth=2, color='g')
    # Построение
    c1.plot(ax)
    c2.plot(ax)
    c3.plot(ax)
    plt.axis('square')
    plt.show()
    #print('Сумма: ', c1 + c2)
    #print('Разность: ', c1 - c2)
    #print('Произведение: ', c1*c2)