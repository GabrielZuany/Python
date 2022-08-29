#New feature: formatad monetary data (100.00 -> R$100,00)
import monetary
value = float(input('Insert a value: $'))
print(f'{monetary.formated(value)} increased by 10% is {monetary.formated(monetary.increase(value))}')
print(f'{monetary.formated(value)} decreased by 10% is {monetary.formated(monetary.decrease(value))}')
print(f'The double of {monetary.formated(value)} is {monetary.formated(monetary.double(value))}')
print(f'The half of {monetary.formated(value)} is {monetary.formated(monetary.half(value))}')