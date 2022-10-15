'''
This program will try to solve a calendar puzzle
kindly given by Diego Lieban at "Festival da Matemática 2022".

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

The objective of the game is to show the desired date while hiding all other days and months.
'''

import numpy as np
import progressbar

#Setting pieces
LETTERS = ('A','B','C','D','E','F','G','H')
ORIENTATIONS = ('N','S','E','W')
REFLECTIONS = ['+', '-']

class Piece:
    '''Set piece letter and orientation.'''

    def __init__(self, letter: str, orientation: str = 'N', reflection: str = '+'):
        '''
       Letters go from A to H

       Orientation can be N, S, E, W'''
        self.letter:str = letter
        self.orientation:str = orientation

        if letter == 'A':
            self.piece_matrix =np.matrix(
                               [[1,1],
                                [1,1],
                                [1,1],
                                [1,0]])

        if letter == 'B':
            self.piece_matrix =np.matrix(
                               [[1,1],
                                [1,1],
                                [1,1]])

        if letter == 'C':
            self.piece_matrix =np.matrix(
                               [[1,0],
                                [1,1],
                                [1,1],
                                [1,0]])

        if letter == 'D':
            self.piece_matrix =np.matrix(
                               [[1,1,0],
                                [1,1,0],
                                [1,1,1]])

        if letter == 'E':
            self.piece_matrix =np.matrix(
                               [[1,1,1,1],
                                [1,0,0,0],
                                [1,0,0,0],
                                [1,0,0,0]])

        if letter == 'F':
            self.piece_matrix =np.matrix(
                               [[0,1],
                                [0,1],
                                [1,1],
                                [1,1]])

        if letter == 'G':
            self.piece_matrix =np.matrix(
                               [[0,1,0],
                                [1,1,0],
                                [1,1,1]])

        if letter == 'H':
            self.piece_matrix =np.matrix(
                               [[1,1,1],
                                [1,0,0],
                                [1,0,0],
                                [1,0,0],
                                [1,0,0]])


        if orientation == 'W':
            self.rotate()

        if orientation == 'S':
            self.rotate()
            self.rotate()

        if orientation == 'E':
            self.rotate()
            self.rotate()
            self.rotate()

        if reflection == '-':
            self.reflect()

    def matrix(self):
        '''Return the matrix that represents the piece'''
        return self.piece_matrix

    def __str__(self):
        '''Define how a piece may be printed'''
        return str(self.matrix())

    def rotate(self):
        '''Rotate a piece pi/2 rad counterclockwise'''
        self.piece_matrix = np.rot90(self.piece_matrix)

    def reflect(self):
        '''Reflect a piece with respect to the y axis'''
        self.piece_matrix = np.flip(self.piece_matrix, 1)

    def shape(self):
        '''Return the shape of the matrix that represents the piece'''
        return self.matrix().shape

#Setting constants (optimization concerns)
EMPTY_MATRIX = np.matrix([])
NP_WHERE = np.where


#Setting a table matrix

TABLE = np.matrix(
        [["jan1","jan2","feb1","feb2","mar1","mar2","apr1","apr2" ],
         ["may1","may2","jun1","jun2","jul1","jul2","ago1","ago2" ],
         ["sep1","sep2","oct1","oct2","nov1","nov2","dec1","dec2" ],
         ['1'   ,'2'   ,'3'   ,'4'   ,'5'   ,'6'   ,'7'   ,'8'    ],
         ['9'   ,'10'  ,'11'  ,'12'  ,'13'  ,'14'  ,'15'  ,'16'   ],
         ['17'  ,'18'  ,'19'  ,'20'  ,'21'  ,'22'  ,'23'  ,'24'   ],
         ['25'  ,'26'  ,'27'  ,'28'  ,'29'  ,'30'  ,'31'  ,'NULL' ]], dtype=object)

