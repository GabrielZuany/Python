def increase(value = 0, Format=False):
    res = value*1.1
    return res if Format==False else formated(res)
def decrease(value = 0, Format=False):
    res = value*0.9
    return res if Format==False else formated(res)
def double(value = 0, Format=False):
    res = value*2
    return res if Format==False else formated(res)
def half(value = 0, Format=False):
    res = value/2
    return res if Format==False else formated(res)
def formated(value = 0, mod='R$'):
    return f'{mod}{value:.2f}'.replace('.', ',')