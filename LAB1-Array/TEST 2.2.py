def create_seat_map(rows, cols):
  """สร้างแผนผังที่นั่งเริ่มต้น (ว่างทั้งหมด)"""
  return [[0 for _ in range(cols)] for _ in range(rows)]

def display_seats(seat_map):
  """แสดงแผนผังที่นั่ง"""
  for row in seat_map:
    for seat in row:
      print('O' if seat == 0 else 'X', end=' ')
    print()

def book_seat(seat_map, row, col):
  """จองที่นั่ง"""
  if 0 <= row < len(seat_map) and 0 <= col < len(seat_map[0]):
    if seat_map[row][col] == 0:
      seat_map[row][col] = 1
      print("จองที่นั่งสำเร็จ")
    else:
      print("ที่นั่งนี้ถูกจองแล้ว")
  else:
    print("พิกัดที่นั่งไม่ถูกต้อง")

def cancel_booking(seat_map, row, col):
  """ยกเลิกการจอง"""
  if 0 <= row < len(seat_map) and 0 <= col < len(seat_map[0]):
    if seat_map[row][col] == 1:
      seat_map[row][col] = 0
      print("ยกเลิกการจองสำเร็จ")
    else:
      print("ที่นั่งนี้ว่างอยู่แล้ว")
  else:
    print("พิกัดที่นั่งไม่ถูกต้อง")

def count_empty_seats(seat_map):
  """นับจำนวนที่นั่งว่าง"""
  return sum(sum(row) for row in seat_map)

# ตัวอย่างการใช้งาน
rows = 5
cols = 10
seat_map = create_seat_map(rows, cols)

display_seats(seat_map)

book_seat(seat_map, 2, 3)
book_seat(seat_map, 4, 9)

display_seats(seat_map)

cancel_booking(seat_map, 2, 3)

display_seats(seat_map)

print("จำนวนที่นั่งว่างทั้งหมด:", count_empty_seats(seat_map))