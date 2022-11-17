import math

e = math.e

def DISC_Distr_Binomial(n = 1, p = 1, evento = 0):
    combinacao = math.comb(n, evento)
    pot = math.pow(p, evento)
    pot2 = math.pow((1-p), n-evento)
    prob = combinacao*pot*pot2
    return prob

def DISC_Distr_Geometrica(p = 1, evento = 0):
    prob = p*math.pow((1-p), evento-1)
    return prob

def DISC_Distr_Hipergeometrica(N, r, k, evento):
    comb = math.comb(r, k)
    comb2 = math.comb((N-r), (evento-k))
    comb3 = math.comb(N, evento)
    prob = comb*comb2/comb3
    return prob

def Poisson(tetha, evento):
    return (pow(e, -tetha)*pow(tetha, evento))/(math.factorial(evento))

def DISC_Esperanca_Binomial(n, p):
    return n*p

def DISC_Esperanca_Geometrica(p):
    return 1/p

def DISC_Esperanca_Hipergeometrica(evento, r, N):
    return evento*r/N

def DISC_Variancia_Hipergeometrica(evento, r, N):
    return (evento*r/N)*(1-r/N)*((N-evento)/(N-1))
