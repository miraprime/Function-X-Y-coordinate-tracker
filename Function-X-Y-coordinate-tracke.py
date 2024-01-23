x_pos = 0
y_pos = 0
x_start_pos = 0
x_end_pos =10
y_start_pos = 0
y_end_pos = 10

def movement_x(x_pos, by_amount=1):
  global x_start_pos, x_end_pos
  x_pos += by_amount
  if x_pos < x_start_pos:
    return x_start_pos
  elif x_pos > x_end_pos:
    return x_end_pos
  return x_pos
def movement_y(y_pos, by_amount=1):
  global y_start_pos, y_end_pos
  y_pos += by_amount
  if y_pos < y_start_pos:
    return y_start_pos
  elif y_pos > y_end_pos:
    return y_end_pos
  return y_pos

x_pos = movement_x(x_pos, int(input("player x move ")))
y_pos = movement_y(y_pos, int(input("player y move ")))
print(x_pos)
print(y_pos)