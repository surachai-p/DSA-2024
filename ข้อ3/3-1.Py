import random

# สร้างข้อมูลอุณหภูมิ 3 มิติ (3 เมือง, 7 วัน, 4 ครั้งต่อวัน)
temperatures = [[[random.randint(15, 40) for _ in range(4)] for _ in range(7)] for _ in range(3)]

# ฟังก์ชันคำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
def calculate_average(city_temps):
    return sum(sum(day) for day in city_temps) / (len(city_temps) * len(city_temps[0]))

# ฟังก์ชันหาวันและเวลาที่อุณหภูมิสูงที่สุดของแต่ละเมือง
def find_highest_temperature(city_temps):
    max_temp = float('-inf')
    max_day, max_time = -1, -1
    for day in range(len(city_temps)):
        for time in range(len(city_temps[day])):
            if city_temps[day][time] > max_temp:
                max_temp = city_temps[day][time]
                max_day, max_time = day + 1, time + 1
    return max_temp, max_day, max_time

# แสดงผลลัพธ์
for city in range(3):
    avg_temp = calculate_average(temperatures[city])
    max_temp, max_day, max_time = find_highest_temperature(temperatures[city])
    print(f"\nเมืองที่ {city + 1}:")
    print(f"- ค่าเฉลี่ยอุณหภูมิ: {avg_temp:.2f} °C")
    print(f"- อุณหภูมิสูงสุด: {max_temp} °C (วันที่ {max_day}, เวลา {max_time})")
