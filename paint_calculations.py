def rectangle():
    l = float(input("\nWhat is the length of your rectangular room in feet? "))
    w = float(input("What is the width of your rectangular room in feet? "))
    area = l * w
    perimeter = 2 * l + 2 * w
    """This was my original way of trying to convert floats into decimals. It obviously doesn't work."""
    # try:
    #     area = int(area)
    # except:
    #     pass
    # try:
    #     perimeter = int(perimeter)
    # except:
    #     pass
    """Here's my actual code of trying to convert floats to decimals. It works some of the time."""
    if area % 1 == 0.0:
        area = int(area)
    if perimeter % 1 == 0.0:
        perimeter == int(perimeter)
    input(f"\nYour room's area is {str(area)} square feet, which would require about {str(area / 400)} gallons of paint. [Hit \"Enter\" to continue.]")
    input(f"Your room's perimeter is {str(perimeter)} feet, which would require about {str(perimeter)} feet of painter's tape. [Hit \"Enter\" to continue.]")


def triangle():
    a = float(input("\nGoing around your triangular room, what is the length of one of the sides in feet? "))
    b = float(input("What is the length of one of the other sides in feet? "))
    c = float(input("What is the length of the final side in feet? "))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    perimeter = a + b + c
    if area % 1 == 0.0:
        area = int(area)
    if perimeter % 1 == 0.0:
        perimeter == int(perimeter)
    input(f"\nYour room's area is {str(area)} square feet, which would require about {str(area / 400)} gallons of paint. [Hit \"Enter\" to continue.]")
    input(f"Your room's perimeter is {str(perimeter)} feet, which would require about {str(perimeter)} feet of painter's tape. [Hit \"Enter\" to continue.]")


def trapezoid():
    b1 = float(input("\nWhat is the length in feet of one of your two parallel sides? "))
    b2 = float(input("What is the length in feet of the opposite, parallel side? "))
    s1 = float(input("What is the length in feet of one of the other two sides? "))
    s2 = float(input("What is the length in feet of the remaining side? "))
    if s1 > s2:
        estimated_area = (b1 + b2) / 2 * s2
    else:
        estimated_area = (b1 + b2) / 2 * s1
    perimeter = b1 + b2 + s1 + s2
    if estimated_area % 1 == 0.0:
        estimated_area = int(estimated_area)
    if perimeter % 1 == 0.0:
        perimeter == int(perimeter)
    print('NOTE: Without knowing the exact layout of your trapezoidal floor, this area calculation is only a rough estimate.')
    input(f"\nYour room's area is {str(estimated_area)} square feet, which would require about {str(estimated_area / 400)} gallons of paint. [Hit \"Enter\" to continue.]")
    input(f"Your room's perimeter is {str(perimeter)} feet, which would require about {str(perimeter)} feet of painter's tape. [Hit \"Enter\" to continue.]")
    
def circle():
    r = float(input("\nWhat is the length stretching across your circular room in feet? (What is the room's diameter in feet?) ")) / 2
    area = 3.14 * r ** 2
    circumference = 6.28 * r
    input(f"\nYour room's area is about {str(area)} square feet, which would require about {str(area / 400)} gallons of paint. [Hit \"Enter\" to continue.]")
    input(f"Your room's circumference is about {str(circumference)} feet, which would require about {circumference} feet of painter's tape. [Hit \"Enter\" to continue.]")

def ellipse():
    a = float(input("\nWhat is the longest length in feet from one side of the room to the other that you can measure? ")) / 2
    print("What is the length in feet of the perpendicular line that cuts through the middle of the line you just measured from wall to wall? ")
    b = float(input("This should be the shortest measurement from side to side. ")) / 2
    area = 3.14 * a * b
    input(f"\nYour room's area is about {str(area)} square feet, which would require about {str(area / 400)} gallons of paint. [Hit \"Enter\" to continue.]")
    print("Do you have any idea how complicated the circumference of an ellipse is? Didn't you just measure with measuring tape? Measure it yourself!")
    print("And then, uh... you would need that much feet of tape to cover your baseboards... Ok, I'm sorry for snapping there;")
    input("I just had a rude experience with a shopping list maker, and I'm not in a good mood. [Hit \"Enter\" to continue.]")