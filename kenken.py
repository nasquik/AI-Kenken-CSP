import csp
import time


def easy3x3():

    info = {}
    cages = [((0, 0), (0, 1), (1, 1)), ((0, 2),), ((1, 0), (2, 0), (2, 1)), ((1, 2), (2, 2))]

    info[cages[0]] = ("*", 3)
    info[cages[1]] = ("None", 2)
    info[cages[2]] = ("+", 7)
    info[cages[3]] = ("/", 3)

    size = 3

    return(tuple(cages), info, size)


def hard5x5():

    info = {}
    cages = [((0, 0), (0, 1), (0, 2)), ((0, 3), (0, 4)), ((1, 0), (2, 0), (2, 1)), ((1, 1),), ((1, 2), (2, 2)),
             ((1, 3), (1, 4), (2, 3)), ((2, 4), (3, 4), (4, 4)), ((3, 0), (4, 0)), ((3, 1), (4, 1)), ((3, 2), (3, 3)),
             ((4, 2), (4, 3))]

    info[cages[0]] = ("+", 6)
    info[cages[1]] = ("-", 1)
    info[cages[2]] = ("*", 40)
    info[cages[3]] = ("None", 3)
    info[cages[4]] = ("-", 2)
    info[cages[5]] = ("+", 6)
    info[cages[6]] = ("+", 10)
    info[cages[7]] = ("+", 6)
    info[cages[8]] = ("+", 5)
    info[cages[9]] = ("/", 2)
    info[cages[10]] = ("-", 1)

    size = 5

    return(tuple(cages), info, size)


def given6x6():

    info = {}
    cages = [((0, 0), (1, 0)), ((0, 1), (0, 2)), ((1, 1), (1, 2)), ((0, 3), (1, 3)), ((0, 4), (0, 5), (1, 5),
             (2, 5)), ((1, 4), (2, 4)), ((2, 0), (2, 1), (3, 0), (3, 1)), ((2, 2), (2, 3)), ((4, 0), (4, 1)), ((3, 2),
             (4, 2)), ((3, 3), (4, 3), (4, 4)), ((3, 4), (3, 5)), ((4, 5), (5, 5)), ((5, 0), (5, 1), (5, 2)), ((5, 3),
             (5, 4))]

    info[cages[0]] = ("+", 11)
    info[cages[1]] = ("/", 2)
    info[cages[2]] = ("-", 3)
    info[cages[3]] = ("*", 20)
    info[cages[4]] = ("*", 6)
    info[cages[5]] = ("/", 3)
    info[cages[6]] = ("*", 240)
    info[cages[7]] = ("*", 6)
    info[cages[8]] = ("*", 6)
    info[cages[9]] = ("*", 6)
    info[cages[10]] = ("+", 7)
    info[cages[11]] = ("*", 30)
    info[cages[12]] = ("+", 9)
    info[cages[13]] = ("+", 8)
    info[cages[14]] = ("/", 2)

    size = 6

    return(tuple(cages), info, size)


