table_status = [
    ["ว่าง", "ไม่ว่าง", "ว่าง",],
    ["ว่าง", "ว่าง", "ไม่ว่าง",],
    ["ไม่ว่าง", "ไม่ว่าง", "ว่าง",]
]
table_sit = [
    ["1", "2", "3",],
    ["4", "5", "6",],
    ["7", "8", "9",]
]


def show_table_status():
    print("\n:แผนผังที่นั่ง")
    for row in table_status:
        print(row)

def choice_table_sit(choice_sit):
        if choice_sit == "1":
            chack_sit = table_status[0][0]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[0][0] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "2":
            chack_sit = table_status[0][1]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[0][1] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "3":
            chack_sit = table_status[0][2]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[0][2] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "4":
            chack_sit = table_status[1][0]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[1][0] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "5":
            chack_sit = table_status[1][1]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[1][1] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "6":
            chack_sit = table_status[1][2]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[1][2] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "7":
            chack_sit = table_status[2][0]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[2][0] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "8":
            chack_sit = table_status[2][1]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[2][1] = "ไม่ว่าง"
                print("จองสำเร็จ")
        elif choice_sit == "9":
            chack_sit = table_status[2][2]
            if chack_sit == "ไม่ว่าง":
                print("ที่นั่งไม่ว่าง")
            else:
                table_status[2][2] = "ไม่ว่าง"
                print("จองสำเร็จ")
        else:
            print("กรุณาเลือกตัวเลือกที่ถูกต้อง")

def calcel_sit(choice_sit):
    if choice_sit == "1":
        chack_sit = table_status[0][0]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[0][0] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "2":
        chack_sit = table_status[0][1]
        if chack_sit == "ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[0][1] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "3":
        chack_sit = table_status[0][2]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[0][2] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "4":
        chack_sit = table_status[1][0]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[1][0] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "5":
        chack_sit = table_status[1][1]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[1][1] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "6":
        chack_sit = table_status[1][2]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[1][2] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "7":
        chack_sit = table_status[2][0]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[2][0] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "8":
        chack_sit = table_status[2][1]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[2][1] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    elif choice_sit == "9":
        chack_sit = table_status[2][2]
        if chack_sit == "ไม่ว่าง":
            print("ที่นั่งนี้ว่างอยู่แล้ว")
        else:
            table_status[2][2] = "ว่าง"
            print("ยกเลิกสำเร็จ")
    else:
        print("กรุณาเลือกตัวเลือกที่ถูกต้อง")

def count_sit():
    count_s = 0
    for row in table_status:
        for status in row:
            if status == "ว่าง":
                count_s += 1
    print(f"จำนวนที่นั่งว่างทั้งหมด {count_s}")
            

while True:
    print("\n1.แสดงแผนผังที่นั่ง \n2.จองที่นั่ง \n3.ยกเลิกการจอง \n4.แสดงจำนวนที่นั่งว่างทั้งหมด \n5.ออกจากโปรแกรม")
    choice = input("เลือกทำอะไร (1/2/3/4/5): ")
    if choice == "1":
        show_table_status()
    elif choice == "2":
        print("\n:แผนผังที่นั่ง")
        for row in table_sit:
            print(row)
        choice_sit = input("เลือกที่นั่ง (1/2/3/4/5/6/7/8/9): ")
        choice_table_sit(choice_sit)
    elif choice == "3":
        print("\n:แผนผังที่นั่ง")
        for row in table_sit:
            print(row)
        choice_sit = input("เลือกที่นั่ง (1/2/3/4/5/6/7/8/9): ")
        calcel_sit(choice_sit)
    elif choice == "4":
        count_sit()
    elif choice == "5":
        print("ออกจากโปรแกรม")
        break
    else:
        print("กรุณาเลือกตัวเลือกที่ถูกต้อง")