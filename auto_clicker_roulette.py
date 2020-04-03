import pyautogui as clik
import time


def find():
    if(clik.locateOnScreen(won)!=None):
        return "won"
    elif(clik.locateOnScreen(lost)!=None):
        return "lost"
    else:
        return None


noir='click/noir.png'
won='click/won.png'
lost='click/lost.png'

bid=0.5


#dabord on releve lempreinte de la case que l'on veut jouer
returned=clik.confirm("Prise d'empreinte de la case a jouer (3 sec)","WE GONNA WIN", ['OK', 'Cancel'])

if(returned=="Cancel"):
    print("program stop")
    exit()

time.sleep(3)
pos_bet=clik.position()

print("normal bet ")
print(pos_bet)

#la case dans laquelle on double la mise
returned=clik.confirm("Prise d'empreinte de la case a doubler (3sec)","WE GONNA WIN", ['OK', 'Cancel'])

if(returned=="Cancel"):
    print("program stop")
    exit()

time.sleep(3)
pos_double=clik.position()

print("double quantité ")
print(pos_double)

clik.confirm("Starting after that !","waiting for win",['OK'])

#pre start, waiting for a win

locate=clik.locateOnScreen(won)

while(locate==None):
    print("waiting for start")
    locate = clik.locateOnScreen(won)

#after that its a start
clik.click(pos_bet)#click on the bet

while(True):
    locate = find()#try to find eiter a won or a lost or nothing

    while(locate==None):
        print("not found")
        locate = find()

    if(locate=="won"):
        time.sleep(2)
        clik.click(pos_bet)
        print("position won, new normal bet")
    elif(locate=="lost"):
        time.sleep(2)
        clik.click(pos_double)
        clik.click(pos_double)
        bid=2*bid
        print("lost, bid is now : ")
        print(bid)

#once you won the first time, its time to get the processing started

locate_noir=clik.locateOnScreen(noir)

clik.moveTo(locate)

print(locate)


