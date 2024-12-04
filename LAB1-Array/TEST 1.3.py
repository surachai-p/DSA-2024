def analyze_temperature():
  """
  ฟังก์ชันวิเคราะห์อุณหภูมิประจำวัน

  :return: ไม่มีค่าส่งคืน แต่จะพิมพ์ผลลัพธ์ลงบนหน้าจอ
  """

  # รับค่าอุณหภูมิ 24 ชั่วโมง
  temperatures = []
  for hour in range(24):
    temp = float(input(f"กรุณากรอกอุณหภูมิในชั่วโมงที่ {hour+1}: "))
    temperatures.append(temp)

  # หาช่วงเวลาที่อุณหภูมิสูงสุด
  max_temp = max(temperatures)
  max_hours = [i+1 for i, temp in enumerate(temperatures) if temp == max_temp]
  print(f"อุณหภูมิสูงสุดคือ {max_temp} องศาเซลเซียส ในช่วงเวลา {max_hours}")


  min_temp = min(temperatures)
  min_hours = [i+1 for i, temp in enumerate(temperatures) if temp == min_temp]
  print(f"อุณหภูมิต่ำสุดคือ {min_temp} องศาเซลเซียส ในช่วงเวลา {min_hours}")


  average_temp = sum(temperatures) / len(temperatures)
  print(f"อุณหภูมิเฉลี่ยคือ {average_temp:.2f} องศาเซลเซียส")

# เรียกใช้ฟังก์ชัน
analyze_temperature()