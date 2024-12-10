import numpy as np

# ฟังก์ชันสำหรับรับข้อมูลอุณหภูมิจากผู้ใช้
def input_temperatures():
    temperatures = np.zeros((3, 7, 4))  # สร้าง Array 3 มิติขนาด (3, 7, 4)
    dates = []  # เก็บข้อมูลวันที่
    times = []  # เก็บข้อมูลเวลา

    print("กรอกข้อมูลวันที่และเวลา:")
    for day in range(7):
        date = input(f"  วันที่สำหรับวัน {day+1} (เช่น 2024-12-01): ")
        dates.append(date)

    for time in range(4):
        hour = input(f"  เวลาสำหรับช่วงเวลา {time+1} (เช่น 08:00): ")
        times.append(hour)

    print("\nกรอกข้อมูลอุณหภูมิ:")
    for city in range(3):
        print(f"\nเมืองที่ {city+1}:")
        for day in range(7):
            for time in range(4):
                while True:
                    try:
                        temp = float(input(f"  วันที่ {dates[day]} เวลา {times[time]}: "))
                        temperatures[city, day, time] = temp
                        break
                    except ValueError:
                        print("  **กรุณากรอกข้อมูลเป็นตัวเลข**")
    
    return temperatures, dates, times

# ฟังก์ชันสำหรับคำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
def calculate_averages(temperatures):
    averages = temperatures.mean(axis=(1, 2))  # คำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
    for i, avg in enumerate(averages, start=1):
        print(f"\nค่าเฉลี่ยอุณหภูมิของเมือง {i}: {avg:.2f}°C")

# ฟังก์ชันสำหรับหาวันและเวลาที่อุณหภูมิสูงสุดของแต่ละเมือง
def find_highest_temperature(temperatures, dates, times):
    for city in range(3):
        highest_temp = temperatures[city].max()
        highest_index = np.unravel_index(temperatures[city].argmax(), temperatures[city].shape)
        highest_day = highest_index[0]
        highest_time = highest_index[1]
        print(f"\nเมือง {city+1}:")
        print(f"  อุณหภูมิสูงสุด: {highest_temp}°C")
        print(f"  วันที่ {dates[highest_day]} เวลา {times[highest_time]}")

# รับข้อมูลอุณหภูมิจากผู้ใช้
temperatures, dates, times = input_temperatures()

# คำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
calculate_averages(temperatures)

# หาวันและเวลาที่อุณหภูมิสูงสุดของแต่ละเมือง
find_highest_temperature(temperatures, dates, times)
