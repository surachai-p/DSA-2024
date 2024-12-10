class CinemaSeatManagement:
    def __init__(self, rows, cols):
        # สร้างแผนผังที่นั่งทั้งหมด โดยเริ่มต้นที่ว่าง
        self.seats = [['ว่าง' for _ in range(cols)] for _ in range(rows)]

    def show_seats(self):
        # แสดงแผนผังที่นั่ง
        for row in self.seats:
            print(" ".join(row))
        print()

    def book_seat(self):
        # ให้ผู้ใช้เลือกที่นั่งที่ต้องการจอง
        self.show_seats()
        try:
            row = int(input("กรุณากรอกหมายเลขแถวที่ต้องการจอง (เริ่มจาก 1): ")) - 1
            col = int(input("กรุณากรอกหมายเลขคอลัมน์ที่ต้องการจอง (เริ่มจาก 1): ")) - 1
            
            if row < 0 or col < 0 or row >= len(self.seats) or col >= len(self.seats[0]):
                print("หมายเลขแถวหรือคอลัมน์ไม่ถูกต้อง โปรดลองใหม่อีกครั้ง\n")
            elif self.seats[row][col] == 'ว่าง':
                self.seats[row][col] = 'จอง'
                print(f"ที่นั่ง {row + 1}-{col + 1} จองเรียบร้อยแล้ว\n")
            else:
                print(f"ที่นั่ง {row + 1}-{col + 1} ถูกจองแล้ว\n")
        except ValueError:
            print("กรุณากรอกหมายเลขที่ถูกต้อง\n")

    def cancel_seat(self):
        # ให้ผู้ใช้เลือกที่นั่งที่ต้องการยกเลิกการจอง
        self.show_seats()
        try:
            row = int(input("กรุณากรอกหมายเลขแถวที่ต้องการยกเลิกการจอง (เริ่มจาก 1): ")) - 1
            col = int(input("กรุณากรอกหมายเลขคอลัมน์ที่ต้องการยกเลิกการจอง (เริ่มจาก 1): ")) - 1
            
            if row < 0 or col < 0 or row >= len(self.seats) or col >= len(self.seats[0]):
                print("หมายเลขแถวหรือคอลัมน์ไม่ถูกต้อง โปรดลองใหม่อีกครั้ง\n")
            elif self.seats[row][col] == 'จอง':
                self.seats[row][col] = 'ว่าง'
                print(f"การจองที่นั่ง {row + 1}-{col + 1} ถูกยกเลิกแล้ว\n")
            else:
                print(f"ที่นั่ง {row + 1}-{col + 1} ยังไม่ได้รับการจอง\n")
        except ValueError:
            print("กรุณากรอกหมายเลขที่ถูกต้อง\n")

    def available_seats(self):
        # แสดงจำนวนที่นั่งว่างทั้งหมด
        available_count = sum(row.count('ว่าง') for row in self.seats)
        print(f"จำนวนที่นั่งว่างทั้งหมด: {available_count}\n")


# สร้างออบเจ็กต์การจัดการที่นั่งในโรงภาพยนตร์
cinema = CinemaSeatManagement(rows=5, cols=5)  # 5 แถว 5 คอลัมน์

# ทำงานในลูปเพื่อให้ผู้ใช้เลือกการทำงาน
while True:
    print("โปรแกรมจัดการที่นั่งในโรงภาพยนตร์")
    print("1. แสดงแผนผังที่นั่ง")
    print("2. จองที่นั่ง")
    print("3. ยกเลิกการจองที่นั่ง")
    print("4. แสดงจำนวนที่นั่งว่าง")
    print("5. ออกจากโปรแกรม")
    try:
        choice = int(input("กรุณาเลือกตัวเลือก (1-5): "))
        
        if choice == 1:
            cinema.show_seats()
        elif choice == 2:
            cinema.book_seat()
        elif choice == 3:
            cinema.cancel_seat()
        elif choice == 4:
            cinema.available_seats()
        elif choice == 5:
            print("ออกจากโปรแกรมแล้ว")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่\n")
    except ValueError:
        print("กรุณากรอกตัวเลขที่ถูกต้อง\n")
