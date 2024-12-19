import numpy as np

def get_temperature_data():
    """รับข้อมูลอุณหภูมิจากผู้ใช้"""
    num_cities = 3
    num_days = 7
    num_measurements_per_day = 4

    data = np.zeros((num_cities, num_days, num_measurements_per_day))
    for city in range(num_cities):
        for day in range(num_days):
            for measurement in range(num_measurements_per_day):
                temp = float(input(f"Enter temperature for city {city+1}, day {day+1}, measurement {measurement+1}: "))
                data[city, day, measurement] = temp
    return data

def calculate_average_and_max(data):
    """คำนวณค่าเฉลี่ยและค่าสูงสุดของแต่ละเมือง"""
    averages = np.mean(data, axis=(1, 2))
    max_temps = np.max(data, axis=(1, 2))
    max_indices = np.argmax(data, axis=(1, 2))
    return averages, max_temps, max_indices

def print_results(averages, max_temps, max_indices):
    """แสดงผลลัพธ์"""
    for city in range(num_cities):
        print(f"City {city+1}:")
        print(f"  Average temperature: {averages[city]}")
        print(f"  Maximum temperature: {max_temps[city]}")
        # คำนวณวันและเวลาที่อุณหภูมิสูงสุด (ปรับตามรูปแบบที่ต้องการ)
        max_day = max_indices[city] // 4 + 1
        max_measurement = max_indices[city] % 4 + 1
        print(f"  Maximum temperature occurred on day {max_day}, measurement {max_measurement}")

if __name__ == "__main__":
    data = get_temperature_data()
    averages, max_temps, max_indices = calculate_average_and_max(data)
    print_results(averages, max_temps, max_indices)