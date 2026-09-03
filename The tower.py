import pygame
import random
import time

nf=1.3
sf=(0,0,0)
pygame.init()
screen = pygame.display.set_mode((int(210*nf), int(460*nf)))
pygame.display.set_caption("Gioco")
screen.fill(sf)

sb=pygame.transform.scale(pygame.image.load("sb.png").convert_alpha(),(int(210*nf), int(460*nf)))
screen.blit(sb,(0,0))

font_semi = pygame.font.SysFont("segoeuiSymbol", int(36*nf))
font_big = pygame.font.SysFont(None, int(8*nf))
font_med = pygame.font.SysFont(None, int(36*nf))
font_small = pygame.font.SysFont(None, int(25*nf))

carte = {'  ': [' ', ' '], 'JR': ['J', 'R'], 'JN': ['J', 'N'], 'A♥': ['A', '♥'], 'A♦': ['A', '♦'], 'A♣': ['A', '♣'],
         'A♠': ['A', '♠'], '2♥': ['2', '♥'], '2♦': ['2', '♦'], '2♣': ['2', '♣'], '2♠': ['2', '♠'], '3♥': ['3', '♥'],
         '3♦': ['3', '♦'], '3♣': ['3', '♣'], '3♠': ['3', '♠'], '4♥': ['4', '♥'], '4♦': ['4', '♦'], '4♣': ['4', '♣'],
         '4♠': ['4', '♠'], '5♥': ['5', '♥'], '5♦': ['5', '♦'], '5♣': ['5', '♣'], '5♠': ['5', '♠'], '6♥': ['6', '♥'],
         '6♦': ['6', '♦'], '6♣': ['6', '♣'], '6♠': ['6', '♠'], '7♥': ['7', '♥'], '7♦': ['7', '♦'], '7♣': ['7', '♣'],
         '7♠': ['7', '♠'], '8♥': ['8', '♥'], '8♦': ['8', '♦'], '8♣': ['8', '♣'], '8♠': ['8', '♠'], '9♥': ['9', '♥'],
         '9♦': ['9', '♦'], '9♣': ['9', '♣'], '9♠': ['9', '♠'], '10♥': ['10', '♥'], '10♦': ['10', '♦'],
         '10♣': ['10', '♣'], '10♠': ['10', '♠'], 'J♥': ['J', '♥'], 'J♦': ['J', '♦'], 'J♣': ['J', '♣'], 'J♠': ['J', '♠'],
         'Q♥': ['Q', '♥'], 'Q♦': ['Q', '♦'], 'Q♣': ['Q', '♣'], 'Q♠': ['Q', '♠'], 'K♥': ['K', '♥'], 'K♦': ['K', '♦'],
         'K♣': ['K', '♣'], 'K♠': ['K', '♠']}
semi = ['♥', '♦', '♣', '♠']
nume = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
l_carte = ['JR', 'JN']
va = 0
while va < 13:
    l_carte.append(nume[va] + semi[0])
    l_carte.append(nume[va] + semi[1])
    l_carte.append(nume[va] + semi[2])
    l_carte.append(nume[va] + semi[3])
    va += 1


