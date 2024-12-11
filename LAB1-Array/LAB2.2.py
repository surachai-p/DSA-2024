rows = 5
cols = 8
seats = [[0] * cols for _ in range(rows)] 

#แสดงแผนผังที่นั่ง
def display_seats():
    print("\nแผนผังที่นั่ง (0 = ว่าง  1 = จองแล้ว):")
    for row in seats:
        print(" ".join(str(seat) for seat in row))

#จองที่นั่ง
def book_seat():
    try:
        row = int(input("กรุณากรอกหมายเลขแถวที่ต้องการจอง (1-5): ")) - 1
        col = int(input("กรุณากรอกหมายเลขคอลัมน์ที่ต้องการจอง (1-8): ")) - 1
        if seats[row][col] == 1:
            print("ที่นั่งนี้ถูกจองแล้ว, กรุณาเลือกที่นั่งอื่น.")
        else:
            seats[row][col] = 1
            print(f"จองที่นั่งแถว {row+1}, คอลัมน์ {col+1} สำเร็จ!")
    except IndexError:
        print("หมายเลขแถวหรือคอลัมน์ไม่ถูกต้อง.")
    except ValueError:
        print("กรุณากรอกข้อมูลเป็นตัวเลข.")

#ยกเลิกการจอง
def cancel_booking():
    try:
        row = int(input("กรุณากรอกหมายเลขแถวที่ต้องการยกเลิกการจอง (1-5): ")) - 1
        col = int(input("กรุณากรอกหมายเลขคอลัมน์ที่ต้องการยกเลิกการจอง (1-8): ")) - 1
        if seats[row][col] == 0:
            print("ที่นั่งนี้ยังไม่ได้จอง.")
        else:
            seats[row][col] = 0
            print(f"ยกเลิกการจองที่นั่งแถว {row+1}, คอลัมน์ {col+1} สำเร็จ")
    except IndexError:
        print("หมายเลขแถวหรือคอลัมน์ไม่ถูกต้อง.")
    except ValueError:
        print("กรุณากรอกข้อมูลเป็นตัวเลข.")

#แสดงจำนวนที่นั่งว่าง
def count_available_seats():
    available = 0
    for row in seats:
        available += row.count(0)
    print(f"จำนวนที่นั่งว่างทั้งหมด: {available} ที่นั่ง")

def main():
    while True:
        print("\nโปรแกรมจัดการที่นั่งในโรงภาพยนตร์")
        print("1. แสดงแผนผังที่นั่ง")
        print("2. จองที่นั่ง")
        print("3. ยกเลิกการจอง")
        print("4. แสดงจำนวนที่นั่งว่างทั้งหมด")
        print("5. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกตัวเลือก (1-5): ")

        if choice == '1':
            display_seats()
        elif choice == '2':
            book_seat()
        elif choice == '3':
            cancel_booking()
        elif choice == '4':
            count_available_seats()
        elif choice == '5':
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง, กรุณาเลือกใหม่")
main()