def create_warehouse():
  # สร้าง array 3 มิติเพื่อเก็บข้อมูลคลังสินค้า
  warehouse = [[[0 for _ in range(5)] for _ in range(4)] for _ in range(3)]
  return warehouse

def input_data(warehouse):
  # รับข้อมูลจำนวนสินค้าในแต่ละตำแหน่ง
  for i in range(3):
    print(f"คลังที่ {i+1}")
    for j in range(4):
      for k in range(5):
        warehouse[i][j][k] = int(input(f"ชั้น {j+1} ช่อง {k+1}: "))

def find_busiest_warehouse(warehouse):
  # หาคลังที่มีสินค้ามากที่สุด
  busiest_warehouse = 0
  max_items = 0
  for i in range(3):
    total_items = sum(sum(row) for row in warehouse[i])
    if total_items > max_items:
      max_items = total_items
      busiest_warehouse = i
  return busiest_warehouse + 1

def find_empty_positions(warehouse):
  # หาตำแหน่งที่ว่าง
  empty_positions = []
  for i in range(3):
    for j in range(4):
      for k in range(5):
        if warehouse[i][j][k] == 0:
          empty_positions.append((i+1, j+1, k+1))
  return empty_positions

# สร้างคลังสินค้า
warehouse = create_warehouse()

# รับข้อมูลสินค้า
input_data(warehouse)

# หาคลังที่มีสินค้ามากที่สุด
busiest_warehouse = find_busiest_warehouse(warehouse)
print(f"คลังที่มีสินค้ามากที่สุดคือ คลังที่ {busiest_warehouse}")

# หาตำแหน่งที่ว่าง
empty_positions = find_empty_positions(warehouse)
print("ตำแหน่งที่ว่าง:")
for pos in empty_positions:
  print(f"คลัง {pos[0]}, ชั้น {pos[1]}, ช่อง {pos[2]}")