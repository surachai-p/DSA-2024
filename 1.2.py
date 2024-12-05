products = []  # รายการสินค้า

while True:
    print("\n1. เพิ่มสินค้าใหม่\n2. ลบสินค้าที่หมด\n3. ค้นหาสินค้า\n4. แสดงรายการสินค้าทั้งหมด\n5. ออก")
    choice = input("เลือกคำสั่ง: ")

    if choice == "1":
        products.append(input("ชื่อสินค้า: "))
        print("เพิ่มสินค้าแล้ว!")
    elif choice == "2":
        product = input("ชื่อสินค้าที่ต้องการลบ: ")
        if product in products:
            products.remove(product)
            print("ลบสินค้าแล้ว!")
        else:
            print("ไม่พบสินค้า!")
    elif choice == "3":
        product = input("ชื่อสินค้าที่ต้องการค้นหา: ")
        print(f"พบสินค้า '{product}'!" if product in products else "ไม่พบสินค้า!")
    elif choice == "4":
        print("รายการสินค้าทั้งหมด:", ", ".join(products) if products else "ไม่มีสินค้า")
    elif choice == "5":
        print("ออกจากโปรแกรม")
        break
    else:
        print("เลือกคำสั่งไม่ถูกต้อง!")