# print(carte)
# print(l_carte)
def draw_card(carta, x, y):
    global nf
    collo = (0, 0, 0)
    if carta[-1] == '♣' or carta[-1] == '♠' or carta[-1] == 'N':
        collo = (0, 0, 0)
    elif carta[-1] == '♥' or carta[-1] == '♦' or carta[-1] == 'R':
        collo = (255, 0, 0)
    carte = {'  ': [' ', ' '], 'JR': ['J', 'R'], 'JN': ['J', 'N'], 'A♥': ['A', '♥'], 'A♦': ['A', '♦'], 'A♣': ['A', '♣'],
             'A♠': ['A', '♠'], '2♥': ['2', '♥'], '2♦': ['2', '♦'], '2♣': ['2', '♣'], '2♠': ['2', '♠'], '3♥': ['3', '♥'],
             '3♦': ['3', '♦'], '3♣': ['3', '♣'], '3♠': ['3', '♠'], '4♥': ['4', '♥'], '4♦': ['4', '♦'], '4♣': ['4', '♣'],
             '4♠': ['4', '♠'], '5♥': ['5', '♥'], '5♦': ['5', '♦'], '5♣': ['5', '♣'], '5♠': ['5', '♠'], '6♥': ['6', '♥'],
             '6♦': ['6', '♦'], '6♣': ['6', '♣'], '6♠': ['6', '♠'], '7♥': ['7', '♥'], '7♦': ['7', '♦'], '7♣': ['7', '♣'],
             '7♠': ['7', '♠'], '8♥': ['8', '♥'], '8♦': ['8', '♦'], '8♣': ['8', '♣'], '8♠': ['8', '♠'], '9♥': ['9', '♥'],
             '9♦': ['9', '♦'], '9♣': ['9', '♣'], '9♠': ['9', '♠'], '10♥': ['10', '♥'], '10♦': ['10', '♦'],
             '10♣': ['10', '♣'], '10♠': ['10', '♠'], 'J♥': ['J', '♥'], 'J♦': ['J', '♦'], 'J♣': ['J', '♣'],
             'J♠': ['J', '♠'], 'Q♥': ['Q', '♥'], 'Q♦': ['Q', '♦'], 'Q♣': ['Q', '♣'], 'Q♠': ['Q', '♠'], 'K♥': ['K', '♥'],
             'K♦': ['K', '♦'], 'K♣': ['K', '♣'], 'K♠': ['K', '♠']}
    semi = ['♥', '♦', '♣', '♠']
    nume = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    l_carte = ['JR', 'JN']
    va = 0
    while va < 13:
        l_carte.append(nume[va] + semi[0])
        l_carte.append(nume[va] + semi[1])
        l_carte.append(nume[va] + semi[2])
        l_carte.append(nume[va] + semi[3])
        va += 1

    # print(carte)
    # print(l_carte)

    ba = pygame.Rect(int(x*nf), int(y*nf), int(40*nf), int(60*nf))
    x=int(x*nf)
    y=int(y*nf)
    pygame.draw.rect(screen, (255, 255, 255), ba)

    msg1 = font_semi.render(str(carte[carta][1]), True, collo)
    screen.blit(msg1, (x + 7.5*(nf/1.2), y - 12.5*(nf/1.2)))

    msg2 = font_med.render(str(carte[carta][0]), True, collo)
    screen.blit(msg2, (x + 12.5*(nf/1.2), y + 37.5*(nf/1.2)))

    pygame.display.flip()

    return ba


def redraw(ba, carta):
    global nf
    collo = (0, 0, 0)
    if carta[-1] == '♣' or carta[-1] == '♠' or carta[-1] == 'N':
        collo = (0, 0, 0)
    elif carta[-1] == '♥' or carta[-1] == '♦' or carta[-1] == 'R':
        collo = (255, 0, 0)
    carte = {'  ': [' ', ' '], 'JR': ['J', 'R'], 'JN': ['J', 'N'], 'A♥': ['A', '♥'], 'A♦': ['A', '♦'], 'A♣': ['A', '♣'],
             'A♠': ['A', '♠'], '2♥': ['2', '♥'], '2♦': ['2', '♦'], '2♣': ['2', '♣'], '2♠': ['2', '♠'], '3♥': ['3', '♥'],
             '3♦': ['3', '♦'], '3♣': ['3', '♣'], '3♠': ['3', '♠'], '4♥': ['4', '♥'], '4♦': ['4', '♦'], '4♣': ['4', '♣'],
             '4♠': ['4', '♠'], '5♥': ['5', '♥'], '5♦': ['5', '♦'], '5♣': ['5', '♣'], '5♠': ['5', '♠'], '6♥': ['6', '♥'],
             '6♦': ['6', '♦'], '6♣': ['6', '♣'], '6♠': ['6', '♠'], '7♥': ['7', '♥'], '7♦': ['7', '♦'], '7♣': ['7', '♣'],
             '7♠': ['7', '♠'], '8♥': ['8', '♥'], '8♦': ['8', '♦'], '8♣': ['8', '♣'], '8♠': ['8', '♠'], '9♥': ['9', '♥'],
             '9♦': ['9', '♦'], '9♣': ['9', '♣'], '9♠': ['9', '♠'], '10♥': ['10', '♥'], '10♦': ['10', '♦'],
             '10♣': ['10', '♣'], '10♠': ['10', '♠'], 'J♥': ['J', '♥'], 'J♦': ['J', '♦'], 'J♣': ['J', '♣'],
             'J♠': ['J', '♠'], 'Q♥': ['Q', '♥'], 'Q♦': ['Q', '♦'], 'Q♣': ['Q', '♣'], 'Q♠': ['Q', '♠'], 'K♥': ['K', '♥'],
             'K♦': ['K', '♦'], 'K♣': ['K', '♣'], 'K♠': ['K', '♠']}
    semi = ['♥', '♦', '♣', '♠']
    nume = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    l_carte = ['JR', 'JN']
    va = 0
    while va < 13:
        l_carte.append(nume[va] + semi[0])
        l_carte.append(nume[va] + semi[1])
        l_carte.append(nume[va] + semi[2])
        l_carte.append(nume[va] + semi[3])
        va += 1

    # print(carte)
    # print(l_carte)

    pygame.draw.rect(screen, (255, 255, 255), ba)

    msg1 = font_semi.render(str(carte[carta][1]), True, collo)
    screen.blit(msg1, (ba.x + 7.5*(nf/1.2), ba.y - 12.5*(nf/1.2)))

    msg2 = font_med.render(str(carte[carta][0]), True, collo)
    screen.blit(msg2, (ba.x + 12.5*(nf/1.2), ba.y + 37.5*(nf/1.2)))

    pygame.display.flip()

