class Robot:
    def __init__(self, E, D, N, K):
        self.E = E
        self.D = D
        self.N = N
        self.K = K
    
    def __str__(self):
        return f'E betűk száma: {self.E}\nD betűk száma: {self.D}\nK betűk száma: {self.K}\nN betűk száma: {self.N}'


parancsok = input("Kérem a robot parancsait: ")
while len(parancsok) > 200:
    print("Túl hosszú! (max 200 betű)")
    parancsok = input("Kérem a robot parancsait: ")

stat = {}
stat['E'] = 0
stat['D'] = 0
stat['N'] = 0
stat['K'] = 0

for betu in parancsok:
    if betu in stat.keys():
        stat[betu] += 1

iranyok = Robot(stat['E'], stat['D'], stat['K'], stat['N'])
print(iranyok)

if int(stat['E']) > int(stat['D']):
    stat['E'] = int(stat['E']) - int(stat['D'])
    stat['D'] = 0
else:
    stat['D'] = int(stat['D']) - int(stat['E'])
    stat['E'] = 0

if int(stat['N']) > int(stat['K']):
    stat['N'] = int(stat['N']) - int(stat['K'])
    stat['K'] = 0
else:
    stat['K'] = int(stat['K']) - int(stat['N'])
    stat['N'] = 0

print("Új parancszó:")
for k,v in stat.items():
    for i in range(v):
        print(k, end='')