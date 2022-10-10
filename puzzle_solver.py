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


from time import time
import numpy as np

#Setting pieces
LETTERS = ('A','B','C','D','E','F','G','H')
letters_left = [1,1,1,1,1,1,1,1]
ORIENTATIONS = ('N','S','E','W')
REFLECTIONS = ['+', '-']

class Piece:
    '''Set piece letter and orientation.'''

    def __init__(self, letter: str, orientation: str = 'N', reflection: str = '+'):
        '''
       Letters go from A to H

       Orientation can be N, S, E, W'''
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



#Setting a table matrix

TABLE = np.matrix(
        [["jan1","jan2","feb1","feb2","mar1","mar2","apr1","apr2" ],
         ["may1","may2","jun1","jun2","jul1","jul2","ago1","ago2" ],
         ["sep1","sep2","out1","out2","nov1","nov2","dec1","dec2" ],
         ['1'   ,'2'   ,'3'   ,'4'   ,'5'   ,'6'   ,'7'   ,'8'    ],
         ['9'   ,'10'  ,'11'  ,'12'  ,'13'  ,'14'  ,'15'  ,'16'   ],
         ['17'  ,'18'  ,'19'  ,'20'  ,'21'  ,'22'  ,'23'  ,'24'   ],
         ['25'  ,'26'  ,'27'  ,'28'  ,'29'  ,'30'  ,'31'  ,'NULL' ]], dtype=object)

#TABLE = np.matrix(
#        [["jan1","jan2","feb1","feb2","mar1","mar2","apr1","apr2" ],
#         ["may1","H","H","H","H","H","ago1","ago2" ],
#         ["sep1","H","out1","out2","nov1","nov1","dec1","dec2"],
#         ['1','H','3'   ,'4'   ,'5','6','7','8'],
#         ['9','10','11' ,'12'  ,'13','14','15','16'],
#         ['17','18','19','20','21','22','23'  ,'24'   ],
#         ['25','26','27','28','29','30','31'  ,'NULL' ]], dtype=object)




table = TABLE

#print(table)
#Select the chosen day
LAZY_DAY_INPUT = '28'

day_index = np.where(table == LAZY_DAY_INPUT)
day_index = tuple([day_index[0][0], day_index[1][0]])
#print(day_index)

#Select the chosen month
LAZY_MONTH_INPUT = "out"

month_index = np.where(table == f"{LAZY_MONTH_INPUT}1")
month_index = tuple([month_index[0][0], month_index[1][0]])
#print(month_index)

DATE=(LAZY_DAY_INPUT, f"{LAZY_MONTH_INPUT}1", f"{LAZY_MONTH_INPUT}2")
#DATE=()

#NUMBERS_STR = [str(x) for x in range(1,32)]


def check_table(piece, table, array, letter):
    '''Check if an element from array is inside table_'''
    for row in range(table.shape[0]):
        for column in range(table.shape[1]):
            if piece.matrix()[row,column] == 1:
                if table[row,column] in array or table[row,column] in LETTERS or\
                   table[row,column] == 'NULL':
                    return False

    return True


def write_table(table):
    '''Check if it is a valid table and save it'''
    valid = 0
    for row in range(TABLE.shape[0]):
        for column in range(TABLE.shape[1]):
            if table[row,column] not in LETTERS and table[row,column] != 'NULL':
                valid +=1
    print(valid, 'valid')
    if valid == 3:
        print(table)
        file = open("matrix.txt", "a", encoding="utf-8")
        file.write(str(table))
        file.write('\n\n')
        file.close()



#Probably the ugliest code i've ever wrote in my life. i should be banned from using computers after this.

#log = []

