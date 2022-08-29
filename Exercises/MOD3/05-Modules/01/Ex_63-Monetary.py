#Make a program that have the functions: increase(),decrease(), double() and half(). Separate these functions into modules and import it.
import monetary
value = float(input('Insert a value: $'))
print(f'Value increased by 10% is {monetary.increase(value):.2f}')
print(f'Value decreased by 10% is {monetary.decrease(value):.2f}')
print(f'The double is {monetary.double(value)}')
print(f'The half is {monetary.half(value)}')