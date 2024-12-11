# ข้อมูลอุณหภูมิ 3 มิติ (3 เมือง, 7 วัน, 4 ครั้งที่วัด)
temperatures = [
    [[25, 28, 31, 29], [28, 29, 30, 38], [33, 34, 35, 32], [30, 30, 29, 30], [29, 28, 30, 31], [32, 33, 34, 31], [31, 30, 32, 33]],
    [[25, 27, 28, 26], [24, 25, 26, 27], [28, 29, 28, 30], [26, 27, 28, 29], [27, 26, 25, 26], [28, 29, 30, 28], [27, 28, 29, 27]],
    [[35, 36, 37, 34], [33, 32, 31, 30], [37, 38, 39, 36], [34, 35, 34, 33], [33, 32, 31, 30], [36, 37, 38, 36], [35, 34, 33, 34]]
]

# ฟังก์ชันคำนวณค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
def calc_average(temps):
    total_temp = 0
    count = 0
    for day in temps:
        for time in day:
            total_temp += time
            count += 1
    return total_temp / count

# ฟังก์ชันหาวันและเวลาที่อุณหภูมิสูงสุด
def find_max_day_time(temps):
    max_temp = temps[0][0][0]
    max_day = 0
    max_time = 0
    for day in range(len(temps)):
        for time in range(len(temps[day])):
            for reading in range(len(temps[day][time])):
                if temps[day][time][reading] > max_temp:
                    max_temp = temps[day][time][reading]
                    max_day = day
                    max_time = time
    return max_temp, max_day +1, max_time +1

#ค่าเฉลี่ยอุณหภูมิของแต่ละเมือง
for i in range(3):
    avg_temp = calc_average(temperatures[i])
    print(f"ค่าเฉลี่ยอุณหภูมิของเมืองที่ {i+1}: {avg_temp:.2f} องศาเซลเซียส")

#หาวันและเวลาที่อุณหภูมิสูงสุดของแต่ละเมือง
for i in range(3):
    max_temp, day, time = find_max_day_time(temperatures[i])
    print(f"\nเมืองที่ {i+1} อุณหภูมิสูงสุด {max_temp} องศาเซลเซียส")
    print(f"วัน: {day} เวลา: {time} (ครั้งที่วัด)")
