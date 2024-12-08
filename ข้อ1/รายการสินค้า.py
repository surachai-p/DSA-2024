Products = ["Clock", "Pen", "Table", "Phone", "Botton"]

# การเพิ่มข้อมูล
Products.append("Computer")
print("หลังจาก append:", Products)

Products.insert(1, "Computer")
print("หลังจาก insert:", Products)

# การลบข้อมูล
Products.pop()
print("หลังจาก pop:", Products)

Products.remove("Botton")
print("หลังจาก remove :", Products)

# การค้นหาข้อมูล
print("ค้นหา 'Phone' :", Products.index("Phone"))
# นับจำนวนครั้งที่ของ "Pen" ปรากฏในรายการ
print("จำนวน 'Pen' ใน array:", Products.count("Pen"))
