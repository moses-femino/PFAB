length = int(input("Enter a number that represents length in feet."))
width = int(input("Enter a number that represents width in feet."))
height = int(input("Enter a number that represents height in feet."))

def prism_vol(l, w, h):
  return l * w * h

print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")
#rectangular prism problem