
temperature_data = [
    #A
    [
        [30, 32, 31, 35],
        [28, 29, 30, 32],
        [25, 27, 28, 32],
        [34, 34, 31, 38],
        [31, 28, 32, 33],
        [29, 34, 31, 32],
        [32, 33, 34, 29] 
    ],
    #B
    [
        [25, 26, 27, 28],
        [28, 29, 30, 32],
        [33, 33, 34, 36],
        [29, 37, 39, 36],
        [28, 27, 29, 32],
        [26, 27, 28, 29],
        [32, 34, 33, 35]
    ],
    #C
    [
        [22, 23, 21, 24],
        [26, 28, 27, 29],
        [30, 31, 32, 33],
        [25, 24, 26, 27],
        [28, 29, 30, 31],
        [27, 28, 29, 30],
        [30, 32, 33, 34] 
    ]
]
cities = ["เมือง A", "เมือง B", "เมือง C"]

# ฟังก์ชันในการคำนวณค่าเฉลี่ยอุณหภูมิของเมือง
def calculate_average_temperature(city_data):
    total_temperature = 0
    count = 0
    for day in city_data:
        for temperature in day:
            total_temperature += temperature
            count += 1
    return total_temperature / count

# ฟังก์ชันในการหาวันและเวลาที่อุณหภูมิสูงสุดของเมือง
def find_max_temperature(city_data):
    max_temp = -float('inf')
    max_day = 0
    max_time = 0

    for day_index, day in enumerate(city_data):
        for time_index, temperature in enumerate(day):
            if temperature > max_temp:
                max_temp = temperature
                max_day = day_index + 1
                max_time = time_index + 1
    
    return max_temp, max_day, max_time

for city_index, city in enumerate(cities):
    print(f"ข้อมูลอุณหภูมิของ {city}:")
    
    # คำนวณค่าเฉลี่ยอุณหภูมิ
    avg_temp = calculate_average_temperature(temperature_data[city_index])
    print(f"ค่าเฉลี่ยอุณหภูมิ: {avg_temp:.2f} C")
    
    # หาวันและเวลาที่อุณหภูมิสูงสุด
    max_temp, day, time_slot = find_max_temperature(temperature_data[city_index])
    print(f"อุณหภูมิสูงสุด: {max_temp} C ในวันที่ {day}, เวลา {time_slot}:00 น.\n")
