def parse_bingo() -> tuple[list[str], list[list]] :
    with open('./input.txt', 'r') as file:
        bingoNums = file.readline().split(',')
        file.readline()
        boards = list(filter(lambda x: False if x=='\n' else True, file.readlines()))

    boards = list(map(list, zip(*[iter(boards)]*5)))
    boards = [[j.strip().split(' ') for j in i]for i in boards]

    for indx in range(len(boards)):
        for indxx in range(len(boards[indx])):
            boards[indx][indxx] = list(filter(lambda x: bool(x), boards[indx][indxx]))

    bingoNums = [i.strip() for i in bingoNums]
    return bingoNums, boards

def checkWinner(board: list[list]) -> bool:
    cboard = list(map(lambda x: True if 'h' in x else False, board.copy()))

    for i in cboard:
        # print(i)
        if i:
            return True

    # rotates the list 90 degrees
    cboard = list(zip(*board))[::-1]
    cboard = list(map(lambda x: True if 'h' in x else False, board.copy()))

    for i in cboard:
        if i:
            return True

    return False

def returnWinner(bingoNumbers: list[int], bingoBoards: list[list[list]]) -> list[list]:
    for ii in bingoNumbers:
        for i in bingoBoards:
            for j in i:
                for i2 in j:
                    if ii == i2:
                        j[j.index(i2)] = j[j.index(i2)] + 'h'

                if checkWinner(j):
                    return j

bingoNumbers, bingoBoards = parse_bingo()

winner = returnWinner(bingoNumbers, bingoBoards)

print(winner)