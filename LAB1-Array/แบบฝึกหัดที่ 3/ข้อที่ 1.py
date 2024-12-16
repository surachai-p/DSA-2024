#สร้างการจัดการอุณหภูมิ
import random

#ข้อมูลอุณหภูมิ
temperatures = [[[random.randint(50, 70) for _ in range(7)] for _ in range(4)] for _ in range(3)]

def calculate_city_average(city_temps):
    """คำนวณค่าเฉลี่ยของเมือง"""
    total_temp = sum(sum(day) for day in city_temps)
    num_readings = len(city_temps) * len(city_temps[0])
    return total_temp / num_readings

def find_max_temp(city_temps):
    """หาวันและเวลาที่อุณหภูมิสูงที่สุด"""
    max_temp = float('-inf')
    max_time = (0, 0)  # (ช่วงเวลา, วัน)
    for time_idx, day_temps in enumerate(city_temps):
        for day_idx, temp in enumerate(day_temps):
            if temp > max_temp:
                max_temp = temp
                max_time = (time_idx, day_idx)
    return max_temp, max_time

# แสดงผลลัพธ์
for city_idx, city_temps in enumerate(temperatures, start = 1):
    print(f"\nเมือง {city_idx}")
    
    # คำนวณค่าเฉลี่ย
    avg_temp = calculate_city_average(city_temps)
    print(f"ค่าเฉลี่ยอุณหภูมิ : {avg_temp:.2f} °C")
    
    # หาวันและเวลาที่อุณหภูมิสูงที่สุด
    max_temp, (max_time, max_day) = find_max_temp(city_temps)
    print(f"อุณหภูมิสูงสุด : {max_temp} °C (ช่วงเวลา {max_time + 1}, วัน {max_day + 1})")