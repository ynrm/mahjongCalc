import copy
import random
from functools import cmp_to_key
def compare(arg1,arg2):
    """
    handViewのソート用
    """
    o1 = copy.deepcopy(arg1)
    o2 = copy.deepcopy(arg2)
    if o1[1] == 'm':
        o1[1] = 1
    elif o1[1] == 's':
        o1[1] = 2
    elif o1[1] == 'p':
        o1[1] = 3
    elif o1[1] == 'e':
        o1[1] = 4
    elif o1[1] == 's':
        o1[1] = 5
    elif o1[1] == 'w':
        o1[1] = 6
    elif o1[1] == 'n':
        o1[1] = 7
    elif o1[1] == 'h':
        o1[1] = 8
    elif o1[1] == 'g':
        o1[1] = 9
    elif o1[1] == 'r':
        o1[1] = 10
    if o2[1] == 'm':
        o2[1] = 1
    elif o2[1] == 's':
        o2[1] = 2
    elif o2[1] == 'p':
        o2[1] = 3
    elif o2[1] == 'e':
        o2[1] = 4
    elif o2[1] == 's':
        o2[1] = 5
    elif o2[1] == 'w':
        o2[1] = 6
    elif o2[1] == 'n':
        o2[1] = 7
    elif o2[1] == 'h':
        o2[1] = 8
    elif o2[1] == 'g':
        o2[1] = 9
    elif o2[1] == 'r':
        o2[1] = 10
    if o1[1]<o2[1]:
        return -1
    elif o1[1]>o2[1]:
        return 1
    else:
        if o1[0]<o2[0]:
            return -1
        elif o1[0]>o2[0]:
            return 1
        else:
            return 0

