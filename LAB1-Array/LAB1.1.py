students = [49, 52, 54, 56, 58]
avg = sum(students) / len(students)
print(f"คะแนนเฉลี่ย : {avg}")
print(f"คะแนนต่ำสุด : {min(students)}")
print(f"คะแนนสูงสุด : {max(students)}")
count = 0
for score in students:
    if score > avg:
        count += 1
print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย : {count}")