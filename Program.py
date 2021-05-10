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
    
  
    
# def theAccelerate():
    
    #i = 0
    
    #while i <= 4:
        #print(the_car.accelerate())
        #i += 1
        #print(i)
    
#def theBrake():
    
    #d = 4
    
    #while d >= 0:
        #print(the_car.brake())
        #d -= 1
        #print(d)
        

main()

# def theLoops():
    
    # i = 0
    # d = 25

    # while i <= 25:
        # print(i)
        # i += 5
        

    # while d >= 25:
        # print(d)
        # d -= 5
    

