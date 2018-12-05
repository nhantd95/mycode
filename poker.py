from collections import  Counter
import string
list_card=[]
print("Suit: S: Spades, C: Clover, D: Diamond, H: Heart")
print("Rank: 2,3...J, Q, K, A")
print("Pls input carđ string:")
card_string= input()
new_string=card_string.replace('10','T')
a=new_string[1]
list_card.append(a)
b=new_string[3]
list_card.append(b)
c=new_string[5]
list_card.append(c)
d=new_string[7]
list_card.append(d)
e=new_string[9]
list_card.append(e)
print (list_card)
c=Counter(list_card)

v= c.values()

sorthand=sorted(v,reverse=True)
print (sorthand)

if sorthand[0]==4:
    print ("4C")
elif sorthand[0]==3 and sorthand[1]==2:
    print("FH")
elif sorthand[0]==3:
    print("3C")
elif sorthand[0]==2 and sorthand[1]==2:
    print("2P")
elif sorthand[0]==2:
    print("1P")
else: print('Nothing')