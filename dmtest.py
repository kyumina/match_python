#coding: utf-8

import csv
import random


#問題点
#現在、for~in文でまわすことにより、メモリ使用量が多くなっている。
#重複した単純配列が見られるため完成次第改善。

#mainlist=[name,sex,ysex,yold,ynew,old,Q1~Q15]
#mainlist = [['kyumina',0,1,0,8,15],['RJ',1,0,6,15,9],['unitychan',1,1,3,43,9],['kanten',0,1,0,100,16],['buran',0,1,34,46,15],['man',0,1,0,12,23]]
initlist = []
mainlist = []
boylist = []
girllist = []
#qchoose = [[マッチングする候補],[...]...]
qchoose = []
#manser = [[name,matchname],[name,matchname]...]
manswer = []
#qchooseの中に入れるリストを一時的に保持するリスト
bqchoose = []
#gosalist
gosa = []
#back gosalist
bgosalist = []
#list in dicgosa
zgosa = []
#sort al conpleated gosalist
sgosa = []

alist = []

#csv読み込み
f = open('match.csv', 'rb')
dataReader = csv.reader(f)
for row in dataReader:
    initlist.append(row)
print 'initlist'
print initlist

#int変換
#for count in xrange(len(mainlist)):
#    for snuncount in xrange(len(mainlist[count])):
#        mainlist[count][snuncount] = str(mainlist[count][snuncount])
#        print mainlist[count][snuncount]
for initcount in xrange(len(initlist)):
    bmainlist = []
    bmainlist.append(initlist[initcount][0])
    for snuncount in xrange(len(initlist[initcount])-1):
        bmainlist.append(int(initlist[initcount][snuncount+1]))
    mainlist.append(bmainlist)
#for initcount in xrange(len(initlist)):
#    mainlist.insert(0,initlist[initcount][0])
print 'main'
print mainlist

#性別の分別
for count in xrange(len(mainlist)):
    if mainlist[count][1] == 0:
        boylist.append(mainlist[count])
    elif mainlist[count][1] == 1:
        girllist.append(mainlist[count])

print 'boy'
print boylist
print 'girl'
print girllist

#年齢での分別
for count in xrange(len(mainlist)):
    bqchoose = []
    if mainlist[count][2] == 1:
        for oldcount in xrange(len(girllist)):
            if mainlist[count][3] <= girllist[oldcount][5] and mainlist[count][4] >= girllist[oldcount][5]:
                bqchoose.append(girllist[oldcount])
                #print bqchoose
            else:
                pass
                #print bqchoose

    elif mainlist[count][2] == 0:
        for oldcount in xrange(len(boylist)):
            if mainlist[count][3] <= boylist[oldcount][5] and mainlist[count][4] >= boylist[oldcount][5]:
                bqchoose.append(boylist[oldcount])
                #print bqchoose
            else:
                pass
                #print bqchoose
    #print bqchoose
    qchoose.append(bqchoose)
print "sex&old"
print qchoose

#誤差処理
for countperm in xrange(len(mainlist)):
    bgosalist = []
    for countperso in xrange(len(qchoose[countperm])):
        siguma = 0
        for qcount in xrange(len(mainlist[0])-6):
            siguma += abs(mainlist[countperm][qcount+6] - qchoose[countperm][countperso][qcount+6])
        bgosalist.append(siguma)
        #print"bbgogogosa"
        #print bgosalist
    if len(qchoose[countperm]) == 0:
        bgosalist.append('None')
#    print "bgosa"
#    print bgosalist
    gosa.append(bgosalist)

print 'gosa'
print gosa



#list of dictionary
for countm in xrange(len(mainlist)):
    bzgosalist = []
    bzgosadic = {}
    for countgo in xrange(len(gosa[countm])):
        #print countm
        #print countgo
        #print gosa[countm][countgo]
        #print qchoose[countm][countgo][0]
        if gosa[countm][countgo] == 'None':
            bzgosalist.append('None')
        else:
            bzgosadic.update({gosa[countm][countgo]:qchoose[countm][countgo][0]})
    zgosa.append(bzgosalist)
    zgosa.append(bzgosadic)

while zgosa.count([]) > 0:
    zgosa.remove([])
while zgosa.count({}) > 0:
    zgosa.remove({})

print "zgosa"
print zgosa


# sort of gosa
for countm in xrange(len(mainlist)):
    if gosa[countm][0] == 'None':
        pass
        #sgosa.append(['Nooo'])
    else:
        gosa[countm].sort()
        #print gosa[countm]

print 'sgosa'
print gosa


#zgosa gosa照合
for countm in xrange(len(mainlist)):
    bcgosa = []
    if gosa[countm][0] == 'None':
        if mainlist[countm][2] == 0:
            bcgosa. append(mainlist[countm][0])
            bcgosa.append(boylist[random.randint(0,len(boylist))-1][0])
        elif mainlist[countm][2] == 1:
            bcgosa.append(mainlist[countm][0])
            bcgosa.append(girllist[random.randint(0,len(girllist))-1][0])
    elif gosa[countm][0] == 0:
        if len(gosa[countm]) == 1:
            if mainlist[countm][2] == 0:
                bcgosa. append(mainlist[countm][0])
                bcgosa.append(boylist[random.randint(0,len(boylist))-1][0])
            elif mainlist[countm][2] == 1:
                bcgosa.append(mainlist[countm][0])
                bcgosa.append(girllist[random.randint(0,len(girllist))-1][0])
        else:
            bcgosa.append(mainlist[countm][0])
            bcgosa.append (zgosa[countm][gosa[countm][1]])
    else:
        bcgosa.append(mainlist[countm][0])
        bcgosa.append(zgosa[countm][gosa[countm][0]])
        print zgosa[countm][gosa[countm][0]]
        print gosa[countm][0]
    alist.append(bcgosa)

print alist
