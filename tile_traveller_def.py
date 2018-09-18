def routes(direction, route):
  for i in route:
    if i in direction:
      return True
  return False
      

def new_route(x, y):
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


def printed(route):
  if route != "":
    print("You can travel: ", end="")

  for i in range(len(route)):
      if i != 0:
        print(" or ", end="")
      if route[i] == "N":
        print("(N)orth", end="")
      elif route[i] == "E":
        print("(E)ast", end="")
      elif route[i] == "S":
        print("(S)outh", end="")
      elif route[i] == "W":
        print("(W)est", end="")
  print(".")


x = 1
y = 1
route = "N"
print("You can travel: (N)orth.")

while not (x == 3 and y == 1):
  direction = input("Direction: ").upper()
  if routes(direction, route):
    if direction == "N":
      y += 1
    if direction == "E":
      x += 1
    if direction == "S":
      y -= 1
    if direction == "W":
      x -= 1

    route = new_route(x, y)
    printed(route)
  else:
      print("Not a valid direction!")
      

print("Victory!")
