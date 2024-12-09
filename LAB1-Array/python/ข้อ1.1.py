# สร้าง Array เก็บคะแนนของนักเรียน 5 คน
scores = [75, 82, 90, 60, 88]
# หาค่าเฉลี่ย
average_score = sum(scores) / len(scores)
# หาคะแนนสูงสุดและต่ำสุด
max_score = max(scores)
min_score = min(scores)
# หาจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
above_average_count = sum(1 for score in scores if score > average_score)
# แสดงผลลัพธ์
print(f"ค่าเฉลี่ยของคะแนน: {average_score:.2f}")
print(f"คะแนนสูงสุด: {max_score}")
print(f"คะแนนต่ำสุด: {min_score}")
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {above_average_count}")