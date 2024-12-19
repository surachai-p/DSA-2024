#เก็บคะแนน
scores = [0] * 5

for i in range(5):
    scores[i] = float(input(f"กรุณากรอกคะแนนของนักเรียนคนที่ {i+1}: "))

print(f"\nคะแนนสอบของนักเรียน 5 คน: {scores}")


#คำนวณหาค่าเฉลี่ยคะแนน
total_score = 0
for score in scores:
    total_score += score
average_score = total_score / len(scores)

print(f"ค่าเฉลี่ยของคะแนนนักเรียนทั้ง 5 คน : {average_score:.2f}")


#คำนวณคะแนนสูงสุด ต่ำสุด
max_score = scores[0]
min_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score

print(f"คะแนนสูงสุดของนักเรียน: {max_score}")
print(f"คะแนนต่ำสุดของนักเรียน: {min_score}")


#แสดงจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
above_average_count = 0
for score in scores:
    if score > average_score:
        above_average_count += 1
        
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {above_average_count}")
