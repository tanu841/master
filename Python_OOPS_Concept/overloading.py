class Sqaure:
    def __init__(self, side):
        self.side = side

    def __add__(squareOne, squareTwo):
        return ((4 * squareOne.side) + (4 * squareTwo.side))


squareOne =Sqaure(5)
squareTwo =Sqaure(10)

print("Sum of sides of both the squares is: ", squareOne + squareTwo)