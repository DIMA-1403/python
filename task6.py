FLOORS = 9
FLATS = 4

for i in range(100):
    n=i//FLATS
    entrance =i//(FLATS*FLOORS)
    floor=n-entrance*FLOORS
    print(i+1,floor + 1, entrance + 1)
