from collections import defaultdict
import math;
jug1=int(input("enter the jug1 value"))
jug2=int(input("enter the jug2 value"))
aim=int(input("enter the aim"))
visited=defaultdict(lambda:false)
def WaterJugSolver(amt1,amt2):
    if(amt1==aim and amt2==0)or(amt2==aim and amt1==0):
        print(amt1,amt2)
        return true
    if visited[(amt1,amt2)]==false:
        print(amt1,amt2)
    if visited[(amt1,amt2)]==true:
            return(WaterJugSolver(0,amt2)or
                   WaterJugSolver(amt1,0)or
                  (WaterJugSolver(amt1,amt2)or
                  (WaterJugSolver(amt1,jug2)or
                   (WaterJugSolver(amt1+min(amt2,(jug1-amt1)),
                                   amt2-min(amt2,(jug1-amt1)))or
                    (WaterJugSolver(amt1-min(amt1,(jug2-amt2)),
                                    amt2+min(amt1,(jug2-amt2))))))))
    else:
            return false
    def check():
            if(jug1<=aim)and(jug2<=aim):
                print("Not Possible")
                return true
            elif(jug1/2==jug2 or jug2/2==jug1)and(jug1!=aim and jug2!=aim):
                print("Not Possible")
                return true
            elif(aim%(math.gcd(jug1,jug2))!=0):
                print("Not Possible")
                return true
            result=ckeck();
            if result!=true:
                print("Steps: ")
                WaterJugSolver(0,0)
                
        