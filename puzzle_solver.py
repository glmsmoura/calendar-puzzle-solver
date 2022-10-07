'''This program will try to solve a calendar puzzle kindly given by Diego Lieban at "Festival da Matemática 2022".

The table size is 7x8, without the (7,8) coordinate

++++++++
++++++++
++++++++
########
########
########
#######

Where each "++" stands for the month in sequence (Jan, Feb, Mar, etc),
and each "#" stands for a number, starting from 1 until 31, in order.

There are 8 different pieces in total:

A:
##  ###   #    ###
##  ####  ##  ####
##        ##
#         ##

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
##     #  ###  ###
##   ###   ##  ###
###  ###   ##  #

E:
####  #        #  ####
#     #        #     #
#     #        #     #
#     ####  ####     #

F:
 #  ##    ##  ####
 #  ####  ##    ##
##        #
##        #

G:
 #   ##   ###    #
##   ###   ##  ###
###  #     #    ##

H:
###  #        #  #####
#    #        #      #
#    #####    #      #
#             #
#           ###

The objective of the game is to show the desired date while hiding all other days and months.
'''


import numpy as np

#Setting pieces
LETTERS = ('A','B','C','D','E','F','G','H')
letters_left = [1,1,1,1,1,1,1,1] 
ORIENTATIONS = ('N','S','L','O')

class Piece:
    '''Set piece letter and orientation.'''

    def __init__(self, letter: str, orientation: str = 'N'):
        '''  
       Letters go from A to H

       Orientation can be N, S, L, O'''
        self.letter = letter
        self.orientation = orientation

        if letter == 'A':
            self.piece_matrix =np.mat(
                               [[1,1],
                                [1,1],
                                [1,1],
                                [1,0]])
        
        if letter == 'B':
            self.piece_matrix =np.mat(
                               [[1,1],
                                [1,1],
                                [1,1]])

        if letter == 'C':
            self.piece_matrix =np.mat(
                               [[1,0],
                                [1,1],
                                [1,1],
                                [1,0]])
            
        if letter == 'D':
            self.piece_matrix =np.mat(
                                [[1,1,0],
                                [1,1,0],
                                [1,1,1]])
        
        if letter == 'E':
            self.piece_matrix =np.mat(
                               [[1,1,1,1],
                                [1,0,0,0],
                                [1,0,0,0],
                                [1,0,0,0]])
        
        if letter == 'F':
            self.piece_matrix =np.mat(
                               [[0,1],
                                [0,1],
                                [1,1],
                                [1,1]])

        if letter == 'G':
            self.piece_matrix =np.mat(
                               [[0,1,0],
                                [1,1,0],
                                [1,1,1]])

        if letter == 'H':
            self.piece_matrix =np.mat(
                               [[1,1,1],
                                [1,0,0],
                                [1,0,0],
                                [1,0,0],
                                [1,0,0]])


        if orientation == 'O':
            self.rotate()

        if orientation == 'S':
            self.rotate()
            self.rotate()

        if orientation == 'L':
            self.rotate()
            self.rotate()
            self.rotate()

    def matrix(self):
        '''Return the matrix that represents the piece'''
        return self.piece_matrix

    def __str__(self):
        '''Define how a piece may be printed'''
        return str(self.matrix())

    def rotate(self):
        '''Rotate a piece pi/2 rad counterclockwise'''
        self.piece_matrix = np.rot90(self.piece_matrix)

    def shape(self):
        '''Return the shape of the matrix that represents the piece'''
        return self.matrix().shape



#Setting a table matrix

table = np.matrix(
        [["jan1","jan2","feb1","feb2","mar1","mar2","apr1","apr2" ],
         ["may1","may2","jun1","jun2","jul1","jul2","ago1","ago2" ],
         ["sep1","sep2","out1","out2","nov1","nov2","dec1","dec2" ],
         ['1'   ,'2'   ,'3'   ,'4'   ,'5'   ,'6'   ,'7'   ,'8'    ],
         ['9'   ,'10'  ,'11'  ,'12'  ,'13'  ,'14'  ,'15'  ,'16'   ],
         ['17'  ,'18'  ,'19'  ,'20'  ,'21'  ,'22'  ,'23'  ,'24'   ],
         ['25'  ,'26'  ,'27'  ,'28'  ,'29'  ,'30'  ,'31'  ,'NULL' ]], dtype=object)

#Select the chosen day
LAZY_DAY_INPUT = '11'
day_index = np.where(table == LAZY_DAY_INPUT)
day_index = tuple([day_index[0][0], day_index[1][0]])
#print(day_index)

#Select the chosen month
LAZY_MONTH_INPUT = "jan"

month_index = np.where(table == f"{LAZY_MONTH_INPUT}1")
month_index = tuple([month_index[0][0], month_index[1][0]])
#print(month_index)

DATE=(LAZY_DAY_INPUT, f"{LAZY_MONTH_INPUT}1", f"{LAZY_MONTH_INPUT}2")


def check_table(table_, array):
    return any((element == table_).any() for element in array)

#Probably the ugliest code i've ever wrote in my life. i should be banned from using computers after this.

log = []

#Choosing piece
for letter_ in LETTERS:
    for orientation_ in ORIENTATIONS:
        piece = Piece(letter_,orientation_)
        
        #Choosing place for the piece
        for table_row in range(7-piece.shape()[0]):
            for table_column in range(8-piece.shape()[1]):
                #Check if the piece would cover some part of the date
                reduced_table = table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]]
                reduced_table = np.where(check_table(reduced_table, DATE),'D',reduced_table)
                reduced_table = np.where(check_table(reduced_table, LETTERS),'L',reduced_table)
                print(reduced_table)
                if any(D in table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]] for D in DATE) or\
                   any(L in table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]] for L in LETTERS) or\
                   'NULL' in table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]]:
                    continue
                else:
                    #Change table
                    print(table_row, piece.shape()[0])
                    reduced_table = table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]]
                    reduced_table = np.where(piece.matrix()==1,letter_,reduced_table)
                    log.append([letter_, orientation_, table_row, table_column])
                                


print(table)
print(log)

