# รายชื่อสินค้า
products = []

# ฟังก์ชันจัดการสินค้า
def manage_products(action):
    name = input("กรุณากรอกชื่อสินค้า: ")
    if action == "add":
        if name in products:
            print(f"สินค้า '{name}' มีอยู่แล้ว!")
        else:
            products.append(name)
            print(f"เพิ่มสินค้า '{name}' สำเร็จ!")
    elif action == "remove":
        if name in products:
            products.remove(name)
            print(f"ลบสินค้า '{name}' สำเร็จ!")
        else:
            print(f"สินค้า '{name}' ไม่พบ!")
    elif action == "search":
        print(f"สินค้า '{name}' {'พบในรายการ!' if name in products else 'ไม่พบในรายการ!'}")

# ฟังก์ชันแสดงรายการสินค้า
def display_products():
    print("\nรายการสินค้าทั้งหมด:" if products else "ไม่มีสินค้าในรายการ!")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")

# เมนูหลัก
def main_menu():
    actions = {
        '1': lambda: manage_products("add"),
        '2': lambda: manage_products("remove"),
        '3': lambda: manage_products("search"),
        '4': display_products,
    }
    while True:
        print("\n=== ระบบจัดการสินค้าในร้านค้า ===")
        print("1. เพิ่มสินค้าใหม่\n2. ลบสินค้าที่หมด\n3. ค้นหาสินค้า\n4. แสดงรายการสินค้าทั้งหมด\n5. ออกจากโปรแกรม")
        choice = input("กรุณาเลือกคำสั่ง (1-5): ")
        if choice == '5':
            print("ออกจากโปรแกรมเรียบร้อยแล้ว!")
            break
        actions.get(choice, lambda: print("กรุณาเลือกคำสั่งที่ถูกต้อง!"))()

# เริ่มโปรแกรม
if __name__ == "__main__":
    main_menu()
