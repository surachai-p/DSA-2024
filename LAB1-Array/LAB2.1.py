matrix = [
    ["student1", 56, 43, 67],
    ["student2", 78, 65, 39],
    ["student3", 62, 70, 48],
    ["student4", 39, 68, 82]
]

score_subj1 = [sum(row[1:2]) for row in matrix]
avg_subj1 = sum(score_subj1) / len(score_subj1)
score_subj2 = [sum(row[2:3]) for row in matrix]
avg_subj2 = sum(score_subj2) / len(score_subj2)
score_subj3 = [sum(row[3:]) for row in matrix]
avg_subj3 = sum(score_subj3) / len(score_subj3)
print(f"คะแนนเฉลี่ยของแต่ละวิชา \nวิชาที่ 1 : {avg_subj1} \nวิชาที่ 2 : {avg_subj2} \nวิชาที่ 3 : {avg_subj3} \n")



scores = [sum(row[1:]) for row in matrix]
max_score = max(scores)
max_index = scores.index(max_score)
print(f"นักเรียนที่ได้คะแนนสูงสุดคือ {matrix[max_index][0]} ด้วยคะแนนรวม {max_score} คะแนน\n")

pass_score = 50
num_subj = len(matrix[0]) - 1
num_pass_students = [0] * num_subj
for row in matrix:
    for i in range(1, num_subj + 1):
        if row[i] >= pass_score:
            num_pass_students[i-1] += 1
for i, num_pass in enumerate(num_pass_students):
    print(f"จำนวนนักเรียนที่สอบผ่านวิชาที่ {i+1}: {num_pass} คน")