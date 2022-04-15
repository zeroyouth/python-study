car_1 = {
    "name":"부가티",
    "color":"silver",
    "fuel":30,
    "mileage":0,
    "efficiency": 13,
}

def drive(car, miles):
    fuel_usage = int(miles/ car["efficiency"])
    if (fuel_usage == 0):
        fuel_usage = 1
    
    if car["fuel"] < fuel_usage:
        print('연료가 부족합니다.!!!')
        return
    
    car["fuel"] = car["fuel"] - fuel_usage
    car["mileage"] = car["mileage"] + miles
    
    
if __name__ == '__main__':
    drive(car_1, 5000000000)
    print(f"주행거리는 {car_1['mileage']} \
        \n 남은 연료는 {car_1['fuel']} 입니다")
