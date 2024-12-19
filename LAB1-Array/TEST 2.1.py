def main():
    # กำหนดขนาดของ array 2 มิติ
    num_students = 4
    num_subjects = 3

    # สร้าง array 2 มิติเพื่อเก็บคะแนน
    scores = []
    for i in range(num_students):
        student_scores = []
        for j in range(num_subjects):
            score = float(input(f"ป้อนคะแนนวิชาที่ {j+1} ของนักเรียนที่ {i+1}: "))
            student_scores.append(score)
        scores.append(student_scores)

    # คำนวณคะแนนเฉลี่ยของแต่ละวิชา
    subject_averages = []
    for j in range(num_subjects):
        subject_total = 0
        for i in range(num_students):
            subject_total += scores[i][j]
        subject_average = subject_total / num_students
        subject_averages.append(subject_average)
        print(f"คะแนนเฉลี่ยของวิชาที่ {j+1}: {subject_average:.2f}")

    # หานักเรียนที่ได้คะแนนรวมสูงสุด
    max_total_score = 0
    max_student_index = -1
    for i in range(num_students):
        total_score = sum(scores[i])
        if total_score > max_total_score:
            max_total_score = total_score
            max_student_index = i
    print(f"นักเรียนที่ {max_student_index+1} ได้คะแนนรวมสูงสุด: {max_total_score:.2f}")

    # นับจำนวนนักเรียนที่สอบผ่านแต่ละวิชา
    passing_scores = 50
    for j in range(num_subjects):
        num_passed = 0
        for i in range(num_students):
            if scores[i][j] >= passing_scores:
                num_passed += 1
        print(f"จำนวนนักเรียนที่สอบผ่านวิชาที่ {j+1}: {num_passed} คน")

if __name__ == "__main__":
    main()