def punti(tutto2):
    # print('Inserisci Carte')
    # tutto1=input('')
    # tutto1='A,PICCHE 2,QUADRI'

    #tutto2 = tutto1.split(' ')
    # print(tutto1)
    # print(tutto2)
    tutto3 = []
    x = 0
    while x < len(tutto2):
        tutto3.extend(tutto2[x].split(','))
        x += 1

    # print(tutto3)
    numeri_prov = []
    y = 0
    while y < len(tutto3):
        numeri_prov.append(tutto3[y])
        y += 2

    # print(numeri_prov)
    semi_prov = []
    z = 1
    while z < len(tutto3):
        semi_prov.append(tutto3[z])
        z += 2
    # print(semi_prov)
    dizionario = {'0': 0, 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                  'Q': 10, 'K': 10, '♠': 1, '♣': 2, '♦': 3, '♥': 4, ' ':0, '  ':0, '':0}
    xx = 0
    numeri = []
    while xx < len(numeri_prov):
        numeri.append(dizionario[numeri_prov[xx]])
        xx += 1
    yy = 0
    semi = []
    while yy < len(semi_prov):
        semi.append(dizionario[semi_prov[yy]])
        yy += 1
    # print(numeri)
    # print(semi)
    bonussemi = [0, 1, 1, 1, 1]
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    i1 = 0
    while i1 < 9:
        if semi[i1] == 1:
            s1 += 1
        elif semi[i1] == 2:
            s2 += 1
        elif semi[i1] == 3:
            s3 += 1
        elif semi[i1] == 4:
            s4 += 1
        i1 += 1
    if s1 > 4:
        bonussemi[1] += 1
    elif s2 > 4:
        bonussemi[2] += 1
    elif s3 > 4:
        bonussemi[3] += 1
    elif s4 > 4:
        bonussemi[4] += 1
    bonus = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    i2 = 0
    while i2 < 9:
        j2 = 0
        while j2 < 9:
            if semi[i2] == semi[j2]:
                bonus[i2] += 1
            j2 += 3
        i2 += 3
    i2 = 1
    while i2 < 9:
        j2 = 1
        while j2 < 9:
            if semi[i2] == semi[j2]:
                bonus[i2] += 1
            j2 += 3
        i2 += 3
    i2 = 2
    while i2 < 9:
        j2 = 2
        while j2 < 9:
            if semi[i2] == semi[j2]:
                bonus[i2] += 1
            j2 += 3
        i2 += 3
    tot = 0
    i3 = 0
    while i3 < 9:
        tot += (numeri[i3] + semi[i3]) * bonus[i3] * bonussemi[semi[i3]]
        i3 += 1
    # print(numeri)
    # print(semi)
    # print(bonussemi)
    # print(bonus)
    #print('')
    #print('Hai Fatto', tot, 'Punti')
    return tot

