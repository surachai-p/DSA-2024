# สร้าง Array เก็บคะแนนสอบของนักเรียน 5 คน
scores = [78, 85, 62, 90, 70]

# หาค่าเฉลี่ย
average_score = sum(scores) / len(scores)

# หาคะแนนสูงสุดและต่ำสุด
max_score = max(scores)
min_score = min(scores)

# หาจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
above_average_count = len([score for score in scores if score > average_score])

# แสดงผลลัพธ์
print("คะแนนนักเรียน:", scores)
print(f"ค่าเฉลี่ย: {average_score:.2f}")
print(f"คะแนนสูงสุด: {max_score}")
print(f"คะแนนต่ำสุด: {min_score}")
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {above_average_count}")
