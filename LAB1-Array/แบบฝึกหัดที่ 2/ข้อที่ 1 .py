#คะแนนสอบของนักเรียน 4 คน
scores = [
    [80, 75, 90],
    [60, 65, 70],
    [85, 95, 100],
    [40, 50, 45]
]

#คะแนนเฉลี่ยแต่ละวิชา
avr_scores = [sum(subject) / len(subject) for subject in zip(*scores)]

#นักเรียนทีไ่ด้คะแนนรวมสูงสุด
total_scores = [sum(student) for student in scores]
highest_score_student = total_scores.index(max(total_scores)) + 1

#จำนวนนักเรียนที่สอบผ่านแต่ละวิชา
passed_student = [sum(1 for score in subject if score >= 50) for subject in zip(*scores)]

#แสดงผลลัพธ์
print("คะแนนสอบของนักเรียน :")
for i, student in enumerate(scores, start = 1):
    print(f"นักเรียน {i} : {student}")

print("\nคะแนนเฉลี่ยของแต่ละวิชา :")
for i,avg in enumerate(avr_scores, start = 1):
    print(f"วิชา {i} : {avg:.2f}")

print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุด : นักเรียน {highest_score_student}")

print("\nจำนวนนักเรียนที่สอบผ่านแต่ละวิชา :")
for i, count in enumerate(passed_student, start = 1):
    print(f"วิชา {i} : {count} คน")