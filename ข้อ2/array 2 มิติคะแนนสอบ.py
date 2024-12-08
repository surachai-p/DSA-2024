# เก็บคะแนนสอบ 3 วิชาของนักเรียน 4 คน (ในรูปแบบ Array 2 มิติ)
scores = [
    [60, 70, 80],  # คะแนนของนักเรียนคนที่ 1
    [45, 55, 65],  # คะแนนของนักเรียนคนที่ 2
    [50, 60, 40],  # คะแนนของนักเรียนคนที่ 3
    [75, 85, 90]   # คะแนนของนักเรียนคนที่ 4
]

# 1. คำนวณคะแนนเฉลี่ยของแต่ละวิชา
num_students = len(scores)  # จำนวนแถวนักเรียน
num_subjects = len(scores[0])  # จำนวนวิชา
subject_averages = [sum(subject) / num_students for subject in zip(*scores)]

# 2. หานักเรียนที่ได้คะแนนรวมสูงสุด
total_scores = [sum(student) for student in scores]  # คำนวณคะแนนรวมของแต่ละคน
max_score_index = total_scores.index(max(total_scores))  # หาตำแหน่งของคะแนนรวมสูงสุด

# 3. แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนนผ่าน ≥ 50)
pass_count = [sum(1 for student in scores if student[i] >= 50) for i in range(num_subjects)]

# แสดงผลลัพธ์
print("คะแนนสอบ:")
for i, student in enumerate(scores, start=1):
    print(f"นักเรียนคนที่ {i}: {student}")

print("\nคะแนนเฉลี่ยของแต่ละวิชา:", [f"{avg:.2f}" for avg in subject_averages])
print(f"นักเรียนที่ได้คะแนนรวมสูงสุด: คนที่ {max_score_index + 1} (คะแนนรวม: {max(total_scores)})")
for i, count in enumerate(pass_count, start=1):
    print(f"จำนวนนักเรียนที่สอบผ่านวิชาที่ {i}: {count} คน")
