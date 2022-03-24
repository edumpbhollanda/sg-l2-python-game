import van

v = van.Van()

   
while not (v.at_destination()):
  
  if v.at_traffic_light('RED'):
    v.wait()
  elif v.is_road('LEFT'):
    v.turn_left()
  elif v.is_road('FORWARD'):
    v.move_forwards()
  elif v.is_road('RIGHT'):
    v.turn_right()
