import numpy as np

# ฟังก์ชันสำหรับรับคะแนนจากผู้ใช้
def input_scores(num_students, num_subjects):
    scores = []
    print("กรอกคะแนนสอบ:")
    for student in range(num_students):
        student_scores = []
        print(f"นักเรียนคนที่ {student + 1}:")
        for subject in range(num_subjects):
            while True:
                try:
                    score = float(input(f"  วิชา {subject + 1}: "))
                    if 0 <= score <= 100:
                        student_scores.append(score)
                        break
                    else:
                        print("  **กรุณากรอกคะแนนระหว่าง 0 ถึง 100 เท่านั้น**")
                except ValueError:
                    print("  **กรุณากรอกตัวเลขเท่านั้น**")
        scores.append(student_scores)
    return np.array(scores)

# จำนวนคนและวิชา
num_students = 4
num_subjects = 3

# รับคะแนนจากผู้ใช้
scores = input_scores(num_students, num_subjects)

# 1. คำนวณคะแนนเฉลี่ยของแต่ละวิชา
print("\nคะแนนเฉลี่ยของแต่ละวิชา:")
subject_averages = scores.mean(axis=0)
for i, avg in enumerate(subject_averages, start=1):
    print(f"วิชา {i}: {avg:.2f}")

# 2. หานักเรียนที่ได้คะแนนรวมสูงสุด
total_scores = scores.sum(axis=1)
top_student_index = total_scores.argmax()
highest_score = total_scores[top_student_index]
print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุดคือ นักเรียนที่ {top_student_index + 1} ด้วยคะแนนรวม {highest_score:.2f}")

# 3. แสดงจำนวนนักเรียนที่สอบผ่านในแต่ละวิชา (คะแนน ≥ 50)
print("\nจำนวนนักเรียนที่สอบผ่านในแต่ละวิชา:")
pass_counts = (scores >= 50).sum(axis=0)
for i, count in enumerate(pass_counts, start=1):
    print(f"วิชา {i}: {count} คน")