screen.blit(sb, (0, 0))

mazzo = []
var = 0
while var < len(l_carte):
    y = len(l_carte)
    a = random.randint(0, (y - 1))
    mazzo.append(l_carte[a])
    l_carte.pop(a)
# print(mazzo)
slot = []
vav = 0
vvav = 1
while vav < 9:
    slot.append(draw_card('  ', -40 + (50 * vvav), 10 + (70 * int(vav / 3))))
    if int(vvav / 3) == 1:
        vvav = 0
    vav += 1
    vvav += 1

vavv = 0
vvavv = 1
while vavv < 9:
    slot.append(draw_card('  ', -40 + (50 * vvavv), 240 + (70 * int(vavv / 3))))
    if int(vvavv / 3) == 1:
        vvavv = 0
    vavv += 1
    vvavv += 1
# print(slot[2])
# print(slot[17])
ordine=[0,3,6,1,4,7,2,5,8]
slot_alto=[slot[i] for i in ordine]
slot_basso=[slot[i+9] for i in ordine]
slotn=['']
slotn.extend(slot_alto)
slotn.extend(slot_basso)
#print(slotn)
#print(len(slotn))

slot_carte_alto=['  ']*9
slot_carte_basso=['  ']*9
slotnc=['']
slotnc.extend(slot_carte_alto)
slotnc.extend(slot_carte_basso)
#print(slotnc)
#print(len(slotnc))

f0 = pygame.Rect(int(160*nf), int(120*nf), int(40*nf), int(60*nf))
f1 = pygame.Rect(int(160*nf), int(270*nf), int(40*nf), int(60*nf))
c0=pygame.transform.scale(pygame.image.load("cb.png").convert_alpha(),(int(40*nf), int(60*nf)))
c1=pygame.transform.scale(pygame.image.load("cs.png").convert_alpha(),(int(40*nf), int(60*nf)))
screen.blit(c0, (int(160 * nf), int(120 * nf)))
screen.blit(c1, (int(160 * nf), int(270 * nf)))

collo0 = (0, 0, 0)
collo1 = (0, 0, 0)
vuo = 0
vue = 0
card = draw_card(mazzo[0], 160, 195)
zz = 0
while len(mazzo)>0:
    if zz % 2 == 0:
        collo0 = (255, 0, 0)
        collo1 = (0, 0, 0)
    elif zz % 2 == 1:
        collo0 = (0, 0, 0)
        collo1 = (255, 0, 0)
    msgc0 = font_semi.render('¤', True, collo0)
    screen.blit(msgc0, (int(110*nf) + int(50*nf), int(10*nf)))
    msgc1 = font_semi.render('¤', True, collo1)
    screen.blit(msgc1, (int(110*nf) + int(50*nf), int(380*nf)))
    msgf0 = font_med.render('F', True, sf)
    msgf1 = font_med.render('F', True, sf)
    screen.blit(msgf0,f0.center)
    screen.blit(msgf1,f1.center)

    cic0 = (0, 0, 0)
    cic1 = (0, 0, 0)
    f0 = pygame.Rect(int(160 * nf), int(120 * nf), int(40 * nf), int(60 * nf))
    pygame.draw.rect(screen, cic0, f0)
    f1 = pygame.Rect(int(160 * nf), int(270 * nf), int(40 * nf), int(60 * nf))
    pygame.draw.rect(screen, cic1, f1)
    
    screen.blit(c0, (int(160 * nf), int(120 * nf)))
    screen.blit(c1, (int(160 * nf), int(270 * nf)))
    if '  ' in slotnc[1:10]:
        ccccc=''
    else:
        cic0 = (255, 255, 255)
        f0 = pygame.Rect(int(160 * nf), int(120 * nf), int(40 * nf), int(60 * nf))
        pygame.draw.rect(screen, cic0, f0)

    if '  ' in slotnc[10:19]:
        ccc=''
    else:
        cic1 = (255, 255, 255)
        f1 = pygame.Rect(int(160 * nf), int(270 * nf), int(40 * nf), int(60 * nf))
        pygame.draw.rect(screen, cic1, f1)

