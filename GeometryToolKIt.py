class ShapeCalculator:
    def area(self,param1,param2=-1):
        if param2!=-1:
            return param1*param2
        else:
            return 3.14*param1*param1





shape= ShapeCalculator()
print(f"Area of Circle : {shape.area(5)}")
print(f"Area of Rectangle : {shape.area(15.2,3)}")