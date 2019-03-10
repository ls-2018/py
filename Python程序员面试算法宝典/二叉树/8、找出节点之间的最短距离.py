"""
        1
      2    3
    4   5 6  7
Dist(4,5)=2
Dist(4,6)=4


------------>
Dist(n1,n2) = Dist(root,n1) + Dist(root,n2) - 2*Dist(root,parent)
parent 为 n1,n2最低的公共父结点

"""