def expert9x9():

    info = {}
    cages = [((0, 0), (1, 0), (2, 0)), ((0, 1), (0, 2)), ((0, 3), (0, 4)), ((0, 5), (1, 5)), ((0, 6), (0, 7)),
             ((0, 8), (1, 8)), ((1, 1), (2, 1)), ((1, 2), (1, 3)), ((1, 4),), ((1, 6), (1, 7), (2, 7), (3, 7)),
             ((2, 2), (2, 3)), ((2, 4), (2, 5)), ((2, 6), (3, 6)), ((2, 8), (3, 8), (4, 8)),
             ((3, 0), (3, 1), (4, 0), (5, 0)), ((3, 2), (3, 3), (4, 2)), ((3, 4), (3, 5)), ((4, 1), (5, 1)),
             ((4, 3), (4, 4), (5, 3)), ((4, 5), (4, 6)), ((4, 7), (5, 6), (5, 7)), ((5, 2),), ((5, 4), (5, 5)),
             ((5, 8), (6, 8)), ((6, 0), (7, 0)), ((6, 1), (6, 2), (6, 3)), ((6, 4), (7, 4), (8, 4)),
             ((6, 5), (6, 6), (6, 7)), ((7, 1), (8, 0), (8, 1)), ((7, 2), (7, 3)), ((7, 5), (8, 5)), ((7, 6), (8, 6)),
             ((7, 7), (7, 8)), ((8, 2), (8, 3)), ((8, 7), (8, 8))]

    info[cages[0]] = ("+", 9)
    info[cages[1]] = ("*", 30)
    info[cages[2]] = ("-", 1)
    info[cages[3]] = ("-", 2)
    info[cages[4]] = ("-", 8)
    info[cages[5]] = ("-", 5)
    info[cages[6]] = ("-", 2)
    info[cages[7]] = ("/", 4)
    info[cages[8]] = ("None", 4)
    info[cages[9]] = ("+", 15)
    info[cages[10]] = ("-", 6)
    info[cages[11]] = ("-", 1)
    info[cages[12]] = ("-", 3)
    info[cages[13]] = ("+", 10)
    info[cages[14]] = ("+", 18)
    info[cages[15]] = ("+", 15)
    info[cages[16]] = ("+", 7)
    info[cages[17]] = ("*", 72)
    info[cages[18]] = ("*", 54)
    info[cages[19]] = ("-", 1)
    info[cages[20]] = ("*", 32)
    info[cages[21]] = ("None", 7)
    info[cages[22]] = ("/", 3)
    info[cages[23]] = ("-", 1)
    info[cages[24]] = ("-", 3)
    info[cages[25]] = ("+", 16)
    info[cages[26]] = ("*", 45)
    info[cages[27]] = ("*", 80)
    info[cages[28]] = ("*", 112)
    info[cages[29]] = ("/", 3)
    info[cages[30]] = ("-", 6)
    info[cages[31]] = ("-", 2)
    info[cages[32]] = ("+", 17)
    info[cages[33]] = ("-", 3)
    info[cages[34]] = ("/", 2)

    size = 9

    return(tuple(cages), info, size)


def createDomain(result, setrange, variable, vlength, vinfo):   # creates the domain
    n = len(setrange)
    createDomainRec(result, setrange, n, variable, vlength, vinfo, [])


def createDomainRec(result, setrange, setlength, variable, vlength, vinfo, mlist):  
    # determines values to go into domain

    op = vinfo[0]
    goal = vinfo[1]

    if (vlength == 0):
        # rejects a value when two cells with the same value are in the same row or column or when the
        # operation between the values in the cells don't result in the goal-number
        pairs = [(p1, p2) for p1 in range(len(variable)) for p2 in range(p1+1, len(variable))]
        for pair in pairs:
            if(((variable[pair[0]][0] == variable[pair[1]][0]) or (variable[pair[0]][1] == variable[pair[1]][1]))
               and (mlist[pair[0]] == mlist[pair[1]])):
                return

        if(op == "+"):
            nsum = 0
            for item in mlist:
                nsum = nsum + item
            if(nsum != goal):
                return
        elif(op == "*"):
            nprod = 1
            for item in mlist:
                nprod = nprod * item
            if(nprod != goal):
                return
        elif(op == "-"):
            Max = max(mlist)
            Min = min(mlist)
            ndiff = Max - Min
            if(ndiff != goal):
                return
        elif(op == "/"):
            Max = max(mlist)
            Min = min(mlist)
            nquot = Max / Min
            if(nquot != goal):
                return
        elif(op == "None"):
            if(mlist[0] != goal):
                return
        result.append(mlist)
        return

    for i in range(setlength):
        newList = list(mlist)
        newList.append(setrange[i])
        createDomainRec(result, setrange, setlength, variable, vlength - 1, vinfo, newList)


