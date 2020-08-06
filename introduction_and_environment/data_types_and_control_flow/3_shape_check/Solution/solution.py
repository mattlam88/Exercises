# Code your solution here
figure = input()

shapes_dict = {
    "3" : "Triangle",
    "4" : "Quadrilateral",
    "5" : "Pentagon", 
    "6" : "Hexagon", 
    "7" : "Heptagon", 
    "8" : "Octagon", 
    "9" : "Nonagon"
}

if figure in shapes_dict.keys():
    data = shapes_dict.get(figure)

print(data)