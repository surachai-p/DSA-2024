products = []
while True:
    print("\n=== ระบบจัดการรายชื่อสินค้าในร้านค้า ===")
    print("1. เพิ่มสินค้าใหม่")
    print("2. ลบสินค้าที่หมด")
    print("3. ค้นหาสินค้า")
    print("4. แสดงรายการสินค้าทั้งหมด")
    print("5. ออกจากโปรแกรม")
    choice = input("เลือกเมนู (1-5): ")
    
    if choice == "1":  # เพิ่มสินค้าใหม่
        product_name = input("กรอกชื่อสินค้าที่ต้องการเพิ่ม: ")
        if product_name in products:
            print(f"สินค้า '{product_name}' มีอยู่ในรายการแล้ว!")
        else:
            products.append(product_name)
            print(f"เพิ่มสินค้า '{product_name}' เรียบร้อยแล้ว!")
    
    elif choice == "2":  # ลบสินค้าที่หมด
        product_name = input("กรอกชื่อสินค้าที่ต้องการลบ: ")
        if product_name in products:
            products.remove(product_name)
            print(f"ลบสินค้า '{product_name}' ออกจากรายการเรียบร้อยแล้ว!")
        else:
            print(f"ไม่พบสินค้า '{product_name}' ในรายการ!")
    elif choice == "3":  # ค้นหาสินค้า
        product_name = input("กรอกชื่อสินค้าที่ต้องการค้นหา: ")
        if product_name in products:
            print(f"พบสินค้า '{product_name}' ในรายการ!")
        else:
            print(f"ไม่พบสินค้า '{product_name}' ในรายการ!")
    elif choice == "4":  # แสดงรายการสินค้าทั้งหมด
        if not products:
            print("ไม่มีสินค้าในรายการ!")
        else:
            print("รายการสินค้าทั้งหมด:")
            for index, product in enumerate(products, start=1):
                print(f"{index}. {product}")
    elif choice == "5":  # ออกจากโปรแกรม
        print("ออกจากโปรแกรมเรียบร้อยแล้ว!")
        break
    else:
        print("กรุณาเลือกเมนูที่ถูกต้อง (1-5)")
