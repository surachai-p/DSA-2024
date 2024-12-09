# เก็บคะแนนสอบของนักเรียน 4 คน ใน 3 วิชา
scores = [
    [45, 57, 83],  # คะแนนของนักเรียนคนที่ 1
    [42, 78, 59],  # คะแนนของนักเรียนคนที่ 2
    [69, 81, 97],  # คะแนนของนักเรียนคนที่ 3
    [75, 84, 68],  # คะแนนของนักเรียนคนที่ 4
]
# คำนวณคะแนนเฉลี่ยของแต่ละวิชา
print("คะแนนเฉลี่ยของแต่ละวิชา:")
subject_count = len(scores[0])
student_count = len(scores)
for subject in range(subject_count):
    total = 0
    for student in range(student_count):
        total += scores[student][subject]
    average = total / student_count
    print(f"วิชา {subject + 1}: {average:.2f}")
# หานักเรียนที่ได้คะแนนรวมสูงสุด
max_total_score = 0
top_student = -1
for student in range(student_count):
    total_score = sum(scores[student])
    if total_score > max_total_score:
        max_total_score = total_score
        top_student = student
print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุดคือ นักเรียนคนที่ {top_student + 1} (คะแนนรวม {max_total_score})")
# แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
print("\nจำนวนนักเรียนที่สอบผ่านในแต่ละวิชา:")
for subject in range(subject_count):
    pass_count = 0
    for student in range(student_count):
        if scores[student][subject] >= 50:
            pass_count += 1
    print(f"วิชา {subject + 1}: {pass_count} คน")