#Choosing piece
def choose_piece(letter_, table):
    '''Choose where to put a piece'''
    #print (letters_left)
    #print(letter_)

    if letter_ not in ['B', 'C', 'E']:
        for reflection in REFLECTIONS:
            for orientation_ in ORIENTATIONS:

                piece = Piece(letter_,orientation_, reflection)
                print(piece.matrix(), 'peca matrix', orientation_, reflection)
                reduced_table = np.matrix([])
                table = np.where(table==letter_, TABLE, table)
                #print(table)

                #Choosing place for the piece
                for table_row in range(7-piece.shape()[0]+1):
                    for table_column in range(8-piece.shape()[1]+1):

                        #Check if the piece would cover some part of the date
                        reduced_table = table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]]

                        if check_table(piece, reduced_table, DATE, letter_):
                            reduced_table = np.where(piece.matrix()==1, letter_, reduced_table)
                        else:
                            #print('oi')
                            reduced_table = np.matrix([])
                            continue

                        #Change table
                        table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]] = reduced_table
                        print(table)
                        #log.append([letter_, orientation_, table_row, table_column])
                        #write_table(table)
                        #print()
                        #print(log)
                        #print()

                        if letter_ == 'H':
                            write_table(table)
                            print(table, 'FINAL')
                            return table

                        #Recursion with the next letter
                        print("proxima recursao", letter_)
                        temporary_table = choose_piece(LETTERS[LETTERS.index(letter_)+1], table)
                        #print(table, 'table!')
                        #print(choose_piece(LETTERS[LETTERS.index(letter_)+1], table), 'funcao oi')
                        #print(temporary_table, 'oi')

                        if temporary_table.size == 0:
                            table = np.where(table==letter_, TABLE, table)
                            reduced_table = np.matrix([])
                            continue

                        table = temporary_table
                        break

                        #write_table(table)

                    #print(table)
                    if reduced_table.size == 0:
                        continue
                    break
                #print(table)
                if reduced_table.size == 0:
                    continue
                break
            if reduced_table.size == 0:
                print('-')
                print('reflection', reflection)
                continue
            break
            #print(table)
        if reduced_table.size == 0:
            table = np.where(table==letter_, TABLE, table)
            return np.matrix([])

        else:
            #print(table)
            return table
    
    #B has only 2 orientations and no reflection
    elif letter_ == 'B':
        for orientation_ in ['N','W']:

            piece = Piece(letter_,orientation_, reflection)
            print(piece.matrix(), 'peca matrix', orientation_, reflection)
            reduced_table = np.matrix([])
            table = np.where(table==letter_, TABLE, table)
            #print(table)

            #Choosing place for the piece
            for table_row in range(7-piece.shape()[0]+1):
                for table_column in range(8-piece.shape()[1]+1):

                    #Check if the piece would cover some part of the date
                    reduced_table = table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]]

                    if check_table(piece, reduced_table, DATE, letter_):
                        reduced_table = np.where(piece.matrix()==1, letter_, reduced_table)
                    else:
                        #print('oi')
                        reduced_table = np.matrix([])
                        continue

                    #Change table
                    table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]] = reduced_table
                    print(table)
                    #log.append([letter_, orientation_, table_row, table_column])
                    #write_table(table)
                    #print()
                    #print(log)
                    #print()

                    if letter_ == 'H':
                        write_table(table)
                        print(table, 'FINAL')
                        return table

                    #Recursion with the next letter
                    print("proxima recursao", letter_)
                    temporary_table = choose_piece(LETTERS[LETTERS.index(letter_)+1], table)
                    #print(table, 'table!')
                    #print(choose_piece(LETTERS[LETTERS.index(letter_)+1], table), 'funcao oi')
                    #print(temporary_table, 'oi')

                    if temporary_table.size == 0:
                        table = np.where(table==letter_, TABLE, table)
                        reduced_table = np.matrix([])
                        continue

                    table = temporary_table
                    break

                    #write_table(table)
                #print(table)
                if reduced_table.size == 0:
                    continue
                break
            if reduced_table.size == 0:
                print('-')
                print('reflection', reflection)
                continue
            break
            #print(table)
        if reduced_table.size == 0:
            table = np.where(table==letter_, TABLE, table)
            return np.matrix([])

        else:
            #print(table)
            return table

    #C and E have no reflection
    else:
        for orientation_ in ORIENTATIONS:

            piece = Piece(letter_,orientation_, reflection)
            print(piece.matrix(), 'peca matrix', orientation_, reflection)
            reduced_table = np.matrix([])
            table = np.where(table==letter_, TABLE, table)
            #print(table)

            #Choosing place for the piece
            for table_row in range(7-piece.shape()[0]+1):
                for table_column in range(8-piece.shape()[1]+1):

                    #Check if the piece would cover some part of the date
                    reduced_table = table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]]

                    if check_table(piece, reduced_table, DATE, letter_):
                        reduced_table = np.where(piece.matrix()==1, letter_, reduced_table)
                    else:
                        #print('oi')
                        reduced_table = np.matrix([])
                        continue

                    #Change table
                    table[table_row:table_row+piece.shape()[0],table_column:table_column+piece.shape()[1]] = reduced_table
                    print(table)
                    #log.append([letter_, orientation_, table_row, table_column])
                    #write_table(table)
                    #print()
                    #print(log)
                    #print()

                    if letter_ == 'H':
                        write_table(table)
                        print(table, 'FINAL')
                        return table

                    #Recursion with the next letter
                    print("proxima recursao", letter_)
                    temporary_table = choose_piece(LETTERS[LETTERS.index(letter_)+1], table)
                    #print(table, 'table!')
                    #print(choose_piece(LETTERS[LETTERS.index(letter_)+1], table), 'funcao oi')
                    #print(temporary_table, 'oi')

                    if temporary_table.size == 0:
                        table = np.where(table==letter_, TABLE, table)
                        reduced_table = np.matrix([])
                        continue

                    table = temporary_table
                    break

                    #write_table(table)
                #print(table)
                if reduced_table.size == 0:
                    continue
                break
            if reduced_table.size == 0:
                print('-')
                print('reflection', reflection)
                continue
            break
            #print(table)
        if reduced_table.size == 0:
            table = np.where(table==letter_, TABLE, table)
            return np.matrix([])

        else:
            #print(table)
            return table

beggining = time()
print(choose_piece('A', table))
print(time()-beggining)
