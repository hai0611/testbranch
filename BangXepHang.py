class SinhVien:
    def __init__(self,hoTen,soBaiDung,soBaiSubmit):
        self.hoTen = hoTen
        self.soBaiDung = soBaiDung
        self.soBaiSubmit = soBaiSubmit
    def __str__(self):
        return f"{self.hoTen} {self.soBaiDung} {self.soBaiSubmit}"
n = int(input())
l = list()
for i in range(0,n):
    x = input()
    [y,z] = [int(x) for x in input().split()]
    l.append(SinhVien(x,y,z))
res = sorted(l,key=lambda x:(-x.soBaiDung,x.soBaiSubmit,x.hoTen))
for i in res:
    print(i)


