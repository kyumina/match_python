#coding: utf-8

import csv
import os
import random
import pygame
import sys
from pygame.locals import *


#問題点
#現在、for~in文でまわすことにより、メモリ使用量が多くなっている。
#重複した単純配列が見られるため完成次第改善。

#mainlist=[name,sex,ysex,yold,ynew,old,Q1~Q15]
#mainlist = [['kyumina',0,1,0,8,15],['RJ',1,0,6,15,9],['unitychan',1,1,3,43,9],['kanten',0,1,0,100,16],['buran',0,1,34,46,15],['man',0,1,0,12,23]]
csvfiles = []
initlist = []
mainlist = []
nomainlist = []
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
print 'Reading csvfile...'
bcsvfiles = os.listdir('.')
for csvcount in xrange(len(bcsvfiles)):
    if 'csv' in bcsvfiles[csvcount]:
        csvfiles.append(bcsvfiles[csvcount])
    else:
        pass
print u"カレントディレクトリ内にあるCSVファイル"
print ','.join(csvfiles)
while True:
    inputfile=raw_input("What CSV files? (Ex. hoge.csv)\n*If you want exit, You tipe 'exit'\n")
    if inputfile == 'exit':
        sys.exit()
    else:
        pass
    try:
        f = open(inputfile, 'rb')
    except IOError:
        print(u'ファイルを開けません。そのようなファイルは存在しません。')
        continue
    break

dataReader = csv.reader(f)
for row in dataReader:
    initlist.append(row)
print 'OK'
#print initlist

print 'Trans int...'
#int変換
#for count in xrange(len(mainlist)):
#    for snuncount in xrange(len(mainlist[count])):
#        mainlist[count][snuncount] = str(mainlist[count][snuncount])
#        print mainlist[count][snuncount]
for initcount in xrange(len(initlist)):
    bmainlist = []
    bmainlist.append(initlist[initcount][0])
    bmainlist.append(initlist[initcount][1])
    bmainlist.append(initlist[initcount][2])
    bmainlist.append(initlist[initcount][3])
    bmainlist.append(initlist[initcount][4])
    for snuncount in xrange(len(initlist[initcount])-5):
        bmainlist.append(int(initlist[initcount][snuncount+5]))
    mainlist.append(bmainlist)
#for initcount in xrange(len(initlist)):
#    mainlist.insert(0,initlist[initcount][0])
print 'OK'
#print mainlist


print 'Divide boy and girl...'
#性別の分別
for count in xrange(len(mainlist)):
    if mainlist[count][3] == 'M':
        boylist.append(mainlist[count])
    elif mainlist[count][3] == 'F':
        girllist.append(mainlist[count])
    elif mainlist[count][3] == 'B':
        boylist.append(mainlist[count])
        girllist.append(mainlist[count])

print 'OK'
#print boylist
#print 'Divide girl'
#print girllist

print "Devide sex&old..."
#年齢での分別
for count in xrange(len(mainlist)):
    bqchoose = []
    if mainlist[count][4] == 'F':
        for oldcount in xrange(len(girllist)):
            if mainlist[count][5] <= int(girllist[oldcount][2]) and mainlist[count][6] >= int(girllist[oldcount][2]):
                bqchoose.append(girllist[oldcount])
                #print bqchoose
            else:
                pass
                #print bqchoose

    elif mainlist[count][4] == 'M':
        for oldcount in xrange(len(boylist)):
            if mainlist[count][5] <= int(boylist[oldcount][2]) and mainlist[count][6] >= int(boylist[oldcount][2]):
                bqchoose.append(boylist[oldcount])
                #print bqchoose
            else:
                pass
                #print bqchoose

    elif mainlist[count][4] == 'B':
        for oldcount in xrange(len(boylist)):
            if mainlist[count][5] <= int(boylist[oldcount][2]) and mainlist[count][6] >= int(boylist[oldcount][2]):
                bqchoose.append(boylist[oldcount])
	for oldcount in xrange(len(girllist)):
	    if mainlist[count][5] <= int(girllist[oldcount][2]) and mainlist[count][6] >= int(girllist[oldcount][2]):
		bqchoose.append(girllist[oldcount])

    #print bqchoose
    qchoose.append(bqchoose)
print "OK"
#print qchoose