#    f0 = pygame.Rect(int(160*nf), int(120*nf), int(40*nf), int(60*nf))
#    pygame.draw.rect(screen, cic0, f0)
#    f1 = pygame.Rect(int(160*nf), int(270*nf), int(40*nf), int(60*nf))
#    pygame.draw.rect(screen, cic1, f1)
    #print(slotnc[1:10])
    #print(slotnc[10:19])
    pygame.display.flip()
    # print(len(mazzo))

    #card = draw_card(mazzo[0], 160, 195)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running=False
                mazzo=[]
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                if zz % 2 == 0 and f0.collidepoint(mx, my):
                    if '  ' in slotnc[1:10]:
                        cc=''
                    else:
                        running=False
                        mazzo=[]
                        break
                elif zz%2 ==1 and f1.collidepoint(mx, my):
                    if '  ' in slotnc[10:19]:
                        cccc=''
                    else:
                        running = False
                        mazzo = []
                        break

                la = 0
                while la < len(slot):
                    if slotn[la + 1].collidepoint(mx,my):
                        bib=la + 1
                        running=False
                    la+=1

    if int(((bib-1)-((bib-1)%9))/9)==zz%2:

        cacaca = 0
        if len(mazzo)>0:
            if slotnc[bib]!='  ':
                redraw(slotn[bib],'  ')
                slotnc[bib]='  '
                cacaca=1
                mazzo.pop(0)

        if len(mazzo) != 0:
            if cacaca == 0 and mazzo[0] == 'JN' or cacaca == 0 and mazzo[0] == 'JR':
                if mazzo[0] == 'JN':
                    cacaca = 1
                    redraw(slotn[bib],'  ')
                    slotnc[bib]='  '
                    mazzo.pop(0)
                    vuo = 0
                    while vuo < 18:
                        babal = slotnc[vuo + 1][-1] == '♣' or slotnc[vuo + 1][-1] == '♠'
                        if babal:
                            slotnc[vuo + 1]='  '
                            redraw(slotn[vuo + 1],'  ')
                        vuo += 1

                if mazzo[0] == 'JR':
                    cacaca = 1
                    redraw(slotn[bib],'  ')
                    slotnc[bib]='  '
                    mazzo.pop(0)
                    vue = 0
                    while vue < 18:
                        bebal = slotnc[vue + 1][-1] == '♥' or slotnc[vue + 1][-1] == '♦'
                        if bebal:
                            slotnc[vue + 1]='  '
                            redraw(slotn[vue + 1],'  ')
                        vue += 1

        if len(mazzo)>0:
            if cacaca==0:
                if slotnc[bib]=='  ':
                    redraw(slotn[bib],mazzo[0])
                    slotnc[bib]=mazzo[0]
                    mazzo.pop(0)

        if cacaca == 0:

            bellaperme = (((bib - 1) - ((bib - 1) % 3)) / 3 + 3) % 6
            # print(bellaperme)
            index = 1
            while index <= 3:
                if slotnc[int(3 * bellaperme + index)][-1]==slotnc[bib][-1]:
                    slotnc[int(3 * bellaperme + index)]='  '
                    redraw(slotn[int(3 * bellaperme + index)],'  ')
                    # print('ciao')
                # print(3*bellaperme+index)
                index += 1

        if len(mazzo)>0:
            card = draw_card(mazzo[0], 160, 195)
            zz += 1
            # pesca
        pygame.display.flip()

    else:
        if slotnc[bib]=='  ':
            cacaca=0
            if len(mazzo) != 0:
                if cacaca == 0 and mazzo[0] == 'JN' or cacaca == 0 and mazzo[0] == 'JR':
                    if mazzo[0] == 'JN':
                        cacaca = 1
                        redraw(slotn[bib],'  ')
                        slotnc[bib]='  '
                        mazzo.pop(0)
                        vuo = 0
                        while vuo < 18:
                            babal = slotnc[vuo + 1][-1] == '♣' or slotnc[vuo + 1][-1] == '♠'
                            if babal:
                                slotnc[vuo + 1]='  '
                                redraw(slotn[vuo + 1],'  ')
                            vuo += 1

                    if mazzo[0] == 'JR':
                        cacaca = 1
                        redraw(slotn[bib],'  ')
                        slotnc[bib]='  '
                        mazzo.pop(0)
                        vue = 0
                        while vue < 18:
                            bebal = slotnc[vue + 1][-1] == '♥' or slotnc[vue + 1][-1] == '♦'
                            if bebal:
                                slotnc[vue + 1]='  '
                                redraw(slotn[vue + 1],'  ')
                            vue += 1

            if len(mazzo)>0:
                if cacaca==0:
                    if slotnc[bib]=='  ':
                        redraw(slotn[bib],mazzo[0])
                        slotnc[bib]=mazzo[0]
                        mazzo.pop(0)

            if cacaca == 0:

                bellaperme = (((bib - 1) - ((bib - 1) % 3)) / 3 + 3) % 6
                # print(bellaperme)
                index = 1
                while index <= 3:
                    if slotnc[int(3 * bellaperme + index)][-1]==slotnc[bib][-1]:
                        slotnc[int(3 * bellaperme + index)]='  '
                        redraw(slotn[int(3 * bellaperme + index)],'  ')
                        # print('ciao')
                    # print(3*bellaperme+index)
                    index += 1

            if len(mazzo) > 0:
                card = draw_card(mazzo[0], 160, 195)
                zz += 1
                # pesca
            pygame.display.flip()

