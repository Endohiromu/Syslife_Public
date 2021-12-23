class SeizaRank:
    seizaList = ['牡牛座', '山羊座', 'うお座', '乙女座', 'ふたご座', '天秤座', '獅子座', '水瓶座', '蠍座', '蟹座', 'いて座', '牡羊座']
    ranksList =  [[]]
    
    def getRank(rankList):
        for i in rankList:
            num = self.seizaList.index( rankList[i] )
            self.ranksList[i].append(num)

    def avgRank():
        for i in range(12):
            print(self.rankList[i].average())

