def routes(i):
  for i in route:
    if i in direction:
      if direction == "N":
        y += 1
      elif direction == "E":
        x += 1
      elif direction == "S":
        y -= 1
      elif direction == "W":
        x -= 1
      break
  else:
    print("Not a valid direction!")


def status():
  if x2 != x or y2 != y:
    if x == 1 and y == 1:
      route = "N"
    elif x == 1 and y == 2:
      route = "NES"
    elif x == 1 and y == 3:
      route = "ES"
    elif x == 2 and y == 1:
      route = "N"
    elif x == 2 and y == 2:
      route = "SW"
    elif x == 2 and y == 3:
      route = "EW"
    elif x == 3 and y == 1:
      break
    elif x == 3 and y == 2:
      route = "NS"
    elif x == 3 and y == 3:
      route = "SW"
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



  
  
    