tutt0=''
n=0
while n<8:
    if slotnc[n+1]!='  ' and slotnc[n+1]!='    ' and slotnc[n+1]!='   ':
        print(slotnc[n + 1])
        tutt0+=carte[slotnc[n+1]][0]+','+carte[slotnc[n+1]][1]+' '
    else:
        print(slotnc[n + 1])
        tutt0+='0,0 '
    n+=1
if slotnc[n+1]!='  ' and slotnc[n+1]!='    ' and slotnc[n+1]!='   ':
    print(slotnc[n + 1])
    tutt0+=carte[slotnc[n+1]][0]+','+carte[slotnc[n+1]][1]
else:
    print(slotnc[n + 1])
    tutt0 += '0,0'
tutt1=''
m=0
while m<8:
    if slotnc[m+10]!='  ' and slotnc[m+10]!='    ' and slotnc[m+10]!='   ':
        print(slotnc[m+10])
        tutt1+=carte[slotnc[m+10]][0]+','+carte[slotnc[m+10]][1]+' '
    else:
        print(slotnc[m+10])
        tutt1 += '0,0 '
    m+=1
if slotnc[m+10]!='  ' and slotnc[m+10]!='    ' and slotnc[m+10]!='   ':
    print(slotnc[m + 10])
    tutt1+=carte[slotnc[m+10]][0]+','+carte[slotnc[m+10]][1]
else:
    print(slotnc[m + 10])
    tutt1 += '0,0'
tutt0=tutt0.split(' ')
tutt1=tutt1.split(' ')
tuttoo0=[tutt0[0],tutt0[3],tutt0[6],tutt0[1],tutt0[4],tutt0[7],tutt0[2],tutt0[5],tutt0[8]]
tuttoo1=[tutt1[0],tutt1[3],tutt1[6],tutt1[1],tutt1[4],tutt1[7],tutt1[2],tutt1[5],tutt1[8]]
print(tutt0)
print(tutt1)
print(type(tutt0))
print(tuttoo0)
print(tuttoo1)
punti0=punti(tuttoo0)
punti1=punti(tuttoo1)

msgc0 = font_med.render(str(punti0), True, (255,0,0))
screen.blit(msgc0, (int(110*nf) + int(50*nf), int(60*nf)))
msgc1 = font_med.render(str(punti1), True, (255,0,0))
screen.blit(msgc1, (int(110*nf) + int(50*nf), int(360*nf)))
pygame.display.flip()

#print('fine')
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
