import van

v = van.Van()

for count in range(36):
  if v.is_road('FORWARD'):
    v.move_forwards()
  elif v.is_road('LEFT'):
    v.turn_left()
  elif v.is_road('RIGHT'):
    v.turn_right()
