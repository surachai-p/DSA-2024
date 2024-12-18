products = ["book", "pen", "computer"]
def add_product(name):
    products.append(name)
    print(f"สินค้า {name} ถูกเพิ่มเข้าไปในรายการแล้ว")
def remove_product(name):
    products.remove(name)
def search_product(name):
    if name in products:
        print(f"พบสินค้า {name} ในรายการ")
    else:
        print(f"ไม่พบสินค้า {name} ในรายการ")
def show_all_product():
    if products:
        print("รายการสินค้าทั้งหมด:")
        for product in products:
            print(product)
    else:
        print("ไม่มีสินค้าในรายการ")
while True:
    print("1.เพิ่มสินค้า \n2.ลบสินค้า \n3.ค้นหาสินค้า \n4.แสดงรายการสินค้า \n5.ออกจากโปรแกรม")
    choice = input("เลือกทำอะไร (1/2/3/4/5): ")
    if choice == "1":
        name = input("เพิ่มสินค้าอะไร : ")
        add_product(name)
    elif choice == "2":
        name = input("ลบสินค้าอะไร : ")
        remove_product(name)
    elif choice == "3":
        name = input("สินค้าที่จะค้นหา : ")
        search_product(name)
    elif choice == "4":
        show_all_product()
    elif choice == "5":
        print("ออกจากโปรแกรม")
        break
    else:
        print("กรุณาเลือกตัวเลือกที่ถูกต้อง")