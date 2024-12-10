import numpy as np

# ฟังก์ชันสำหรับรับคะแนนจากผู้ใช้
def input_scores():
    scores = np.zeros((3, 5, 4))  # Array 3 มิติ: (3 ห้อง, 5 คน, 4 วิชา)
    
    print("กรอกคะแนนของนักเรียน (คะแนนเต็ม 100):")
    for room in range(3):  # แต่ละห้อง
        print(f"\nห้องที่ {room+1}:")
        for student in range(5):  # แต่ละคนในห้อง
            print(f"  นักเรียนคนที่ {student+1}:")
            for subject in range(4):  # คะแนนในแต่ละวิชา
                while True:
                    try:
                        score = float(input(f"    วิชา {subject+1}: "))
                        if 0 <= score <= 100:
                            scores[room, student, subject] = score
                            break
                        else:
                            print("    **กรุณากรอกคะแนนระหว่าง 0 ถึง 100 เท่านั้น**")
                    except ValueError:
                        print("    **กรุณากรอกตัวเลขเท่านั้น**")
    return scores

# ฟังก์ชันสำหรับหาห้องที่มีคะแนนเฉลี่ยสูงสุด
def find_highest_average_room(scores):
    room_averages = scores.mean(axis=(1, 2))  # คำนวณค่าเฉลี่ยของแต่ละห้อง
    max_index = room_averages.argmax()  # ห้องที่มีคะแนนเฉลี่ยสูงสุด
    print(f"\nห้องที่มีคะแนนเฉลี่ยสูงสุดคือ ห้อง {max_index+1} ด้วยค่าเฉลี่ย {room_averages[max_index]:.2f}")

# ฟังก์ชันสำหรับหานักเรียนที่มีคะแนนรวมสูงสุดในแต่ละห้อง
def find_top_student_in_each_room(scores):
    print("\nนักเรียนที่ได้คะแนนรวมสูงสุดในแต่ละห้อง:")
    for room in range(3):
        total_scores = scores[room].sum(axis=1)  # คะแนนรวมของนักเรียนแต่ละคนในห้อง
        max_index = total_scores.argmax()  # นักเรียนที่ได้คะแนนรวมสูงสุดในห้อง
        print(f"  ห้อง {room+1}: นักเรียนคนที่ {max_index+1} ด้วยคะแนนรวม {total_scores[max_index]:.2f}")

# ฟังก์ชันสำหรับแสดงจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง
def count_students_passing_all_subjects(scores):
    print("\nจำนวนนักเรียนที่สอบผ่านทุกวิชาในแต่ละห้อง (คะแนนผ่าน ≥ 50):")
    for room in range(3):
        passing = (scores[room] >= 50).all(axis=1)  # เช็คว่าสอบผ่านทุกวิชาหรือไม่
        print(f"  ห้อง {room+1}: {passing.sum()} คน")

# เริ่มโปรแกรม
scores = input_scores()

# วิเคราะห์ผลการเรียน
find_highest_average_room(scores)
find_top_student_in_each_room(scores)
count_students_passing_all_subjects(scores)