print 'Outputs error...'
#誤差処理
for countperm in xrange(len(mainlist)):
    bgosalist = []
    for countperso in xrange(len(qchoose[countperm])):
        siguma = 0
        for qcount in xrange(len(mainlist[0])-7):
            siguma += abs(mainlist[countperm][qcount+7] - qchoose[countperm][countperso][qcount+7])
        bgosalist.append(siguma)
        #print"bbgogogosa"
        #print bgosalist
    if len(qchoose[countperm]) == 0:
        bgosalist.append('None')
#    print "bgosa"
#    print bgosalist
    gosa.append(bgosalist)

print 'OK'
#print gosa


print "Trans dictionary..."
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
            bzgosadic.update({gosa[countm][countgo]:qchoose[countm][countgo][1]})
    zgosa.append(bzgosalist)
    zgosa.append(bzgosadic)

while zgosa.count([]) > 0:
    zgosa.remove([])
while zgosa.count({}) > 0:
    zgosa.remove({})

print "OK"
#print zgosa


print 'Sort of error...'
# sort of gosa
for countm in xrange(len(mainlist)):
    if gosa[countm][0] == 'None':
        pass
        #sgosa.append(['Nooo'])
    else:
        gosa[countm].sort()
        #print gosa[countm]

print 'OK'
#print gosa


print 'To collate...'
#zgosa gosa照合
for countm in xrange(len(mainlist)):
    bcgosa = []
    if gosa[countm][0] == 'None':
        if mainlist[countm][4] == 'M':
            bcgosa.append(mainlist[countm][1])
            bcgosa.append(boylist[random.randint(0,len(boylist))-1][1])
        elif mainlist[countm][4] == 'F':
            bcgosa.append(mainlist[countm][1])
            bcgosa.append(girllist[random.randint(0,len(girllist))-1][1])
	elif mainlist[countm][4] == 'B':
	    chsli = 0
	    chsli = random.randint(0,1)
	    bcgosa.append(mainlist[countm][1])
	    if chsli == 0:
		bcgosa.append(boylist[random.randint(0,len(boylist))-1][1])
	    elif chsli == 1:
		bcgosa.append(girllist[random.randint(0,len(girllist))-1][1])
    elif gosa[countm][0] == 0:
        if len(gosa[countm]) == 1:
            if mainlist[countm][4] == 'M':
                bcgosa.append(mainlist[countm][1])
                bcgosa.append(boylist[random.randint(0,len(boylist))-1][1])
            elif mainlist[countm][4] == 'F':
                bcgosa.append(mainlist[countm][1])
                bcgosa.append(girllist[random.randint(0,len(girllist))-1][1])
            elif mainlist[countm][4] == 'B':
                chsli = 0
                chsli = random.randint(0,1)
                bcgosa.append(mainlist[countm][1])
                if chsli == 0:
                    bcgosa.append(boylist[random.randint(0,len(boylist))-1][1])
                elif chsli == 1:
                    bcgosa.append(girllist[random.randint(0,len(girllist))-1][1])
        else:
            bcgosa.append(mainlist[countm][1])
            bcgosa.append (zgosa[countm][gosa[countm][1]])
    else:
        bcgosa.append(mainlist[countm][1])
        bcgosa.append(zgosa[countm][gosa[countm][0]])
        #print zgosa[countm][gosa[countm][0]]
        #print gosa[countm][0]
    alist.append(bcgosa)

print 'OK'


print 'Image generation...'
#画像生成
SCREEN_SIZE = (640,480)
for counta in xrange(len(alist)):
    fname = mainlist[counta][0]
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("match_python")
    myfont = pygame.font.Font("mika.ttf", 80)
    idfont = pygame.font.Font("mika.ttf", 40)
    matchi = idfont.render('ID%s'%(mainlist[counta][0]), True, (0,0,0))
    matchm = myfont.render(unicode(alist[counta][0], 'utf-8'), True, (0,0,0))
    matcha = myfont.render(unicode(alist[counta][1], 'utf-8'), True, (0,0,0))
    screen.fill((225,255,255))
    screen.blit(matchi, (20,10))
    screen.blit(matchm, (20,60))
    screen.blit(matcha, (20,160))
    pygame.image.save(screen, '%s.png'%(fname))
print 'OK'
print 'Completion'
