#coding: utf-8


#問題点
#現在、for~in文でまわすことにより、メモリ使用量が多くなっている。
#二つ目にオブジェクト指向ではない問題が発生している。

#mainlist=[name,sex,ysex,yold,ynew,old,Q1~Q15]
mainlist = [['kyumina',0,1,0,8,15],['RJ',1,0,6,15,9],['unitychan',1,1,3,43,9],['kanten',0,1,0,100,16],['buran',0,1,34,46,15],['man',0,1,0,12,23]]
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
bgosa = []

#性別の分別
for count in xrange(len(mainlist)):
    if mainlist[count][1] == 0:
        boylist.append(mainlist[count])
    elif mainlist[count][1] == 1:
        girllist.append(mainlist[count])

print boylist
print girllist

#年齢での分別
for count in xrange(len(mainlist)):
    bqchoose = []
    if mainlist[count][2] == 0:
        for oldcount in xrange(len(girllist)):
            if mainlist[count][3] <= girllist[oldcount][5] and mainlist[count][4] >= girllist[oldcount][5]:
                bqchoose.append(girllist[oldcount])
                #マッチング処理
                #for mcount in xrange(len(qchoose)):
                    #gosa = |mainlist[count][qcount]
                #print bqchoose
            else:
                pass
#bqchoose.append(None)
                #print bqchoose

    if mainlist[count][2] == 1:
        for oldcount in xrange(len(boylist)):
            if mainlist[count][3] <= boylist[oldcount][5] and mainlist[count][4] >= boylist[oldcount][5]:
                bqchoose.append(boylist[oldcount])
                #print bqchoose
            else:
                pass
#bqchoose.append(None)
                #print bqchoose
    qchoose.append(bqchoose)

print qchoose

#本命のマッチング
for count in xrange(len(mainlist)):
    for bmcount in xrange(len(qchoose):
            if len(qchoose[bmcount]) != 0:
                for obmcount in xrange(len(qchoose[bmcount])):
                siguma = 0
                    for qcount in xrange(5,20):
                        siguma += abs(mainlist[count][qcount]- qchoose[bmcount][obmcount][qcount])
                bgosa.append(siguma)

            else:
                bgosa.append('None')

            gosa.append(bgosa)

print gosa

#match your human
for gcount in xrange(len(gosa)):
    for gnucount in xrange(len(gosa[gcount])):
        