def dealing(hand):
    """
    麻雀の山を積んで、和了形になっている手牌をhandに格納して返す。\n
    現在は面子4つと対子1つの14牌を返す。\n
    各面子・対子の形式は、[形式, 牌1, 牌2, ...]\n
    各牌の形式は以下の組でリストになっている\n
    萬子: [1,'m']～[9,'m']\n
    索子：[1,'s']～[9,'s']\n
    筒子：[1,'p']～[9,'p']\n
    東：[0,'e']、南：[0,'s']、西：[0,'w']、北：[0,'n']\n
    白：[0,'h']、發：[0,'g']、中：[0,'r'] <- wHite, Green, Red\n

    Args:
        hand (list): 手牌のリスト
    
    Return:
        hand (list): 手牌のリスト
    """
    # 手牌を初期化しておく
    hand = []
    # 山札の準備
    jihai = ['e','s','w','n','h','g','r']
    deck = [[i,'m'] for i in range(1,10)] + [[i,'s'] for i in range(1,10)]
    deck += [[i,'p'] for i in range(1,10)] + [[0,i] for i in jihai]
    deck.extend(copy.deepcopy(deck))
    deck.extend(copy.deepcopy(deck))
    deck.extend(copy.deepcopy(deck))
    """ ID確認用
        print(deck[0])
        print(deck[34])
        print(deck[68])
        print(deck[102])
        print(id(deck[0]))
        print(id(deck[34]))
        print(id(deck[68]))
        print(id(deck[102]))
    """
    # 考え得る組み合わせを作っておく（面子）
    tileSet = []
    tileSetTmp = [['o',[i,'m'],[i+1,'m'],[i+2,'m']] for i in range(1,8)]
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSetTmp = [['o',[i,'s'],[i+1,'s'],[i+2,'s']] for i in range(1,8)]
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSetTmp = [['o',[i,'p'],[i+1,'p'],[i+2,'p']] for i in range(1,8)]
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSet.extend(copy.deepcopy(tileSetTmp))
    tileSetTmp =  [['3',[i,'m'],[i,'m'],[i,'m']] for i in range(1,10)]
    tileSetTmp += [['3',[i,'s'],[i,'s'],[i,'s']] for i in range(1,10)]
    tileSetTmp += [['3',[i,'p'],[i,'p'],[i,'p']] for i in range(1,10)]
    tileSetTmp += [['3',[0,i],[0,i],[0,i]] for i in jihai]
    #tileSetTmp += [['4',[i,'m'],[i,'m'],[i,'m'],[i,'m']] for i in range(1,10)]
    #tileSetTmp += [['4',[i,'s'],[i,'s'],[i,'s'],[i,'s']] for i in range(1,10)]
    #tileSetTmp += [['4',[i,'p'],[i,'p'],[i,'p'],[i,'p']] for i in range(1,10)]
    #tileSetTmp += [['4',[0,i],[0,i],[0,i],[0,i]] for i in jihai]
    tileSet.extend(copy.deepcopy(tileSetTmp))
    """ ID確認用
        print(tileSet[0])
        print(tileSet[7])
        print(id(tileSet[0]))
        print(id(tileSet[7]))
        print(tileSet[0][1])
        print(tileSet[7][1])
        print(id(tileSet[0][1]))
        print(id(tileSet[7][1]))
        print(tileSet[0][2])
        print(tileSet[1][1])
        print(id(tileSet[0][2]))
        print(id(tileSet[1][1]))
    """
    # 考え得る組み合わせを作っておく（対子）
    tilePair = []
    tilePairTmp =  [['2',[i,'m'],[i,'m']] for i in range(1,10)]
    tilePairTmp += [['2',[i,'s'],[i,'s']] for i in range(1,10)]
    tilePairTmp += [['2',[i,'p'],[i,'p']] for i in range(1,10)]
    tilePairTmp += [['2',[0,i],[0,i]] for i in jihai]
    tilePair.extend(copy.deepcopy(tilePairTmp))
    tilePair.extend(copy.deepcopy(tilePairTmp))

    # 配牌
    ind = random.randrange(len(tileSet))
    tmpTiles=tileSet.pop(ind)
    hand.append(copy.deepcopy(tmpTiles))

    while True:
        ind = random.randrange(len(tileSet))
        tmpTiles=tileSet.pop(ind)
        deckTmp = copy.deepcopy(deck)
        if not (tmpTiles[1] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[1])
        if not (tmpTiles[2] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[2])
        if not (tmpTiles[3] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[3])
        if tmpTiles[0] == '4':
            if not (tmpTiles[4] in deckTmp):
                continue
            deckTmp.remove(tmpTiles[4])
        break
    hand.append(copy.deepcopy(tmpTiles))
    for i in range(1,len(tmpTiles)):
        tmpTile=tmpTiles[i]
        for j in range(0,len(deck)):
            if deck[j][0] != tmpTile[0]:
                continue
            if deck[j][1] != tmpTile[1]:
                continue
            deck.pop(j)
            break

    while True:
        ind = random.randrange(len(tileSet))
        tmpTiles=tileSet.pop(ind)
        deckTmp = copy.deepcopy(deck)
        if not (tmpTiles[1] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[1])
        if not (tmpTiles[2] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[2])
        if not (tmpTiles[3] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[3])
        if tmpTiles[0] == '4':
            if not (tmpTiles[4] in deckTmp):
                continue
            deckTmp.remove(tmpTiles[4])
        break
    hand.append(copy.deepcopy(tmpTiles))
    for i in range(1,len(tmpTiles)):
        tmpTile=tmpTiles[i]
        for j in range(0,len(deck)):
            if deck[j][0] != tmpTile[0]:
                continue
            if deck[j][1] != tmpTile[1]:
                continue
            deck.pop(j)
            break

    while True:
        ind = random.randrange(len(tileSet))
        tmpTiles=tileSet.pop(ind)
        deckTmp = copy.deepcopy(deck)
        if not (tmpTiles[1] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[1])
        if not (tmpTiles[2] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[2])
        if not (tmpTiles[3] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[3])
        if tmpTiles[0] == '4':
            if not (tmpTiles[4] in deckTmp):
                continue
            deckTmp.remove(tmpTiles[4])
        break
    hand.append(copy.deepcopy(tmpTiles))
    for i in range(1,len(tmpTiles)):
        tmpTile=tmpTiles[i]
        for j in range(0,len(deck)):
            if deck[j][0] != tmpTile[0]:
                continue
            if deck[j][1] != tmpTile[1]:
                continue
            deck.pop(j)
            break

    while True:
        ind = random.randrange(len(tilePair))
        tmpTiles=tilePair.pop(ind)
        deckTmp = copy.deepcopy(deck)
        if not (tmpTiles[1] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[1])
        if not (tmpTiles[2] in deckTmp):
            continue
        deckTmp.remove(tmpTiles[2])
        break
    hand.append(copy.deepcopy(tmpTiles))
    for i in range(1,len(tmpTiles)):
        tmpTile=tmpTiles[i]
        for j in range(0,len(deck)):
            if deck[j][0] != tmpTile[0]:
                continue
            if deck[j][1] != tmpTile[1]:
                continue
            deck.pop(j)
            break

    """ 手牌確認用
    handView=[]
    for i in range(len(hand)):
        tmpHandTiles = copy.deepcopy(hand[i])
        tmpHandTiles.pop(0)
        handView.extend(tmpHandTiles)
    print(handView)
    """
    return hand

def handViewer(hand):
    handView=[]
    for i in range(len(hand)):
        tmpHandTiles = copy.deepcopy(hand[i])
        tmpHandTiles.pop(0)
        handView.extend(tmpHandTiles)
    sortedHand=sorted(handView, key=cmp_to_key(compare))
    print(sortedHand)
    for tile in sortedHand:
        if tile[0] == 0:
            if tile[1] == 'e':
                print('東 ',end='')
            elif tile[1] == 's':
                print('南 ',end='')
            elif tile[1] == 'w':
                print('西 ',end='')
            elif tile[1] == 'n':
                print('北 ',end='')
            elif tile[1] == 'h':
                print('白 ',end='')
            elif tile[1] == 'g':
                print('發 ',end='')
            elif tile[1] == 'r':
                print('中 ',end='')
        else:
            if tile[0] == 1:
                print('一',end='')
            elif tile[0] == 2:
                print('二',end='')
            elif tile[0] == 3:
                print('三',end='')
            elif tile[0] == 4:
                print('四',end='')
            elif tile[0] == 5:
                print('五',end='')
            elif tile[0] == 6:
                print('六',end='')
            elif tile[0] == 7:
                print('七',end='')
            elif tile[0] == 8:
                print('八',end='')
            elif tile[0] == 9:
                print('九',end='')
            if tile[1] == 'm':
                print('萬 ',end='')
            elif tile[1] == 's':
                print('索 ',end='')
            elif tile[1] == 'p':
                print('筒 ',end='')

if __name__ == "__main__":
    hand=dealing(hand=list())
    handViewer(hand)