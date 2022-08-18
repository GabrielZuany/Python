#Make a script that reads 5 peoples weight and print the higher and lower weight.
HigherWeight = 0
LowerWheight = 1000

for count in range(0, 5, +1):
    weight = float(input('Insert your weight: '))

    if weight > HigherWeight:
        HigherWeight = weight
    if weight < LowerWheight:
        LowerWheight = weight

print('Higher weight: {}\nLower weight: {}' .format(HigherWeight, LowerWheight))