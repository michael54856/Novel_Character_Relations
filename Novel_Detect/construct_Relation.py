import json

characterAppear = {}
edgeWeight = {} #計算兩兩人物關係的權重
characterValue = {} #計算人物的重要程度
with open("character_list.txt", mode = "r", encoding="utf-8") as file: #先建立人物列表
    for line in file: #每次讀取一行
        characterValue[line.rstrip()] = 0
        characterAppear[line.rstrip()] = False


for num in range(1,41) :
    with open("chapters/ch_" + str(num) + ".txt", mode = "r", encoding="utf-8") as file: #開啟檔案
        for line in file: #每次讀取一行
            s = ""
            for c in line :
                if c == '。': #遇到句號,開始進行關係配對
                    nameList = []
                    for name in characterAppear : #先設為全部沒看過
                        characterAppear[name] = False
                    
                    #處理別名的狀況
                    if "張三豐" in s :
                        characterAppear["張君寶"] = True
                    if "東邪" in s :
                        characterAppear["黃藥師"] = True
                    if "西毒" in s :
                        characterAppear["歐陽鋒"] = True
                    if "南帝" in s  or "一燈大師" in s:
                        characterAppear["段智興"] = True
                    if "北丐" in s :
                        characterAppear["洪七公"] = True
                    if "中神通" in s :
                        characterAppear["王重陽"] = True
                    if "甄志丙" in s :
                        characterAppear["尹志平"] = True
                    if "金輪法王" in s :
                        characterAppear["金輪國師"] = True
                    if "長鬚鬼" in s :
                        characterAppear["樊一翁"] = True
                    
                    for name in characterAppear : #看段落有沒有出現這個角色
                        if name in s :
                            characterAppear[name] = True

                    for name in characterAppear : #有出現過的話就加進list
                        if characterAppear[name] == True :
                            nameList.append(name)

                    for i in range(0,len(nameList)) :
                        for j in range(i+1,len(nameList)):
                            thisEdge = nameList[i]+"_"+nameList[j]
                            if thisEdge in edgeWeight:
                                edgeWeight[thisEdge] += 1
                            else :
                                edgeWeight[thisEdge] = 1
                    
                    for name in nameList :
                        characterValue[name] += len(nameList)-1
                    s = ""
                else :
                    s += c
            
            #最後再檢查一次
            nameList = []
            for name in characterAppear : #先設為全部沒看過
                characterAppear[name] = False
            
            #處理別名的狀況
            if "張三豐" in s :
                characterAppear["張君寶"] = True
            if "東邪" in s :
                characterAppear["黃藥師"] = True
            if "西毒" in s :
                characterAppear["歐陽鋒"] = True
            if "南帝" in s  or "一燈大師" in s:
                characterAppear["段智興"] = True
            if "北丐" in s :
                characterAppear["洪七公"] = True
            if "中神通" in s :
                characterAppear["王重陽"] = True
            if "甄志丙" in s :
                characterAppear["尹志平"] = True
            if "金輪法王" in s :
                characterAppear["金輪國師"] = True
            if "長鬚鬼" in s :
                characterAppear["樊一翁"] = True
            
            for name in characterAppear : #看段落有沒有出現這個角色
                if name in s :
                    characterAppear[name] = True

            for name in characterAppear : #有出現過的話就加進list
                if characterAppear[name] == True :
                    nameList.append(name)

            for i in range(0,len(nameList)) :
                for j in range(i+1,len(nameList)):
                    thisEdge = nameList[i]+"_"+nameList[j]
                    if thisEdge in edgeWeight:
                        edgeWeight[thisEdge] += 1
                    else :
                        edgeWeight[thisEdge] = 1
            
            for name in nameList :
                characterValue[name] += len(nameList)-1

characterValue = dict(sorted(characterValue.items(), reverse=True ,key=lambda item: item[1]))
edgeWeight = dict(sorted(edgeWeight.items(), reverse=True, key=lambda item: item[1]))


idCount = 1
nodeArr = []
linkArr = []
for name in characterValue :
    if characterValue[name] > 0:
        nodeStruct = {}
        nodeStruct["id"] = name
        nodeStruct["val"] = characterValue[name]
        nodeArr.append(nodeStruct)
        idCount += 1

for name in edgeWeight :
    linkStruct = {}
    nodeNames = name.split('_')
    linkStruct["source"] = nodeNames[0]
    linkStruct["target"] = nodeNames[1]
    linkStruct["val"] = edgeWeight[name]
    linkArr.append(linkStruct)

finalObj = {}
finalObj["nodes"] = nodeArr
finalObj["links"] = linkArr

#將內容寫入json
with open("../data.json", mode="w", encoding="utf-8") as myFile:
        json.dump(finalObj, myFile, indent=4, ensure_ascii=False)



