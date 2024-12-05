# สร้างแผนผังที่นั่งในโรงภาพยนตร์ (5 แถว 5 คอลัมน์)
seats = [['ว่าง' for _ in range(5)] for _ in range(5)]  # 5x5 แผนที่นั่ง

# ฟังก์ชันแสดงแผนผังที่นั่ง
def display_seats():
    print("\nแผนผังที่นั่ง:")
    for row in seats:
        print(" | ".join(row))
        print("-" * 19)  # สร้างเส้นแบ่งแถว

# ฟังก์ชันจองที่นั่ง
def book_seat(row, col):
    if seats[row][col] == 'ว่าง':
        seats[row][col] = 'จอง'
        print(f"จองที่นั่งแถว {row+1} คอลัมน์ {col+1} เรียบร้อยแล้ว!")
    else:
        print(f"ที่นั่งแถว {row+1} คอลัมน์ {col+1} ถูกจองแล้ว!")

# ฟังก์ชันยกเลิกการจองที่นั่ง
def cancel_seat(row, col):
    if seats[row][col] == 'จอง':
        seats[row][col] = 'ว่าง'
        print(f"ยกเลิกการจองที่นั่งแถว {row+1} คอลัมน์ {col+1} เรียบร้อยแล้ว!")
    else:
        print(f"ที่นั่งแถว {row+1} คอลัมน์ {col+1} ยังไม่ถูกจอง!")

# ฟังก์ชันแสดงจำนวนที่นั่งว่าง
def available_seats():
    count = sum(row.count('ว่าง') for row in seats)  # นับจำนวนที่นั่งว่าง
    print(f"\nจำนวนที่นั่งว่างทั้งหมด: {count} ที่นั่ง")

# เมนูหลัก
while True:
    print("\n1. แสดงแผนผังที่นั่ง")
    print("2. จองที่นั่ง")
    print("3. ยกเลิกการจองที่นั่ง")
    print("4. แสดงจำนวนที่นั่งว่างทั้งหมด")
    print("5. ออกจากโปรแกรม")
    
    choice = input("เลือกคำสั่ง: ")

    if choice == "1":
        display_seats()
    elif choice == "2":
        row = int(input("กรุณากรอกแถวที่นั่ง (1-5): ")) - 1
        col = int(input("กรุณากรอกคอลัมน์ที่นั่ง (1-5): ")) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            book_seat(row, col)
        else:
            print("กรุณากรอกแถวและคอลัมน์ในช่วง 1-5!")
    elif choice == "3":
        row = int(input("กรุณากรอกแถวที่นั่งที่ต้องการยกเลิก (1-5): ")) - 1
        col = int(input("กรุณากรอกคอลัมน์ที่นั่งที่ต้องการยกเลิก (1-5): ")) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            cancel_seat(row, col)
        else:
            print("กรุณากรอกแถวและคอลัมน์ในช่วง 1-5!")
    elif choice == "4":
        available_seats()
    elif choice == "5":
        print("ออกจากโปรแกรม")
        break
    else:
        print("เลือกคำสั่งไม่ถูกต้อง!")
