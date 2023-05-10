#Make a script that reads the velocity of a car. If the velocity is >80Km/h, print a message and aplly a traffic ticket (R$7,00 / km/h>80)
vel = float(input('Insert the velocity: '))
if(vel > 80):
    print('FINED! Your velocity was {}\nYou will pay {} of traffic ticket' .format(vel, ((vel-80)*7)))
