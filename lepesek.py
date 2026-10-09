lepesek_szama=[
6500,8200,4300,10100,7600,12000,5400,9800,3900,11200]
legtobb_lepesek=0
ossz=0
nap=0
mini=0
for i in range(len(lepesek_szama)):
    nap+=1
    if legtobb_lepesek<lepesek_szama[i]:
        legtobb_lepesek=lepesek_szama[i]
        nap-=1
    if 10000<=lepesek_szama[i]:
        mini+=1
    ossz+=lepesek_szama[i]
  

print(f"A lépések összege: {ossz} db")
print(f"A lépések átlaga egy nap: {ossz/len(lepesek_szama)} db")
print(f"A legtöbb lépés a {nap}. napon volt: {legtobb_lepesek}")
print(f"{mini} napon volt legalább 10000 lépés")