# Parameterised Functions

def MultiplicationTable(n):
    for i in range(1, 13, 1):
        print(f"{n} x {str(i)} = {n * i}")


def BMI(weight=0, height=0):
    if not weight or not height:
        print("provide weight and height values")
        return

    result = weight / (height ** 2)
    if result < 18.5:
        print("underweight")
    elif result >= 18.5 and result < 24.9:
        print("healthy weight")
    elif result >= 24.9 and result < 29.9:
        print("overweight")
    elif result >= 29.9:
        print("obese")



def RectArea(width=0, height=0):
    print(f"Area of the rectangle: {width * height} squared meters")



RectArea(20, 10)
RectArea(5, 10)
RectArea(7)
RectArea()























