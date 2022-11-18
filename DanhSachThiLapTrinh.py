class Team:
    def __init__(self, ma, tenTeam, tenTruong):
        self.ma = ma
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong
    def __str__(self):
        return f"{self.tenTeam} {self.tenTruong}"
class ThiSinh:
    def __init__(self, maTS, tenTS, maTeam):
        self.maTS = maTS
        self.tenTS = tenTS
        self.maTeam = maTeam
        for team in listTeam:
            if team.ma == self.maTeam:
                self.team = team
                break
    def __str__(self):
        return f"{self.maTS} {self.tenTS} {self.team}"
soTeam = int(input())
listTeam = []
for i in range(0,soTeam):
    maTeam = "Team{s:2}".format(s = i+1).replace(' ','0')
    listTeam.append(Team(maTeam,input(),input()))
soTS = int(input())
listTS = []
for i in range(0,soTS):
    maTS = "C{s:3}".format(s = i+1).replace(' ','0')
    listTS.append(ThiSinh(maTS,input(),input()))
res = sorted(listTS,key= lambda ts:ts.tenTS)
for i in res:
    print(i)




