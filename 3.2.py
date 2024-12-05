import random

# สร้างข้อมูลคะแนนนักเรียน 3 ห้อง, ห้องละ 5 คน, 4 วิชา (สุ่มคะแนน 0-100)
scores = [[[random.randint(0, 100) for _ in range(4)] for _ in range(5)] for _ in range(3)]

# แสดงคะแนนของนักเรียน
print("คะแนนของนักเรียน (ห้อง x คน x วิชา):")
for room_idx, room in enumerate(scores, start=1):
    print(f"ห้องที่ {room_idx}: {room}")

# 1. หาห้องที่มีคะแนนเฉลี่ยสูงสุด
room_averages = []
for room in scores:
    total_room_score = sum(sum(student) for student in room)
    room_avg = total_room_score / (len(room) * len(room[0]))  # หาค่าเฉลี่ย
    room_averages.append(room_avg)

highest_avg_room = room_averages.index(max(room_averages))  # ห้องที่ค่าเฉลี่ยสูงสุด
print(f"\nห้องที่มีคะแนนเฉลี่ยสูงสุดคือ ห้องที่ {highest_avg_room + 1} (คะแนนเฉลี่ย: {room_averages[highest_avg_room]:.2f})")

# 2. หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
for room_idx, room in enumerate(scores, start=1):
    student_totals = [sum(student) for student in room]  # คะแนนรวมของนักเรียนแต่ละคน
    top_student_idx = student_totals.index(max(student_totals))  # นักเรียนที่ได้คะแนนรวมสูงสุด
    print(f"\nนักเรียนที่ได้คะแนนรวมสูงสุดในห้องที่ {room_idx} คือ นักเรียนคนที่ {top_student_idx + 1} (คะแนนรวม: {max(student_totals)})")

# 3. แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง (สมมุติคะแนนผ่าน = 50)
pass_score = 50
for room_idx, room in enumerate(scores, start=1):
    passed_all_subjects = [all(score >= pass_score for score in student) for student in room]  # ตรวจสอบการผ่านทุกวิชา
    num_passed_students = sum(passed_all_subjects)  # จำนวนนักเรียนที่ผ่านทุกวิชา
    print(f"\nจำนวนนักเรียนที่สอบผ่านทุกวิชาในห้องที่ {room_idx}: {num_passed_students} คน")
