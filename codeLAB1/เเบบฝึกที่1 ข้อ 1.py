# รับคะแนนสอบจากผู้ใช้
scores = [float(input(f"คะแนนของนักเรียนคนที่ {i+1} (0-100): ")) for i in range(5)]

# ตรวจสอบค่าคะแนนให้อยู่ในช่วง 0-100
if not all(0 <= score <= 100 for score in scores):
    print("กรุณากรอกคะแนนระหว่าง 0-100 เท่านั้น")
else:
    # การคำนวณ
    average = sum(scores) / len(scores)
    max_score, min_score = max(scores), min(scores)
    above_average_count = sum(score > average for score in scores)

    # แสดงผลลัพธ์
    print("\n=== ผลลัพธ์การคำนวณ ===")
    print(f"คะแนนเฉลี่ย: {average:.2f}")
    print(f"คะแนนสูงสุด: {max_score}")
    print(f"คะแนนต่ำสุด: {min_score}")
    print(f"จำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {above_average_count}")
