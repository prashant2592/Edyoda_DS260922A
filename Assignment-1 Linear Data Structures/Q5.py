#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n,source,destination,auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
TowerOfHanoi(4,'A','B','C')