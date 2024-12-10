#ผังที่นั่งทั้งหมด
rows, cols = 5, 6
seats = [[0 for _ in range(cols)] for _ in range(rows)]

def show_seats():
    print("\nแผนผังที่นั่ง (0 = ว่าง, 1 = จอง):")
    for row in seats:
        print(" ".join(map(str, row)))

def book_seat(row, col):
    if seats[row][col] == 0:
        seats[row][col] = 1
        print(f"จองที่นั่งแถว {row + 1} คอลัมน์ {col + 1} เรียบร้อย")
    else:
        print(f"ที่นั่งแถว {row + 1} คอลัมน์ {col + 1} ถูกจองไปแล้ว")

def cancel_booking(row, col):
    if seats[row][col] == 1:
        seats[row][col] = 0
        print(f"ยกเลิกการจองที่นั่งแถว {row + 1} คอลัมน์ {col + 1} เรียบร้อย")
    else:
        print(f"ที่นั่งแถว {row + 1} คอลัมน์ {col + 1} ไม่ได้ถูกจอง")

def count_available_seats():
    available = sum(row.count(0) for row in seats)
    print(f"\nจำนวนที่นั่งว่างทั้งหมด : {available} ที่นั่ง")

#ผลลัพธ์
show_seats()
book_seat(3, 4)
book_seat(1, 2)
cancel_booking(3, 4)
count_available_seats()
show_seats()