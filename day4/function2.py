def create_car(name="제네시스", brand="현대",engine= "휘발유", passengers = 5):
    return {
        "name":name,
        "brand":brand,
        "engine": engine,
        "passengers": passengers
    }

print(create_car(brand="기아", engine="디젤", passengers = 3))