import random

# สร้างคะแนนของนักเรียน (3 ห้อง, 5 คนต่อห้อง, 4 วิชา)
scores = [[[random.randint(0, 100) for _ in range(4)] for _ in range(5)] for _ in range(3)]

# ฟังก์ชันคำนวณค่าเฉลี่ยของห้อง
def calculate_room_average(room_scores):
    return sum(sum(student) for student in room_scores) / (len(room_scores) * len(room_scores[0]))

# ฟังก์ชันหานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
def find_highest_student(room_scores):
    max_total = 0
    max_index = -1
    for i, student_scores in enumerate(room_scores):
        total = sum(student_scores)
        if total > max_total:
            max_total = total
            max_index = i
    return max_index + 1, max_total

# ฟังก์ชันนับนักเรียนที่สอบผ่านทุกวิชา (ผ่าน = คะแนน ≥ 50)
def count_pass_students(room_scores):
    return sum(all(score >= 50 for score in student) for student in room_scores)

# วิเคราะห์ข้อมูล
room_averages = [calculate_room_average(scores[room]) for room in range(3)]
highest_room = room_averages.index(max(room_averages)) + 1

print("\n--- ผลการวิเคราะห์ ---")
print(f"ห้องที่มีคะแนนเฉลี่ยสูงสุด: ห้องที่ {highest_room} (ค่าเฉลี่ย: {max(room_averages):.2f})")

for room in range(3):
    print(f"\nห้องที่ {room + 1}:")
    highest_student, highest_total = find_highest_student(scores[room])
    print(f"- นักเรียนที่ได้คะแนนรวมสูงสุด: คนที่ {highest_student} (คะแนนรวม: {highest_total})")
    pass_students = count_pass_students(scores[room])
    print(f"- จำนวนนักเรียนที่สอบผ่านทุกวิชา: {pass_students} คน")
