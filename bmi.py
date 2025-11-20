import sys

if len(sys.argv) == 3:
    weight = sys.argv[1]
    height = sys.argv[2]
else:
    weight = "60"
    height = "1.6"

weight = eval(weight)
height = eval(height)
print("BMI:", weight / (height * height))
