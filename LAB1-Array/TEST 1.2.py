#ข้อที่ 2

products = {}

def add_product():
  product_id = input("กรุณากรอกรหัสสินค้า: ")
  product_name = input("กรุณากรอกชื่อสินค้า: ")
  product_price = float(input("กรุณากรอกราคาสินค้า: "))
  product_quantity = int(input("กรุณากรอกจำนวนสินค้า: "))
  products[product_id] = {'name': product_name,1 'price': product_price, 'quantity': product_quantity}
  print("เพิ่มสินค้าเรียบร้อยแล้ว")

def remove_product():
  product_id = input("กรุณากรอกรหัสสินค้าที่จะลบ: ")
  if product_id in products:
    del products[product_id]
    print("ลบสินค้าเรียบร้อยแล้ว")
  else:
    print("ไม่พบสินค้า")

def search_product():
  search_term = input("กรุณากรอกคำค้นหา (รหัสสินค้าหรือชื่อสินค้า): ")
  found = False
  for product_id, product_info in products.items():
    if search_term in product_id or search_term in product_info['name']:
      print(f"พบสินค้า: {product_info}")
      found = True
  if not found:
    print("ไม่พบสินค้า")

def show_all_products():
  if not products:
    print("ไม่มีสินค้าในรายการ")
  else:
    print("รายการสินค้าทั้งหมด:")
    for product_id, product_info in products.items():
      print(f"รหัสสินค้า: {product_id}")
      print(f"ชื่อสินค้า: {product_info['name']}")
      print(f"ราคา: {product_info['price']} บาท")
      print(f"จำนวนสินค้า: {product_info['quantity']}")
      print("-" * 20)

while True:
  print("\nโปรแกรมจัดการสินค้า")
  print("1. เพิ่มสินค้าใหม่")
  print("2. ลบสินค้าที่หมด")
  print("3. ค้นหาสินค้า")
  print("4. แสดงรายการสินค้าทั้งหมด")
  print("5. ออกจากโปรแกรม")
  
  choice = input("กรุณาเลือกเมนู: ")
  
  if choice == '1':
    add_product()
  elif choice == '2':
    remove_product()
  elif choice == '3':
    search_product()
  elif choice == '4':
    show_all_products()
  elif choice == '5':
    break
  else:
    print("เมนูไม่ถูกต้อง")

    