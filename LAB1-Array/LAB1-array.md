# ใบงานการทดลอง: การใช้งาน Array ในภาษา Python
## วัตถุประสงค์
1. เพื่อเรียนรู้การสร้างและใช้งาน Array 1 มิติ
2. เพื่อเรียนรู้การสร้างและใช้งาน Array 2 มิติ
3. เพื่อเรียนรู้การสร้างและใช้งาน Array 3 มิติ
4. เพื่อฝึกการประยุกต์ใช้ Array ในการแก้ปัญหาต่างๆ

## อุปกรณ์ที่ใช้
1. เครื่องคอมพิวเตอร์
2. Python 3.x
3. Text Editor หรือ IDE ที่ใช้เขียน Python

## การทดลองที่ 1: Array 1 มิติ
### ขั้นตอนการทดลอง

#### 1.1 การสร้างและแสดงผล Array
```python
# วิธีที่ 1: สร้าง Array แบบกำหนดค่าเริ่มต้น
numbers = [1, 2, 3, 4, 5]
print("Array 1:", numbers)

# วิธีที่ 2: สร้าง Array ว่าง
empty_array = []
print("Array ว่าง:", empty_array)

# วิธีที่ 3: สร้าง Array ด้วย list comprehension
squares = [x**2 for x in range(5)]
print("Array กำลังสอง:", squares)
```

#### 1.2 การเข้าถึงและแก้ไขข้อมูล
```python
fruits = ["แอปเปิล", "กล้วย", "ส้ม", "มะม่วง", "องุ่น"]

# การเข้าถึงข้อมูล
print("ผลไม้ชิ้นแรก:", fruits[0])
print("ผลไม้ชิ้นสุดท้าย:", fruits[-1])
print("ผลไม้ชิ้นที่ 2-4:", fruits[1:4])

# การแก้ไขข้อมูล
fruits[1] = "สตรอเบอร์รี่"
print("Array หลังการแก้ไข:", fruits)
```

#### 1.3 การดำเนินการพื้นฐาน
```python
numbers = [1, 2, 3, 4, 5]

# การเพิ่มข้อมูล
numbers.append(6)
print("หลังจาก append:", numbers)

numbers.insert(0, 0)
print("หลังจาก insert:", numbers)

# การลบข้อมูล
numbers.pop()
print("หลังจาก pop:", numbers)

numbers.remove(3)
print("หลังจาก remove 3:", numbers)

# การค้นหาข้อมูล
print("ตำแหน่งของ 4:", numbers.index(4))
print("จำนวน 2 ในarray:", numbers.count(2))
```

### แบบฝึกหัดที่ 1: Array 1 มิติ

