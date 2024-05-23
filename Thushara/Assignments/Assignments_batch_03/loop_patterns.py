"""
   * * *
 *       *
 *       *
 *       *
 *       *
 *       *
   * * *
"""
for i in range(7):
    for j in range(5):
        if (0<j<4) and (i==0 or i==6):
            print("*", end=" " )
        elif(0<i<6) and(j==0 or j==4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# first part
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")

# second part
print()
for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Third part
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")
'''
"""
* * * * * *
* * * * * *
    * *
    * *
    * *
    * *
"""
print("#"*50)
for i in range(6):
    for j in range(6):
        if i == 0 or i == 1:
            print("*",end=" ")
        elif (1 < i < 6) and (j == 2 or j == 3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
  * * *
*       *
*       *
*       *
* * * * *
*       *
*       *
*       *  
"""
print("#"*50)
for i in range(8):
    for j in range(5):
        if(0<i<=7) and (j==0 or j==4):
            print("*",end=" ")
        elif(0<j<4) and(i==0 or i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""

  * *   * * * * * 
  * *   * * * * * 
  * *   * * 
  * * * * * * * *
  * * * * * * * *
        * *   * *
  * * * * *   * *
  * * * * *   * *
"""
print("#"*50)
for i in range(8):
    for j in range(8):
        if (i==0 or i==1) and (j==2):
            print(" ",end=" ")
        elif i==2 and(j==2 or j>4):
            print(" ", end=" ")
        elif i==5 and(j<3 or j==5):
            print(" ", end=" ")
        elif (i==6 or i==7) and j==5:
            print(" ", end=" ")
        else:
            print("*", end=" ")

    print()
print("#"*120)
"""
# # # # # # # # # #           # #           #   # # # # #   #           #   # # # # #     # # # # #     # # # # #                 
        #         #           # #           # #             #           # #           # #           # #           #               
        #         #           # #           # #             #           # #           # #           # #           #               
        #         # # # # # # # #           #   # # # # #   # # # # # # # # # # # # # # # # # # # #   # # # # # # #               
        #         #           # #           #             # #           # #           # #           # #           #               
        #         #           # #           #             # #           # #           # #           # #           #               
        #         #           #   # # # # #     # # # # #   #           # #           # #           # #           #               

"""
for i in range(7):
    for j in range(0,65):
        if i==0 and j<9:
            print("#",end=" ")
        elif j==4 and i>0:
            print("#",end=" ")
        elif (j==9 or j==15) and i<7:
            print("#", end=" ")
        elif i==3 and 9<j<15:
            print("#", end=" ")
        elif (j==16 or j==22) and i<6:
            print("#", end=" ")
        elif i==6 and 16<j<22:
            print("#", end=" ")
        elif(i==0 or i==3 or i==6) and (23<j<29):
            print("#", end=" ")
        elif j==23 and (0<i<3):
            print("#", end=" ")
        elif j == 29 and (3 < i < 6):
            print("#", end=" ")
        elif (j==30 or j==36) and i<7:
            print("#", end=" ")
        elif i==3 and 30<j<36:
            print("#", end=" ")
        elif i==0 and(37<j<43):
            print("#",end=" ")

        elif (j==37 or j==43) and 0<i<7:
            print("#", end=" ")
        elif i==3 and 37<j<43:
            print("#", end=" ")
        elif i==0 and(44<j<50):
            print("#",end=" ")

        elif (j==44 ) and 0<=i<7:
            print("#", end=" ")
        elif j==50 and ((0<i<3) or(3<i<7)):
            print("#",end=" ")
        elif i==3 and 44<j<50:
            print("#", end=" ")
        elif i==0 and(51<j<57):
            print("#",end=" ")

        elif (j==51 or j==57) and 0<i<7:
            print("#", end=" ")
        elif i==3 and 51<j<57:
            print("#", end=" ")
        else:
            print(" ", end=" ")

    print()