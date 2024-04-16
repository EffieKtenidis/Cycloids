import turtle
import numpy as np
import math
from math import sin, cos, pi

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


def drawArr(arr, scale=25, polar=True):
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
  t.penup()
  for p in range(len(arr)):
    if p > 0:
      t.pendown()
    p = arr[p]
    if polar:
      x, y = polarToCartesian(p)
    else:
      x, y = p
    x *= scale
    y *= scale
    t.goto(x, y)


def cycloid(maxInc=100, rDiv=30):
  r = maxInc/rDiv
  data = []
  for i in range(maxInc):
    t = i
    x = r * (t - sin(t))
    y = r * (1 - cos(t))
    data.append([x, y])
  
  return np.array(data)


def hyperCycloidData(thetaRange, ratio, resolution=100):
  assert len(thetaRange) == 2, 'thetaRange must be list of two vals'

  data = []
  start, stop = thetaRange
  r = 1
  R = ratio
  for theta in np.linspace(start, stop, resolution):
    # x = (R - r) * cos(theta) + r * cos(((R - r) * theta) / r)
    # y = (R - r) * sin(theta) - r * sin(((R - r) * theta) / r)
    x = (R - r) * cos(theta * (r/R)) + r * cos(((R - r) * theta) / r)
    y = (R - r) * sin(theta * (r/R)) - r * sin(((R - r) * theta) / r)

    data.append([x, y])
  
  return np.array(data)


if __name__ == '__main__':
  # data = cycloid()
  tRange = [0, 2*pi*6]
  R, r = 4, 1
  ratio = R/r
  data = hyperCycloidData(tRange, ratio, resolution=800)
  print(data)
  print(f'Building Hypercycloid with ratio: {ratio}')
  drawArr(data, scale=60, polar=False)
  turtle.done()

  '''
  Result notes:
    2.5 => 5 point sharp star
    3   => 3 pointed tri
    3.5 => 7 pointed star
    4   => 4 pointed star(ish)
    4.5 => 9 pointed star
    5   => 5 pointed wide star(ish)
    5.5 => 10 pointed star

    1/6.5 => more like a "normal" spirograph,
      but can't figure out adjusting pen point on internal circle
  '''