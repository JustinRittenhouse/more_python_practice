from paint_calculations import rectangle, triangle, trapezoid, circle, ellipse

def paint():
    print('\nWelcome to the Floor Painting Calculator. Here we can tell you how much resources you need for your painting projects.')
    print('We calculate the amount of paint needed to paint your floor, and the length of tape needed to protect all your baseboards.')
    print('This is accomplished by finding the areas and perimeters of your rooms, which will also be displayed.')
    print('NOTE: We assume that you would use one gallon of paint for every 400 square feet of floor.')
    more_calculations = 'y'
    while more_calculations == 'y':
        print('\nWhat type of basic shape does your floor layout match the most closely?')
        room_shape = input('Type "rectangle," "triangle," "trapezoid," "circle," or "ellipse." ').lower()
        if room_shape == 'rectangle':
            rectangle()
        elif room_shape == 'triangle':
            triangle()
        elif room_shape == 'trapezoid':
            trapezoid()
        elif room_shape == 'circle':
            circle()
        elif room_shape == 'ellipse':
            ellipse()
        more_calculations = input('\nWould you like to make another calculation? ["Y"/"N"] ').lower()
        if more_calculations == 'n':
            print('\nOk. Good luck with your painting!')
        elif more_calculations != 'y':
            print("I don't understand your request. I'm stopping the program. Have a nice day!")

paint()