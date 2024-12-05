# เก็บคะแนนสอบ 3 วิชาของนักเรียน 4 คน (2 มิติ: นักเรียน x วิชา)
scores = [
    [45, 60, 75],  # คะแนนของนักเรียนคนที่ 1
    [80, 55, 90],  # คะแนนของนักเรียนคนที่ 2
    [60, 70, 65],  # คะแนนของนักเรียนคนที่ 3
    [95, 85, 88]   # คะแนนของนักเรียนคนที่ 4
]

# ฟังก์ชันคำนวณคะแนนเฉลี่ยของแต่ละวิชา
def average_per_subject():
    averages = []
    for i in range(3):  # สำหรับ 3 วิชา
        total = sum(scores[j][i] for j in range(4))  # หาผลรวมคะแนนของแต่ละวิชา
        averages.append(total / 4)  # คำนวณเฉลี่ย
    return averages

# ฟังก์ชันหานักเรียนที่ได้คะแนนรวมสูงสุด
def highest_total_score():
    total_scores = [sum(student) for student in scores]  # คำนวณคะแนนรวมของแต่ละนักเรียน
    max_score = max(total_scores)  # หาคะแนนรวมสูงสุด
    student_index = total_scores.index(max_score) + 1  # หานักเรียนที่ได้คะแนนรวมสูงสุด (บวก 1 เพราะเริ่มจาก 0)
    return student_index, max_score

# ฟังก์ชันแสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา (คะแนน ≥ 50)
def passed_count():
    passed = [0, 0, 0]  # เก็บจำนวนคนที่สอบผ่านในแต่ละวิชา
    for i in range(3):  # สำหรับ 3 วิชา
        passed[i] = sum(1 for j in range(4) if scores[j][i] >= 50)  # นับนักเรียนที่ได้คะแนน ≥ 50
    return passed

# แสดงผลลัพธ์
def display_results():
    # คำนวณคะแนนเฉลี่ยของแต่ละวิชา
    averages = average_per_subject()
    print("\nคะแนนเฉลี่ยของแต่ละวิชา:")
    for i in range(3):
        print(f"วิชา {i+1}: {averages[i]:.2f}")

    # หานักเรียนที่ได้คะแนนรวมสูงสุด
    student, max_score = highest_total_score()
    print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียน {student} ได้คะแนนรวม {max_score}")

    # แสดงจำนวนนักเรียนที่สอบผ่านแต่ละวิชา
    passed = passed_count()
    print("\nจำนวนผู้สอบผ่านแต่ละวิชา (คะแนน ≥ 50):")
    for i in range(3):
        print(f"วิชา {i+1}: {passed[i]} คน")

# เรียกใช้งาน
display_results()