class KenKen(csp.CSP):

    def __init__(self, matrix):

        variables, self.info, self.size = matrix
        domains = {}
        neighbors = {}
        self.constraint_calls = 0

        setrange = list(range(1, self.size+1))      # setrange = [1,....., size]

        # create Domains dictionary
        for i in variables:
            result = []
            createDomain(result, setrange, i, len(i), self.info[i])
            domains[i] = result

        # create Neighbors dictionary
        for i in variables:
            temp = []
            for j in variables:
                if(j != i):
                    for item1 in i:
                        for item2 in j:
                            if(item1[0] == item2[0] or item1[1] == item2[1]):
                                temp.append(j)
            neighbors[i] = temp

        csp.CSP.__init__(self, variables, domains, neighbors, self.all_different_constraint)

    def all_different_constraint(self, A, a, B, b):
        # if cages A, B contain cells with the same value, they cannot be in the same row or column

        # increment number of times this function is called
        self.constraint_calls += 1

        pairs = [(p1, p2) for p1 in range(len(A)) for p2 in range(len(B))]
        for pair in pairs:
            if(A[pair[0]][0] == B[pair[1]][0] or A[pair[0]][1] == B[pair[1]][1]):
                if(a[pair[0]] == b[pair[1]]):
                    return False
        return True

    def displayMatrix(self, solution):

        w = self.size
        h = self.size

        MatrixBefore = [[0 for x in range(w)] for y in range(h)]
        MatrixAfter = [[0 for x in range(w)] for y in range(h)]

        for key in self.info.keys():
            temp = self.info[key]
            for pair in key:
                if(temp[0] == "None"):
                    MatrixBefore[pair[0]][pair[1]] = str(temp[1])
                else:
                    MatrixBefore[pair[0]][pair[1]] = str(temp[1]) + temp[0]

        print("This is the Puzzle:")
        # places operation agent, goal-number in the cells belonging to the same cage
        for i in range(len(MatrixBefore)):
            for j in range(len(MatrixBefore[i])):
                print(MatrixBefore[i][j], end="\t")
            print(end="\n")
        print(end="\n")

        if solution:
            print("This is the Solution: ")
            # prints value attributed to each cell
            for key in solution.keys():
                temp = solution[key]
                for item in range(len(key)):
                    MatrixAfter[key[item][0]][key[item][1]] = str(temp[item])

            for i in range(len(MatrixAfter)):
                for j in range(len(MatrixAfter[i])):
                    print(MatrixAfter[i][j], end="\t")
                print(end="\n")
            print(end="\n")
        else:
            print("No solution found :(")


print("Available Puzzles:")
print("1. Easy 3x3")
print("2. Hard 5x5")
print("3. Given 6x6")
print("4. Expert 9x9")

puzzle = input("Please select the puzzle you want to solve(1,2,3,4): ")
puzzle = int(puzzle)
print(end="\n")

print("Algorithms: ")
print("1. BT")
print("2. BT+MRV")
print("3. FC")
print("4. FC+MRV")
print("5. MAC")
print("6. min_conflicts")

algorithm = input("Please select the algorithm you want to run(1,2,3,4, 5, 6): ")
algorithm = int(algorithm)
print(end="\n")

start = time.time()

if(puzzle == 1):
    kenken = KenKen(easy3x3())
elif(puzzle == 2):
    kenken = KenKen(hard5x5())
elif(puzzle == 3):
    kenken = KenKen(given6x6())
else:
    kenken = KenKen(expert9x9())

solution = []

if(algorithm == 1):
    solution = csp.backtracking_search(kenken)
elif(algorithm == 2):
    solution = csp.backtracking_search(kenken, select_unassigned_variable=csp.mrv)
elif(algorithm == 3):
    solution = csp.backtracking_search(kenken, inference=csp.forward_checking)
elif(algorithm == 4):
    solution = csp.backtracking_search(kenken, select_unassigned_variable=csp.mrv, inference=csp.forward_checking)
elif(algorithm == 5):
    solution = csp.backtracking_search(kenken, inference=csp.mac)
else:
    solution = csp.min_conflicts(kenken)

kenken.displayMatrix(solution)


end = time.time()
elapsed_time = end - start
print("Elapsed Time:", elapsed_time)
print("nassigns:", kenken.nassigns)
print("Constraint Calls:", kenken.constraint_calls)
