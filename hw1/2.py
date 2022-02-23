# Пользователь задает любое количество чисел с экрана,разделяя их запятыми.
# Реализовать алгоритм,который распределяет числа на
# натуральные, целые, рациональные, вещественные, комплексные, четные, нечетные и простые.
# Обратите внимание, что цифры могут попадать в несколько категорий

# пример входных данных:
# 1,2,3,-6,-7.5,3*i-7,i,0.98,i,i,3*i-7,-400.78299,837826287.97,113,9,-15
# 1,2,3.454,4*i-2,-400.90087,2-5*i

def sortNumbers(numbers, symbol, new):
    for number in numbers:
        if number.rfind(symbol) == -1:
            new.append(number)
    return new


line = input('Enter numbers separated by commas:\n')
numbers = line.split(",")
realNumbers = []
integerNumbers = []
naturalNumbers = []
evenNumbers = []
oddNumbers = []
primeNumbers = []

print('Complex numbers:\n', ' '.join(numbers))
print('Real numbers:\n', ' '.join(sortNumbers(numbers, 'i', realNumbers)))
print('Integer numbers:\n', ' '.join(sortNumbers(realNumbers, '.', integerNumbers)))


for number in integerNumbers:
    if int(number) > 0:
        naturalNumbers.append(number)

print('Natural numbers:\n', ' '.join(naturalNumbers))

for number in integerNumbers:
    if int(number) % 2 == 0:
        evenNumbers.append(number)
    else:
        oddNumbers.append(number)

print('Even numbers:\n', ' '.join(evenNumbers))
print('Odd numbers:\n', ' '.join(oddNumbers))

# for number in integerNumbers:
#     if int(number) < 2:
#         break
#     for i in range(2, int(int(number) ** 0.5 + 1)):
#         if int(number) % i == 0:
#             break
#     else:
#         primeNumbers.append(number)
#
# print('Prime numbers:\n', ' '.join(primeNumbers))