#TABLE = np.matrix(
#        [["jan1","jan2","feb1","feb2","mar1","mar2","apr1","apr2" ],
#         ["may1","H"   ,"H"   ,"H"   ,"H"   ,"H"   ,"ago1","ago2" ],
#         ["sep1","H"   ,"oct1","oct2","nov1","nov1","dec1","dec2" ],
#         ['1'   ,'H'   ,'3'   ,'4'   ,'5'   ,'6'   ,'7'   ,'8'    ],
#         ['9'   ,'10'  ,'11'  ,'12'  ,'13'  ,'14'  ,'15'  ,'16'   ],
#         ['17'  ,'18'  ,'19'  ,'20'  ,'21'  ,'22'  ,'23'  ,'24'   ],
#         ['25'  ,'26'  ,'27'  ,'28'  ,'29'  ,'30'  ,'31'  ,'NULL' ]], dtype=object)



table = TABLE

#Select the chosen day
LAZY_DAY_INPUT = '13'

day_index = NP_WHERE(table == LAZY_DAY_INPUT)
day_index = tuple([day_index[0][0], day_index[1][0]])

#Select the chosen month
LAZY_MONTH_INPUT = "oct"

month_index = NP_WHERE(table == f"{LAZY_MONTH_INPUT}1")
month_index = tuple([month_index[0][0], month_index[1][0]])

DATE=(LAZY_DAY_INPUT, f"{LAZY_MONTH_INPUT}1", f"{LAZY_MONTH_INPUT}2")

#Progressbar
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
interaction = 0 

def check_table(piece: Piece, table: np.matrix, array: tuple):
    '''Check if an element from array is inside table_'''
    for row in range(table.shape[0]):
        for column in range(table.shape[1]):
            if piece.matrix()[row,column] == 1:
                if table[row,column] in array or table[row,column] in LETTERS or\
                   table[row,column] == 'NULL':
                    return False
                
            #Check if the date is right
            try:
                if table[row,column] == array[1]:
                    if table[row,column+1] == array[2]:
                        continue
                    else:
                        return False
            except IndexError:
                pass

    return True


def write_table(table: np.matrix):
    '''Write the resulted table on matrix.txt'''
    file = open("matrix.txt", "a", encoding="utf-8")
    file.write(str(np.vectorize(lambda x:f'{x:>4}')(table)))
    file.write('\n\n')
    file.close()



#Probably the ugliest code i've ever wrote in my life. i should be banned from using computers after this.


