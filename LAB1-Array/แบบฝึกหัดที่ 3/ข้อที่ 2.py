# สร้างการจัดการผลการเรียน
import random

# สุ่มคะแนนของนักเรียน
scores = [[[random.randint(0, 100) for _ in range(4)] for _ in range(5)] for _ in range(3)]

def calculate_room_average(room_scores):
    """คำนวณคะแนนเฉลี่ยของห้อง"""
    total_score = sum(sum(student_scores) for student_scores in room_scores)
    num_students = len(room_scores) * len(room_scores[0])
    return total_score / num_students

def find_top_student_in_room(room_scores):
    """หานักเรียนที่ได้คะแนนรวมสูงสุดในห้อง"""
    max_score = float('-inf')
    top_student_idx = -1
    for idx, student_scores in enumerate(room_scores):
        total_score = sum(student_scores)
        if total_score > max_score:
            max_score = total_score
            top_student_idx = idx
    return top_student_idx, max_score

def count_passing_students_in_room(room_scores):
    """นับจำนวนคนที่สอบผ่านทุกวิชา (คะแนน >= 50) ในแต่ละห้อง"""
    passing_count = 0
    for student_scores in room_scores:
        if all(score >= 50 for score in student_scores):
            passing_count += 1
    return passing_count

#แสดงผลลัพธ์
best_room_idx = -1
best_room_avg = float('-inf')

for room_idx, room_scores in enumerate(scores, start=1):
    print(f"\nห้อง {room_idx}")
    
    #คะแนนเฉลี่ยของห้อง
    avg_score = calculate_room_average(room_scores)
    print(f"คะแนนเฉลี่ยของห้อง: {avg_score:.2f}")
    
    #นักเรียนที่ได้คะแนนรวมสูงสุด
    top_student_idx, top_score = find_top_student_in_room(room_scores)
    print(f"นักเรียนที่ได้คะแนนรวมสูงสุด: นักเรียน {top_student_idx+1} ได้คะแนนรวม {top_score}")
    
    #จำนวนนักเรียนที่สอบผ่านทุกวิชา
    passing_count = count_passing_students_in_room(room_scores)
    print(f"จำนวนผู้สอบผ่านทุกวิชาในห้อง: {passing_count} คน")
    
    #ห้องที่มีคะแนนเฉลี่ยสูงสุด
    if avg_score > best_room_avg:
        best_room_avg = avg_score
        best_room_idx = room_idx

print(f"\nห้องที่มีคะแนนเฉลี่ยสูงสุดคือห้อง {best_room_idx} ด้วยคะแนนเฉลี่ย {best_room_avg:.2f}")
