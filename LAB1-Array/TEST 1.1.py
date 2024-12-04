
def analyze_scores():
  """ฟังก์ชันวิเคราะห์คะแนนสอบของนักเรียน 5 คน

  คำนวณค่าเฉลี่ย ค่าสูงสุด ค่าต่ำสุด และจำนวนคนที่ได้คะแนนมากกว่าค่าเฉลี่ย
  """
  scores = []
  for i in range(5):
    score = int(input(f"กรุณากรอกคะแนนสอบของนักเรียนคนที่ {i+1}: "))
    scores.append(score)

  average = sum(scores) / len(scores)

  max_score = max(scores)
  min_score = min(scores)

  above_average = sum(score > average for score in scores)

  print(f"ค่าเฉลี่ยคะแนนสอบ: {average:.2f}")
  print(f"คะแนนสูงสุด: {max_score}")
  print(f"คะแนนต่ำสุด: {min_score}")
  print(f"จำนวนนักเรียนที่ได้คะแนนมากกว่าค่าเฉลี่ย: {above_average} คน")

analyze_scores()