from math import atan2, degrees, radians, sin, cos

class Force:
    def __init__(self, magnitude, angle):
        self.magnitude = round(magnitude, 1)
        self.angle = angle
    def get_horizontal(self):
        return self.magnitude * (cos(radians(self.angle)))
    def get_vertical(self):
        return self.magnitude * (sin(radians(self.angle)))
    def get_angle(self, use_degrees = True):
        if use_degrees == True:
            return round(degrees(self.angle),1)
        if use_degrees == False:
            return round(radians(self.angle), 1)

def find_net_force(instance):
    total_horizontal = 0
    total_vertical = 0
    for i in instance:
        total_horizontal += i.get_horizontal()
        total_vertical += i.get_vertical()
    
    magnitude = (total_horizontal ** 2 + total_vertical ** 2) ** 0.5
    angle = atan2(total_vertical, total_horizontal)
    new_Force = Force(magnitude,angle)
    return new_Force


#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print:
#103.1
#-14.0

force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())



