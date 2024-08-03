# collection = single "variable" used to store multiple values

# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#List[]

Bikes = ["Royal Enfield", "Honda", "Yamaha", "Ducati", "KTM"]
Bikes2 = ["JAWA", "Suzuki", "Ather", "Kawasaki", "Benling"]

# Bikes.append("pulsar")
# Bikes.insert(2, "TVS")
# Bikes.pop()
# Bikes.remove("Honda")
# Bikes.sort()
# Bikes.reverse()
# Bikes.extend(Bikes2)
# Bikes[0] = "pulsure"
# Bikes.clear()
# Bikes.index("Honda")

# print("Honda" in Bikes)
# print(Bikes[-1])
# print(len(Bikes))
print(Bikes)

#Set{}

fruits = {"apple", "orange", "banana", "coconut", "apple"}

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()

print(fruits)

#Tuple()

cars = ("Maruti", "TATA", "Toyato", "Mahindra", "Hyundai", "Mahindra")

# print(cars.index("TATA"))
# print(cars.count("Mahindra"))

for cars in cars:
     print(cars)
