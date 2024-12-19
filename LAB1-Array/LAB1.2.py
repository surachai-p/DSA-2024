#สร้างโปรแกรมจัดการรายชื่อสินค้าในร้านค้า โดยมีฟังก์ชัน

products = []

#เพิ่มสินค้าใหม่
def add_product():
    name = input("กรุณากรอกชื่อสินค้าที่จะเพิ่ม : ")
    products.append(name)

    print(f"สินค้าชื่อ '{name}' ถูกเพิ่มเรียบร้อย")


#ลบสินค้าที่หมด
def remove_out_of_stock():
    name = input("กรุณากรอกชื่อสินค้าที่จะลบ (สินค้าที่หมด): ")
    if name in products:
        products.remove(name)
        print(f"'{name}' ถูกลบเรียบร้อย")
    else:
        print(f"ไม่พบ '{name}' ในรายการสินค้า")

#ค้นหาสินค้า
def search_product():
    name = input("กรุณากรอกชื่อสินค้าที่ต้องการค้นหา : ")
    if name in products:
        print(f"พบสินค้าที่ชื่อ '{name}' ในร้านค้า")
    else:
        print(f"ไม่พบสินค้าที่ชื่อ '{name}' ในร้านค้า")

# ฟังก์ชันแสดงรายการสินค้าทั้งหมด
def display_products():
    if len(products) > 0:
        print("รายการสินค้าทั้งหมด:")
        for product in products:
            print(f"- {product}")
    else:
        print("ไม่มีสินค้าภายในร้านค้า")


def main():
    while True:
        print("\n โปรแกรมจัดการร้านค้า")
        print("1. เพิ่มสินค้าใหม่")
        print("2. ลบสินค้าที่หมด")
        print("3. ค้นหาสินค้า")
        print("4. แสดงรายการสินค้าทั้งหมด")
        print("5. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกตัวเลือก 1-5 : ")

        if choice == '1':
            add_product ()
        elif choice == '2':
            remove_out_of_stock ()
        elif choice == '3':
            search_product ()
        elif choice == '4':
            display_products ()
        elif choice == '5':
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง, กรุณาเลือกตัวเลือก 1-5 ")        
main()