1. จงเขียนโปรแกรมสร้าง Array เก็บคะแนนสอบของนักเรียน 5 คน และ:
   - หาค่าเฉลี่ย
   - หาคะแนนสูงสุดและต่ำสุด
   - แสดงจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
     ![Screenshot 2024-12-04 160827](https://github.com/user-attachments/assets/9d8a539a-eb5e-4605-ae0f-41b5cfa4d571)


2. สร้างโปรแกรมจัดการรายชื่อสินค้าในร้านค้า โดยมีฟังก์ชัน:
   - เพิ่มสินค้าใหม่
   - ลบสินค้าที่หมด
   - ค้นหาสินค้า
   - แสดงรายการสินค้าทั้งหมด
     ![Screenshot 2024-12-08 110024](https://github.com/user-attachments/assets/8af317c1-d144-482a-9a5c-ef85f97aa266)
     ![Screenshot 2024-12-08 110048](https://github.com/user-attachments/assets/adb106fa-7654-42a8-b671-21d9f7590d0a)
     ![Screenshot 2024-12-08 110103](https://github.com/user-attachments/assets/1a24a4c0-9879-465e-880b-680a85ab5224)

## การทดลองที่ 2: Array 2 มิติ
### ขั้นตอนการทดลอง

#### 2.1 การสร้างและแสดงผล Array 2 มิติ
```python
# วิธีที่ 1: สร้างแบบกำหนดค่าโดยตรง
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# วิธีที่ 2: สร้างด้วย list comprehension
matrix2 = [[i+j for j in range(3)] for i in range(3)]

# การแสดงผล
print("Matrix 1:")
for row in matrix:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)
```

#### 2.2 การเข้าถึงและแก้ไขข้อมูล
```python
# การเข้าถึงข้อมูล
print("ข้อมูลแถวที่ 1:", matrix[0])
print("ข้อมูลแถวที่ 2 คอลัมน์ที่ 3:", matrix[1][2])

# การแก้ไขข้อมูล
matrix[1][1] = 10
print("\nMatrix หลังการแก้ไข:")
for row in matrix:
    print(row)

# การแก้ไขทั้งแถว
matrix[0] = [10, 20, 30]
print("\nMatrix หลังการแก้ไขทั้งแถว:")
for row in matrix:
    print(row)
```

#### 2.3 การดำเนินการพื้นฐาน
```python
# การหาผลรวมแต่ละแถว
row_sums = [sum(row) for row in matrix]
print("ผลรวมแต่ละแถว:", row_sums)

# การหาผลรวมแต่ละคอลัมน์
col_sums = [sum(col) for col in zip(*matrix)]
print("ผลรวมแต่ละคอลัมน์:", col_sums)

# การสลับแถว
matrix[0], matrix[1] = matrix[1], matrix[0]
print("\nMatrix หลังการสลับแถว:")
for row in matrix:
    print(row)
```

### แบบฝึกหัดที่ 2: Array 2 มิติ

1. จงเขียนโปรแกรมจัดการคะแนนสอบ:
   - เก็บคะแนนสอบ 3 วิชาของนักเรียน 4 คน
   - คำนวณคะแนนเฉลี่ยของแต่ละวิชา
   - หานักเรียนที่ได้คะแนนรวมสูงสุด
   - แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
     ![Screenshot 2024-12-08 105656](https://github.com/user-attachments/assets/d040a901-41b5-45a8-b7ba-a4af6d63b0eb)
     ![Screenshot 2024-12-08 105724](https://github.com/user-attachments/assets/ecbc1e53-85a8-48ce-aaf0-1ff668ad92c4)
2. สร้างโปรแกรมจัดการที่นั่งในโรงภาพยนตร์:
   - แสดงแผนผังที่นั่ง (ว่าง/จอง)
   - จองที่นั่ง
   - ยกเลิกการจอง
   - แสดงจำนวนที่นั่งว่างทั้งหมด
     ![Screenshot 2024-12-08 120725](https://github.com/user-attachments/assets/0a537af9-c68d-4d1b-969f-59677d80d474)
     ![Screenshot 2024-12-08 120803](https://github.com/user-attachments/assets/9421bf9a-8b74-4ead-aaa7-f7258c891994)
     ![Screenshot 2024-12-08 120917](https://github.com/user-attachments/assets/431e48b1-603f-4609-acff-637d986a88c2)
     ![Screenshot 2024-12-08 121005](https://github.com/user-attachments/assets/ee38500d-669d-4428-ad13-f7e4a626ba02)
     ![Screenshot 2024-12-08 121024](https://github.com/user-attachments/assets/9a398325-7fd5-4f57-8209-db1f23a2e223)

## การทดลองที่ 3: Array 3 มิติ
### ขั้นตอนการทดลอง

#### 3.1 การสร้างและแสดงผล Array 3 มิติ
```python
# วิธีที่ 1: สร้างแบบกำหนดค่าโดยตรง
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# วิธีที่ 2: สร้างด้วย list comprehension
cube2 = [[[k+j+i for k in range(2)] for j in range(2)] for i in range(2)]

# การแสดงผล
print("Cube 1:")
for layer in cube:
    for row in layer:
        print(row)
    print()
```

#### 3.2 การเข้าถึงและแก้ไขข้อมูล
```python
# การเข้าถึงข้อมูล
print("ข้อมูลชั้นที่ 1:", cube[0])
print("ข้อมูลชั้นที่ 1 แถวที่ 2:", cube[0][1])
print("ข้อมูลที่ตำแหน่ง [0][1][0]:", cube[0][1][0])

# การแก้ไขข้อมูล
cube[0][0][0] = 10
print("\nCube หลังการแก้ไข:")
for layer in cube:
    for row in layer:
        print(row)
    print()
```

### แบบฝึกหัดที่ 3: Array 3 มิติ

1. จงเขียนโปรแกรมจัดการข้อมูลอุณหภูมิ:
   - เก็บอุณหภูมิของ 3 เมือง
   - วัด 4 ครั้งต่อวัน
   - เป็นเวลา 7 วัน
   - หาค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
   - หาวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง
     ![Screenshot 2024-12-08 191109](https://github.com/user-attachments/assets/1c06fb5e-3b8d-4625-96fb-0df13e738a4f)
     ![Screenshot 2024-12-08 191124](https://github.com/user-attachments/assets/aa8b58c7-a0ac-4e41-bca6-bacc77d62ce4)
     ![Screenshot 2024-12-08 191138](https://github.com/user-attachments/assets/2a532c48-e7f8-4112-b956-f0f97335569e
     ![Screenshot 2024-12-08 191155](https://github.com/user-attachments/assets/43591d45-8d31-4ab4-946e-5844772cbd0d)
     ![Screenshot 2024-12-08 191209](https://github.com/user-attachments/assets/cb06b418-a8e1-4087-a768-b8aab05f3a20)
     ![Screenshot 2024-12-08 191222](https://github.com/user-attachments/assets/72461037-74c2-4f7b-b023-19b7c0e880ea)

2. เขียนโปรแกรมวิเคราะห์ผลการเรียน:
   - เก็บคะแนนของนักเรียน 3 ห้อง
   - ห้องละ 5 คน
   - สอบ 4 วิชา
   - หาห้องที่มีคะแนนเฉลี่ยสูงสุด
   - หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
   - แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง
     ![Screenshot 2024-12-08 194303](https://github.com/user-attachments/assets/a3282a5f-c190-49bb-9c9b-8b37bc70bc73)
     ![Screenshot 2024-12-08 194317](https://github.com/user-attachments/assets/3e9befc0-0381-48d1-85a2-0985137eb266)
     ![Screenshot 2024-12-08 194334](https://github.com/user-attachments/assets/e6cde836-180d-441a-8433-7ff4906383c9)
     ![Screenshot 2024-12-08 194346](https://github.com/user-attachments/assets/3b01e8ab-687e-4ab5-9b67-22aac332c6bc)
     ![Screenshot 2024-12-08 194407](https://github.com/user-attachments/assets/f2d6fe92-e1bc-42d1-afcf-bd2812efcd63)
     
## การส่งงาน
1. ส่งไฟล์ .py ที่มีโค้ดการทดลองทั้ง 3 ส่วน
2. แสดงผลลัพธ์การทำงานของโปรแกรมในแต่ละการทดลอง
3. ส่งคำตอบของแบบฝึกหัดทั้ง 6 ข้อ พร้อมผลลัพธ์การทำงาน
4. เขียนสรุปสิ่งที่ได้เรียนรู้จากการทดลอง

## เกณฑ์การให้คะแนน
- ความถูกต้องของโค้ด (30%)
- ความครบถ้วนของการทดลอง (20%)
- การทำแบบฝึกหัด (40%)
- การสรุปผลการเรียนรู้ (10%)
