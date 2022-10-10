This program will try to solve a calendar puzzle
kindly given by Diego Lieban at "Festival da Matemática 2022".

<img src="https://user-images.githubusercontent.com/48142996/194793072-a5b74fb1-ec41-419a-8d0a-36c1ff42509c.jpeg" width=50% height=50%>

> 9 Oct displayed on image


The table size is 7x8, without the (7,8) coordinate

```
++++++++ 
++++++++ 
++++++++ 
######## 
######## 
######## 
####### 
```

Where each "++" stands for the month in sequence (Jan, Feb, Mar, etc),
and each "#" stands for a number, starting from 1 until 31, in order.

There are 8 different pieces in total:
```
A:
##  ###   #    ###  ##  ####  #    ###  
##  ####  ##  ####  ##  ###   ##  ####  
##        ##        ##        ##        
#         ##         #        ##

B:
##  ###
##  ###
##

C:
#    #  ####   ##
##  ##   ##   ####
##  ##
#    #

D:
##     #  ###  ###   ##  ###  ###  #
##   ###   ##  ###   ##  ###  ##   ###
###  ###   ##  #    ###    #  ##   ### 

E:
####  #        #  ####
#     #        #     #
#     #        #     #
#     ####  ####     #

F:
 #  ##    ##  ####  #   ####  ##    ##
 #  ####  ##    ##  #   ##    ##  ####
##        #         ##         #    
##        #         ##         #   

G:
 #   ##   ###    #   #   #    ###   ## 
##   ###   ##  ###   ##  ###  ##   ###
###  #     #    ##  ###  ##    #     #

H:
###  #        #  #####  ###      #  #    #####
#    #        #      #    #      #  #    #   
#    #####    #      #    #  #####  #    #
#             #           #         #
#           ###           #         ###
```
The objective of the game is to show the desired date while hiding all other days and months.
