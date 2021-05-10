import car

def main():
    
    # create an object from the Car class
    # the_car = Car(year, make)
    the_car = car.Car(2007, 'camry')
    
    the_car.accelerate()
    the_car.accelerate()
    the_car.accelerate()
    the_car.accelerate()
    the_car.accelerate()
    print('Your max speed is ', the_car.get_speed())
    the_car.brake()
    the_car.brake()
    the_car.brake()
    the_car.brake()
    the_car.brake()
    print('Your decelerated speed is ', the_car.get_speed())
    

main()

