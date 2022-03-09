from random import randint
from tabulate import tabulate


def expectationSearch(array):
    expected_value = 0
    for x in array:
        expected_value += probability * x
    return expected_value


def dispersionSearch(array, expected_value):
    expected_value_new = 0
    for x in array:
        expected_value_new += x**2 * probability
    dispersion = expected_value_new - expected_value**2
    return dispersion


print('Enter number of rows and columns(n): ')
n = int(input())
probability = 1/n
randomVariables = [[randint(1, 30) for j in range(n)] for i in range(n)]
print('resulting table:')
print(tabulate(randomVariables))

for i in range(n):
    print(f'{i+1} row:\nexpected value =', format(expectationSearch(randomVariables[i]), '.3f'),
          '\ndispersion =', format(dispersionSearch(randomVariables[i], expectationSearch(randomVariables[i])), '.3f'))

# print('Expected value and dispersion in which row do you want to count?')
# row = int(input())
# print('expected value =', expectationSearch(randomVariables[row-1]),
#       '\n dispersion =', dispersionSearch(randomVariables[row-1], expectationSearch(randomVariables[row-1])))
