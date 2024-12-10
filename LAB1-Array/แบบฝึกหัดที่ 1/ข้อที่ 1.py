#เก็บคะแนนสอบของนักเรียน
scores = [78, 85, 92, 67, 88]

#หาค่าเฉลี่ย
avr_scores = sum(scores) / len(scores)

#หาคะแนนสูงสุด
max_scores = max(scores)

#หาคะแนนต่ำสุด
min_scores = min(scores)

#คนที่ได้คะแนนมากกว่าค่าเฉลี่ย
avr_count = sum(1 for scores in scores if scores > avr_scores)

#แสดงผลลัพธ์
print(f"คะแนนสอบของนักเรียน : {scores}")
print(f"ค่าเฉลี่ย : {avr_scores:.2f}")
print(f"คะแนนสูงสุด : {max_scores}")
print(f"คะแนนต่ำสุด : {min_scores}")
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย : {avr_count}")