#Choosing piece
def choose_piece(letter_: str, table: np.matrix, interaction: int = -1):
    '''Choose where to put a piece'''

    if letter_ not in ['B', 'C', 'E']:
        for reflection in REFLECTIONS:
            for orientation_ in ORIENTATIONS:

                piece = Piece(letter_,orientation_, reflection)
                PIECE_SHAPE = piece.shape
                PIECE_MATRIX = piece.matrix

                reduced_table = EMPTY_MATRIX
                table = NP_WHERE(table==letter_, TABLE, table)

                #Choosing place for the piece
                for table_row in range(7-PIECE_SHAPE()[0]+1):
                    for table_column in range(8-PIECE_SHAPE()[1]+1):

                        #Check if the piece would cover some part of the date
                        reduced_table = table[table_row:table_row+PIECE_SHAPE()[0],table_column:table_column+PIECE_SHAPE()[1]]
                        
                        #Update Progressbar
                        if interaction >= 0:
                            interaction += 1
                            bar.update(interaction)

                        if check_table(piece, reduced_table, DATE):
                            reduced_table = NP_WHERE(PIECE_MATRIX()==1, letter_, reduced_table)
                        else:
                            reduced_table = EMPTY_MATRIX
                            continue

                        #Change table
                        table[table_row:table_row+PIECE_SHAPE()[0],table_column:table_column+PIECE_SHAPE()[1]] = reduced_table

                        if letter_ == 'H':
                            write_table(table)
                            return table, interaction

                        #Recursion with the next letter
                        temporary_table, interaction = choose_piece(LETTERS[LETTERS.index(letter_)+1], table, interaction)

                        if temporary_table.size == 0:
                            table = NP_WHERE(table==letter_, TABLE, table)
                            reduced_table = EMPTY_MATRIX
                            continue

                        table = temporary_table
                        break

                    if reduced_table.size == 0:
                        continue
                    break

                if reduced_table.size == 0:
                    continue
                break
            if reduced_table.size == 0:
                continue
            break

        if reduced_table.size == 0:
            table = NP_WHERE(table==letter_, TABLE, table)
            return EMPTY_MATRIX, interaction

        else:
            return table, interaction
    
    #B has only 2 orientations and no reflection
    elif letter_ == 'B':
        for orientation_ in ['N','W']:

            piece = Piece(letter_,orientation_)
            PIECE_SHAPE = piece.shape
            PIECE_MATRIX = piece.matrix

            reduced_table = EMPTY_MATRIX
            table = NP_WHERE(table==letter_, TABLE, table)

            #Choosing place for the piece
            for table_row in range(7-PIECE_SHAPE()[0]+1):
                for table_column in range(8-PIECE_SHAPE()[1]+1):

                    #Check if the piece would cover some part of the date
                    reduced_table = table[table_row:table_row+PIECE_SHAPE()[0],table_column:table_column+PIECE_SHAPE()[1]]

                    #Update Progressbar
                    if interaction >= 0:
                        interaction += 1
                        bar.update(interaction)

                    if check_table(piece, reduced_table, DATE):
                        reduced_table = NP_WHERE(PIECE_MATRIX()==1, letter_, reduced_table)
                    else:
                        reduced_table = EMPTY_MATRIX
                        continue

                    #Change table
                    table[table_row:table_row+PIECE_SHAPE()[0],table_column:table_column+PIECE_SHAPE()[1]] = reduced_table

                    #Recursion with the next letter
                    temporary_table, interaction = choose_piece(LETTERS[LETTERS.index(letter_)+1], table, interaction)

                    if temporary_table.size == 0:
                        table = NP_WHERE(table==letter_, TABLE, table)
                        reduced_table = EMPTY_MATRIX
                        continue

                    table = temporary_table
                    break

                if reduced_table.size == 0:
                    continue
                break

            if reduced_table.size == 0:
                continue
            break
        
        if reduced_table.size == 0:
            table = NP_WHERE(table==letter_, TABLE, table)
            return EMPTY_MATRIX, interaction

        else:
            return table, interaction

    #C and E have no reflection
    else:
        for orientation_ in ORIENTATIONS:

            piece = Piece(letter_,orientation_)
            PIECE_SHAPE = piece.shape
            PIECE_MATRIX = piece.matrix

            reduced_table = EMPTY_MATRIX
            table = NP_WHERE(table==letter_, TABLE, table)

            #Choosing place for the piece
            for table_row in range(7-PIECE_SHAPE()[0]+1):
                for table_column in range(8-PIECE_SHAPE()[1]+1):

                    #Check if the piece would cover some part of the date
                    reduced_table = table[table_row:table_row+PIECE_SHAPE()[0],table_column:table_column+PIECE_SHAPE()[1]]

                    #Update Progressbar
                    if interaction >= 0:
                        interaction += 1
                        bar.update(interaction)

                    if check_table(piece, reduced_table, DATE):
                        reduced_table = NP_WHERE(PIECE_MATRIX()==1, letter_, reduced_table)
                    else:
                        reduced_table = EMPTY_MATRIX
                        continue

                    #Change table
                    table[table_row:table_row+PIECE_SHAPE()[0],table_column:table_column+PIECE_SHAPE()[1]] = reduced_table

                    #Recursion with the next letter
                    temporary_table, interaction = choose_piece(LETTERS[LETTERS.index(letter_)+1], table, interaction)

                    if temporary_table.size == 0:
                        table = NP_WHERE(table==letter_, TABLE, table)
                        reduced_table = EMPTY_MATRIX
                        continue

                    table = temporary_table
                    break

                if reduced_table.size == 0:
                    continue
                break

            if reduced_table.size == 0:
                continue
            break

        if reduced_table.size == 0:
            table = NP_WHERE(table==letter_, TABLE, table)
            return EMPTY_MATRIX, interaction

        else:
            return table, interaction


table, interaction = choose_piece('A', table, interaction)
print(np.vectorize(lambda x:f'{x:>4}')(table))
