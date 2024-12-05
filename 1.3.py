import array

# ฟังก์ชันรับค่าอุณหภูมิ 24 ชั่วโมง
def input_temperatures():
    """รับค่าอุณหภูมิ 24 ชั่วโมงจากผู้ใช้"""
    temperatures = array.array('f', [])  # ใช้ float ('f') เก็บค่าอุณหภูมิ
    print("กรอกค่าอุณหภูมิ 24 ชั่วโมง (หน่วย: °C):")
    for hour in range(24):
        temp = float(input(f"ชั่วโมงที่ {hour + 1}: "))
        temperatures.append(temp)
    return temperatures

# ฟังก์ชันหาช่วงเวลาที่อุณหภูมิสูงที่สุด
def find_highest_temperature(temperatures):
    """หาค่าอุณหภูมิสูงสุดและช่วงเวลา"""
    max_temp = max(temperatures)
    max_hour = temperatures.index(max_temp)
    return max_temp, max_hour

# ฟังก์ชันหาช่วงเวลาที่อุณหภูมิต่ำที่สุด
def find_lowest_temperature(temperatures):
    """หาค่าอุณหภูมิต่ำสุดและช่วงเวลา"""
    min_temp = min(temperatures)
    min_hour = temperatures.index(min_temp)
    return min_temp, min_hour

# ฟังก์ชันคำนวณค่าเฉลี่ยของอุณหภูมิ
def calculate_average_temperature(temperatures):
    """คำนวณค่าเฉลี่ยของอุณหภูมิ"""
    return sum(temperatures) / len(temperatures)

# โปรแกรมหลัก
def main():
    # รับค่าอุณหภูมิจากผู้ใช้
    temperatures = input_temperatures()

    # วิเคราะห์ข้อมูล
    max_temp, max_hour = find_highest_temperature(temperatures)
    min_temp, min_hour = find_lowest_temperature(temperatures)
    avg_temp = calculate_average_temperature(temperatures)

    # แสดงผล
    print("\n--- รายงานการวิเคราะห์อุณหภูมิ ---")
    print(f"อุณหภูมิสูงสุด: {max_temp:.2f} °C ช่วงเวลา: {max_hour}:00")
    print(f"อุณหภูมิต่ำสุด: {min_temp:.2f} °C ช่วงเวลา: {min_hour}:00")
    print(f"อุณหภูมิเฉลี่ย: {avg_temp:.2f} °C")

# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()
