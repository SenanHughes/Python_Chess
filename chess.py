#Chess Game
import random, string, colorama
from colorama import Fore

theBoard = {}
count = 1
for letters in string.ascii_uppercase[:8]:
    for count in range(1,9):
        theBoard[letters + str(count)] = ' '
        count += 1

blackPieces = {1: Fore.BLUE + 'R',2: Fore.BLUE + 'H', 3: Fore.BLUE + 'B', 4: Fore.BLUE + 'Q', 5: Fore.BLUE + 'K'\
               , 6:Fore.BLUE + 'B', 7: Fore.BLUE + 'H', 8: Fore.BLUE + 'R', 9: Fore.BLUE + 'P', 10: Fore.BLUE + 'P'\
               , 11: Fore.BLUE + 'P', 12: Fore.BLUE + 'P', 13: Fore.BLUE + 'P', 14:Fore.BLUE + 'P', 15: Fore.BLUE + 'P'\
               , 16:Fore.BLUE + 'P'}
whitePieces = {1: Fore.WHITE + 'R',2: Fore.WHITE + 'H', 3: Fore.WHITE + 'B', 4: Fore.WHITE + 'Q', 5: Fore.WHITE + 'K'\
               , 6:Fore.WHITE + 'B', 7: Fore.WHITE + 'H', 8: Fore.WHITE + 'R', 9: Fore.WHITE + 'P', 10: Fore.WHITE + 'P'\
               , 11: Fore.WHITE + 'P', 12: Fore.WHITE + 'P', 13: Fore.WHITE + 'P', 14:Fore.WHITE + 'P', 15: Fore.WHITE + 'P'\
               , 16:Fore.WHITE + 'P'}

countVal = 1
for count in range(1,3):
    for letters in string.ascii_uppercase[:8]:
        theBoard[letters + str(count)] = whitePieces[countVal]
        countVal += 1

countVal = 1
for count in range(8,6,-1):
    for letters in string.ascii_uppercase[:8]:
        theBoard[letters + str(count)] = blackPieces[countVal]
        countVal += 1

def printBoard(board):
    print('| A | B | C | D | E | F | G | H |')
    print('----------------------------------')
    print('| ' + board['A8'] + Fore.WHITE + ' | ' + board['B8'] + Fore.WHITE + ' | ' + board['C8']+ Fore.WHITE + ' | ' + board['D8'] + Fore.WHITE + ' | ' + board['E8'] + Fore.WHITE + ' | ' + board['F8'] + Fore.WHITE +\
          ' | ' + board['G8'] + Fore.WHITE + ' | ' + board['H8'] + Fore.WHITE + ' |8')
    print('----------------------------------')
    print('| ' + board['A7'] + Fore.WHITE + ' | ' + board['B7'] + Fore.WHITE + ' | ' + board['C7']+ Fore.WHITE + ' | ' + board['D7'] + Fore.WHITE + ' | ' + board['E7'] + Fore.WHITE + ' | ' + board['F7'] + Fore.WHITE +\
          ' | ' + board['G7'] + Fore.WHITE + ' | ' + board['H7'] + Fore.WHITE + ' |7')
    print('----------------------------------')
    print('| ' + board['A6'] + Fore.WHITE + ' | ' + board['B6'] + Fore.WHITE + ' | ' + board['C6']+ Fore.WHITE + ' | ' + board['D6'] + Fore.WHITE + ' | ' + board['E6'] + Fore.WHITE + ' | ' + board['F6'] + Fore.WHITE +\
          ' | ' + board['G6'] + Fore.WHITE + ' | ' + board['H6'] + Fore.WHITE + ' |6')
    print('----------------------------------')
    print('| ' + board['A5'] + Fore.WHITE + ' | ' + board['B5'] + Fore.WHITE + ' | ' + board['C5']+ Fore.WHITE + ' | ' + board['D5'] + Fore.WHITE + ' | ' + board['E5'] + Fore.WHITE + ' | ' + board['F5'] + Fore.WHITE +\
          ' | ' + board['G5'] + Fore.WHITE + ' | ' + board['H5'] + Fore.WHITE + ' |5')
    print('----------------------------------')
    print('| ' + board['A4'] + Fore.WHITE + ' | ' + board['B4'] + Fore.WHITE + ' | ' + board['C4']+ Fore.WHITE + ' | ' + board['D4'] + Fore.WHITE + ' | ' + board['E4'] + Fore.WHITE + ' | ' + board['F4'] + Fore.WHITE +\
          ' | ' + board['G4'] + Fore.WHITE + ' | ' + board['H4'] + Fore.WHITE + ' |4')
    print('----------------------------------')
    print('| ' + board['A3'] + Fore.WHITE + ' | ' + board['B3'] + Fore.WHITE + ' | ' + board['C3']+ Fore.WHITE + ' | ' + board['D3'] + Fore.WHITE + ' | ' + board['E3'] + Fore.WHITE + ' | ' + board['F3'] + Fore.WHITE +\
          ' | ' + board['G3'] + Fore.WHITE + ' | ' + board['H3'] + Fore.WHITE + ' |3')
    print('----------------------------------')
    print('| ' + board['A2'] + Fore.WHITE + ' | ' + board['B2'] + Fore.WHITE + ' | ' + board['C2']+ Fore.WHITE + ' | ' + board['D2'] + Fore.WHITE + ' | ' + board['E2'] + Fore.WHITE + ' | ' + board['F2'] + Fore.WHITE +\
          ' | ' + board['G2'] + Fore.WHITE + ' | ' + board['H2'] + Fore.WHITE + ' |2')
    print('----------------------------------')
    print('| ' + board['A1'] + Fore.WHITE + ' | ' + board['B1'] + Fore.WHITE + ' | ' + board['C1']+ Fore.WHITE + ' | ' + board['D1'] + Fore.WHITE + ' | ' + board['E1'] + Fore.WHITE + ' | ' + board['F1'] + Fore.WHITE +\
          ' | ' + board['G1'] + Fore.WHITE + ' | ' + board['H1'] + Fore.WHITE + ' |1')
    print('----------------------------------')


printBoard(theBoard)

print('Please pick a piece to move using grid references.')
pieceSelect = input().upper()
while theBoard[pieceSelect] == ' ':
    print('Please pick a piece to move using grid references.')
    pieceSelect = input().upper()

print('Please pick the space to move to.')
moveSelect = input().upper()
theBoard[moveSelect] = theBoard[pieceSelect]
theBoard[pieceSelect] = ' '
printBoard(theBoard)

if theBoard['A8'] == blackPieces[1]:
    print('Yes')

if theBoard['A8'] in blackPieces.values():
    print('Also Yes')

if theBoard['A8'] not in whitePieces.values():
    print('This may work')
