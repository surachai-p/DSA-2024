#รายการสินค้าทั้งหมด
products = ["น้ำดื่ม", "ขนมปัง", "นม", "แยม"]

#เพิ่มสินค้า
products.append("ข้าวสาร")
print(f"เพิ่มสินค้าเรียบร้อย : {products}")

#ลบสินค้า
products.remove("แยม")
print(f"ลบสินค้าเรียบร้อย : {products}")

#ค้นหาสินค้า
search_item = "น้ำดื่ม"
print(f"พบ '{search_item}'" if search_item in products else f"ไม่พบ '{search_item}'")

#รายการสินค้าทั้งหมด
print(f"รายการสินค้าทั้งหมด : {products}")