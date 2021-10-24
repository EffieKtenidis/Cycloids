import turtle
import numpy as np
import math

def polarToCartesian(coord):
  '''
  Arguments:
    coord: Polar coordinate in form (r, theta)
  Returns:
    Cartesian coordate cooresponding to given polar input
  '''
  assert len(coord) == 2, 'Polar coordinate input must be dim of 2'

  r, theta = coord
  x = r * math.cos(theta)
  y = r * math.sin(theta)

  return x, y


def drawArr(arr, scale=25):
  '''
  Arguments:
    arr: Nx2 numpy array, where each row is a polar coordinate point.
  Returns:
    None: Draw array with turtle
  '''
  t = turtle.Turtle()
  t.speed('fastest')
  t.clear()
  t.hideturtle()
  for p in range(len(arr)):
    p = arr[p]
    x, y = polarToCartesian(p)
    # x, y = p
    x *= scale
    y *= scale
    t.goto(x, y)


if __name__ == '__main__':
  data = []
  maxInc = 20
  for i in range(maxInc):
    r = math.sin(i)
    theta = (i / maxInc) * (2*math.pi)
    data.append([r, theta])
  
  data = np.array(data)
  print(data)
  drawArr(data)
