def increase(value = 0):
    return value*1.1
def decrease(value = 0):
    return value*0.9
def double(value = 0):
    return value*2
def half(value = 0):
    return value/2
def formated(value = 0, mod='R$'):
    return f'{mod}{value:.2f}'.replace('.', ',')