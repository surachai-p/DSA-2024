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
   -
   - ![image](https://github.com/user-attachments/assets/09016ee1-db6f-4758-985a-ac8cdd9996c3)


2. สร้างโปรแกรมจัดการรายชื่อสินค้าในร้านค้า โดยมีฟังก์ชัน:
   - เพิ่มสินค้าใหม่
   - ลบสินค้าที่หมด
   - ค้นหาสินค้า
   - แสดงรายการสินค้าทั้งหมด
   - 
     ![image](https://github.com/user-attachments/assets/c203a67f-ffc0-4ee6-a2ef-68a2541a683d)
     
     ![image](https://github.com/user-attachments/assets/a9837d99-eea6-43a5-a668-afc9f2f8b67e)
     
     ![image](https://github.com/user-attachments/assets/9d40d669-910d-4215-83a2-447b2e89f113)
     


3. เขียนโปรแกรมวิเคราะห์อุณหภูมิประจำวัน โดย:
   - รับค่าอุณหภูมิ 24 ชั่วโมง
   - หาช่วงเวลาที่อุณหภูมิสูงที่สุด
   - หาช่วงเวลาที่อุณหภูมิต่ำที่สุด
   - คำนวณอุณหภูมิเฉลี่ย

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
     ![image](https://github.com/user-attachments/assets/1f9aa1b0-1f51-4e96-a713-49b5added68a)
     
     ![image](https://github.com/user-attachments/assets/7376d883-349b-4fe8-8b78-cc849c6b9266)



2. สร้างโปรแกรมจัดการที่นั่งในโรงภาพยนตร์:
   - แสดงแผนผังที่นั่ง (ว่าง/จอง)
   - จองที่นั่ง
   - ยกเลิกการจอง
   - แสดงจำนวนที่นั่งว่างทั้งหมด
![image](https://github.com/user-attachments/assets/5de5172f-3877-470c-aacc-0c912345964c)

![image](https://github.com/user-attachments/assets/5429ae62-f43b-457e-9919-1c80ce8da709)

![image](https://github.com/user-attachments/assets/99cfa107-1293-4985-8fb4-66dc58c7a95c)

![image](https://github.com/user-attachments/assets/c0a8b1a3-7155-44b6-9121-0feb90a9df8f)




3. เขียนโปรแกรมวิเคราะห์ยอดขาย:
   - เก็บยอดขายของพนักงาน 5 คน ในแต่ละวันของสัปดาห์
   - หาพนักงานที่มียอดขายสูงสุดในแต่ละวัน
   - หาวันที่มียอดขายรวมสูงสุด
   - คำนวณยอดขายเฉลี่ยของแต่ละพนักงาน

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
   -
   - ![image](https://github.com/user-attachments/assets/d15bfb92-9d7c-4586-851f-e32835451503)
   - 
      ![image](https://github.com/user-attachments/assets/e8a332a9-9847-4b12-be25-c9f97c4aecb8)


3. สร้างโปรแกรมจัดการคลังสินค้า:
   - มี 3 คลัง
   - แต่ละคลังมี 4 ชั้น
   - แต่ละชั้นมี 5 ช่อง
   - บันทึกจำนวนสินค้าในแต่ละตำแหน่ง
   - หาคลังที่มีสินค้ามากที่สุด
   - หาตำแหน่งที่ว่าง (จำนวนสินค้า = 0)
   - ![image](https://github.com/user-attachments/assets/b82569dc-8e20-463c-9647-f37e860fc754)
   - 
   - ![image](https://github.com/user-attachments/assets/e2cbec9a-4fd4-4aea-8a7d-cd40a32c26b9)



4. เขียนโปรแกรมวิเคราะห์ผลการเรียน:
   - เก็บคะแนนของนักเรียน 3 ห้อง
   - ห้องละ 5 คน
   - สอบ 4 วิชา
   - หาห้องที่มีคะแนนเฉลี่ยสูงสุด
   - หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
   - แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง

## การส่งงาน
1. ส่งไฟล์ .py ที่มีโค้ดการทดลองทั้ง 3 ส่วน
2. แสดงผลลัพธ์การทำงานของโปรแกรมในแต่ละการทดลอง
3. ส่งคำตอบของแบบฝึกหัดทั้ง 9 ข้อ พร้อมผลลัพธ์การทำงาน
4. เขียนสรุปสิ่งที่ได้เรียนรู้จากการทดลอง

## เกณฑ์การให้คะแนน
- ความถูกต้องของโค้ด (30%)
- ความครบถ้วนของการทดลอง (20%)
- การทำแบบฝึกหัด (40%)
- การสรุปผลการเรียนรู้ (10%)
