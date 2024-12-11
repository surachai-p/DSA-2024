
scores = [
    #A
    [
        [80, 75, 90, 85],
        [85, 90, 88, 87],
        [78, 80, 85, 70],
        [90, 92, 95, 93],
        [70, 65, 60, 72],
    ],
    #B
    [
        [85, 87, 88, 90],
        [80, 70, 75, 85],
        [92, 95, 90, 91],
        [75, 80, 70, 78],
        [88, 90, 85, 92],
    ],
    #C
    [
        [65, 70, 75, 80],
        [60, 62, 55, 58],
        [95, 94, 93, 96],
        [80, 85, 88, 90],
        [70, 68, 65, 75],
    ]
]

# รายชื่อห้องเรียน
room_names = ["ห้อง A", "ห้อง B", "ห้อง C"]

highest_avg_score = 0
best_room_index = 0

for room_index in range(3):
    room_scores = scores[room_index]
    
    # คำนวณคะแนนเฉลี่ยของห้อง
    total_score = 0
    total_students = 0
    for student_scores in room_scores:
        total_score += sum(student_scores)
        total_students += len(student_scores)
    
    avg_score = total_score / total_students
    print(f"คะแนนเฉลี่ยของ {room_names[room_index]}: {avg_score:.2f} คะแนน")
    
    # หานักเรียนที่ได้คะแนนรวมสูงสุดในห้อง
    highest_total_score = 0
    top_student = 0
    for student_index in range(5):
        total = sum(room_scores[student_index])
        if total > highest_total_score:
            highest_total_score = total
            top_student = student_index + 1
    print(f"นักเรียนที่ได้คะแนนรวมสูงสุดใน {room_names[room_index]}: นักเรียนที่ {top_student}")
    
    # นับจำนวนนักเรียนที่สอบผ่านทุกวิชา
    passed_count = 0
    for student_scores in room_scores:
        if all(score >= 50 for score in student_scores):
            passed_count += 1
    print(f"จำนวนนักเรียนที่สอบผ่านทุกวิชาใน {room_names[room_index]}: {passed_count} คน\n")
    
    # คำนวณหาห้องที่มีคะแนนเฉลี่ยสูงสุด
    if avg_score > highest_avg_score:
        highest_avg_score = avg_score
        best_room_index = room_index

# แสดงห้องที่มีคะแนนเฉลี่ยสูงสุด
print(f"ห้องที่มีคะแนนเฉลี่ยสูงสุดคือ {room_names[best_room_index]} ด้วยคะแนนเฉลี่ย {highest_avg_score:.2f} คะแนน")
