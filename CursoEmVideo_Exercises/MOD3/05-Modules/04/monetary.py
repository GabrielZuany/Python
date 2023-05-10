def increase(value = 0, perc = 0, Format=False):
    res = value*(1+perc/100)
    return res if Format==False else formated(res)
def decrease(value = 0, perc = 0, Format=False):
    res = value*(1-perc/100)
    return res if Format==False else formated(res)
def double(value = 0, Format=False):
    res = value*2
    return res if Format==False else formated(res)
def half(value = 0, Format=False):
    res = value/2
    return res if Format==False else formated(res)
def formated(value = 0, mod='R$'):
    return f'{mod}{value:.2f}'.replace('.', ',')
def resume(value = 0, up = 0, down = 0):
        print(f'{formated(value)} increased by {up}% is:\t{increase(value, up, True)}')
        print(f'{formated(value)} decreased by {down}% is:\t{decrease(value, down, True)}')
        print(f'The double of {formated(value)} is:\t{double(value, True)}')
        print(f'The half of {formated(value)} is:\t{half(value, True)}')