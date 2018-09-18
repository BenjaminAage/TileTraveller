def routes(direction, route):
  for i in route:
    if i in direction:
      return True
  return False
      
#       
#       if direction == "N":
#         y += 1
#       elif direction == "E":
#         x += 1
#       elif direction == "S":
#         y -= 1
#       elif direction == "W":
#         x -= 1
#       break
#   else:
#     print("Not a valid direction!")
# 

def new_route(x, y):
  if x2 != x or y2 != y:
    if x == 1 and y == 1:
      return "N"
    elif x == 1 and y == 2:
      return "NES"
    elif x == 1 and y == 3:
      return "ES"
    elif x == 2 and y == 1:
      return "N"
    elif x == 2 and y == 2:
      return "SW"
    elif x == 2 and y == 3:
      return "EW"
    elif x == 3 and y == 1:
      return ""
    elif x == 3 and y == 2:
      return "NS"
    elif x == 3 and y == 3:
      return "SW"
    print("You can travel: ", end="")

def printed():
  for i in range(len(route)):
      if i != 0:
        print(" or", end="")
      if route[i] == "N":
        print("(N)orth", end="")
      elif route[i] == "E":
        print("(E)ast", end="")
      elif route[i] == "S":
        print("(S)outh", end="")
      elif route[i] == "W":
        print("(W)est", end="")
    print()

  print("Victory!")


x = 1
y = 1
route = "N"

while True:
  x2 = x
  y2 = y
  direction = input("Direction: ").upper()



  
  
    