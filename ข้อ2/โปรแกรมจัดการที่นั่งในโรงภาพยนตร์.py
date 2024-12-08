# สร้างแผนผังที่นั่ง 5x5 (0 = ว่าง, 1 = จองแล้ว)
seats = [[0] * 5 for _ in range(5)]

# ฟังก์ชันแสดงแผนผังที่นั่ง
def display_seats():
    print("\nแผนผังที่นั่ง (0 = ว่าง, 1 = จอง):")
    for row in seats:
        print(" ".join(map(str, row)))

# ฟังก์ชันจองที่นั่ง
def book_seat(row, col):
    if seats[row][col] == 0:
        seats[row][col] = 1
        print("จองที่นั่งสำเร็จ!")
    else:
        print("ที่นั่งนี้ถูกจองแล้ว!")

# ฟังก์ชันยกเลิกการจอง
def cancel_seat(row, col):
    if seats[row][col] == 1:
        seats[row][col] = 0
        print("ยกเลิกการจองสำเร็จ!")
    else:
        print("ที่นั่งนี้ยังว่างอยู่!")

# ฟังก์ชันแสดงจำนวนที่นั่งว่าง
def count_available_seats():
    print(f"จำนวนที่นั่งว่าง: {sum(row.count(0) for row in seats)} ที่นั่ง")

# เมนูหลัก
while True:
    print("\n1. แสดงแผนผังที่นั่ง\n2. จองที่นั่ง\n3. ยกเลิกการจอง\n4. แสดงจำนวนที่นั่งว่าง\n5. ออกจากโปรแกรม")
    choice = input("เลือกคำสั่ง: ")

    if choice == "1":
        display_seats()
    elif choice == "2":
        r, c = map(int, input("ป้อนแถวและคอลัมน์ที่ต้องการจอง (เช่น 1 2): ").split())
        book_seat(r - 1, c - 1)
    elif choice == "3":
        r, c = map(int, input("ป้อนแถวและคอลัมน์ที่ต้องการยกเลิกจอง (เช่น 1 2): ").split())
        cancel_seat(r - 1, c - 1)
    elif choice == "4":
        count_available_seats()
    elif choice == "5":
        print("ออกจากโปรแกรม!")
        break
    else:
        print("กรุณาเลือกคำสั่งที่ถูกต้อง!")
