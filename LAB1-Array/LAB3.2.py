cube = [
    [[56, 49, 67, 57], [57, 58, 55, 50], [60, 51, 63, 56], [64, 65, 49, 56], [48, 56, 59, 50], [50, 61, 54, 56]],
    [[60, 51, 64, 66], [59, 68, 46, 57], [54, 68, 50, 47], [53, 58, 55, 50], [58, 59, 56, 60], [64, 45, 59, 56]],
    [[53, 58, 65, 50], [54, 65, 59, 56], [78, 36, 57, 50], [58, 60, 56, 54], [52, 51, 59, 55], [50, 51, 54, 56]]
]

sc_avg_t1 = sum(sum(row) for row in cube[0]) / (len(cube[0]) * len(cube[0][0]))
sc_avg_t2 = sum(sum(row) for row in cube[1]) / (len(cube[1]) * len(cube[1][0]))
sc_avg_t3 = sum(sum(row) for row in cube[2]) / (len(cube[2]) * len(cube[2][0]))

if sc_avg_t1 > sc_avg_t2 and sc_avg_t1 > sc_avg_t3:
    print("ห้องที่ 1 มีคะแนนเฉลี่ยสูงสุด")
elif sc_avg_t2 > sc_avg_t3:
    print("ห้องที่ 2 มีคะแนนเฉลี่ยสูงสุด")
else:
    print("ห้องที่ 3 มีคะแนนเฉลี่ยสูงสุด")

for room_index, room in enumerate(cube, start=1):
    max_score = 0
    top_student_index = -1
    passed_students = 0
    
    for student_index, scores in enumerate(room):
        total_score = sum(scores)
        
        if total_score > max_score:
            max_score = total_score
            top_student_index = student_index
        

        if all(score >= 50 for score in scores):
            passed_students += 1
    
    print(f"ห้องที่ {room_index}:")
    print(f" - นักเรียนที่ได้คะแนนรวมสูงสุดคือคนที่ {top_student_index + 1} ด้วยคะแนน {max_score}")
    print(f" - จำนวนนักเรียนที่สอบผ่านทุกวิชา: {passed_students}")
