#Code modification: simplify this call {monetary.formated(monetary.increase(value))}
import monetary
value = float(input('Insert a value: $'))
print(f'{monetary.formated(value)} increased by 10% is {monetary.increase(value, True)}')
print(f'{monetary.formated(value)} decreased by 10% is {monetary.decrease(value, True)}')
print(f'The double of {monetary.formated(value)} is {monetary.double(value, True)}')
print(f'The half of {monetary.formated(value)} is {monetary.half(value, True)}')