import mastermind
mm = mastermind.Mastermind()
## pour g ́en ́erer un code secret :
cpt = 1
bp, mp = 0, 0
while (cpt < 10) and (bp != mm.dim()) :
    print("Tour "+str(cpt))
    rep = eval(input("Votre proposition ? "))
    bp,mp = mm.bp_mp(rep)
    print("La r ́eponse est ",bp,"bien plac ́es et ",mp,"mal plac ́es.")
    cpt += 1
## end of while
if (bp,mp) == (mm.dim(),0) :
    print("Bravo, la partie est finie, vous avez gagn ́e.")
