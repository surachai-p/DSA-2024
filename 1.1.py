# การสร้าง Array เก็บคะแนนสอบ
import array

# กำหนดคะแนนของนักเรียน 5 คน
scores = array.array('i', [85, 90, 78, 92, 88])  # ใช้ 'i' สำหรับข้อมูลประเภทจำนวนเต็ม

# คำนวณค่าเฉลี่ย
average_score = sum(scores) / len(scores)

# หาคะแนนสูงสุดและต่ำสุด
max_score = max(scores)
min_score = min(scores)

# นับจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
above_average_count = sum(score > average_score for score in scores)

# แสดงผล
print("คะแนนสอบของนักเรียน:", scores.tolist())  # แปลงเป็น list เพื่อแสดงผล
print("ค่าเฉลี่ยคะแนน:", average_score)
print("คะแนนสูงสุด:", max_score)
print("คะแนนต่ำสุด:", min_score)
print("จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย:", above_average_count)
