scores = []
# รับคะแนนจากผู้ใช้
for room in range(3):
    print(f"\nEnter scores for Room {room + 1}:")
    room_scores = []
    for student in range(5):
        student_scores = []
        for subject in range(4):
            score = float(input(f"Enter score for Student {student + 1} in Subject {subject + 1}: "))
            student_scores.append(score)
        room_scores.append(student_scores)
    scores.append(room_scores)
# หาห้องที่มีคะแนนเฉลี่ยสูงสุด
max_avg_score = 0
max_avg_room = 0  # เริ่มจากห้องแรก
for room in range(3):
    room_total = sum(sum(scores[room][student]) for student in range(5))
    room_avg = room_total / (5 * 4)
    if room_avg > max_avg_score:
        max_avg_score = room_avg
        max_avg_room = room
print(f"\nRoom {max_avg_room + 1} has the highest average score: {max_avg_score:.2f}")
# หานักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง
for room in range(3):
    max_total_score = sum(scores[room][0])
    max_total_student = 1  # เริ่มจากนักเรียนคนแรก
    for student in range(1, 5):
        student_total = sum(scores[room][student])
        if student_total > max_total_score:
            max_total_score = student_total
            max_total_student = student + 1  # +1 เพื่อให้ตรงกับนักเรียนที่ 1-based index
    print(f"Highest total score for Room {room + 1}: Student {max_total_student} with total score {max_total_score:.2f}")
# แสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง (เกณฑ์ผ่าน >= 50)
passing_count_per_room = [0] * 3
for room in range(3):
    for student in range(5):
        if all(score >= 50 for score in scores[room][student]):
            passing_count_per_room[room] += 1
for room in range(3):
    print(f"\nNumber of students passing all subjects in Room {room + 1}: {passing_count_per_room[room]}")