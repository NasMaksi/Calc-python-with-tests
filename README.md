# Калькулятор на Python

Простой, но мощный калькулятор с поддержкой математических операций и unit-тестами.

## Функциональность
- Базовые операции: `+`, `-`, `*`, `/`
- Возведение в степень (`^`)
- Квадратный корень
- Тригонометрические функции: `sin`, `cos`, `tan`
- Логарифмы и экспонента
- Факториал
- Подробная обработка ошибок

## Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/NasMaksi/Calc-python-with-tests.git
   cd Calc-python-with-tests
2. Установите зависимости:
  pip install pytest
3. Запустите калькулятор:
python calculator.py
4. Запустите тесты:
   pytest test_calculator.py -v

Может использоваться через код:
from calculator import Calculator
print(Calculator.add(2, 3))  # 5
print(Calculator.sin(math.pi/2))  # 1.0

Технические детали
Написан на Python 3.8+
Использует модуль math для сложных операций
Полное покрытие тестами (pytest)
   
   
