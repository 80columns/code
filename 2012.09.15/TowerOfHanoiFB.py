#!/usr/bin/python

'''
Facebook hiring sample test

There are K pegs. Each peg can hold discs in decreasing order of
radius when looked from bottom to top of the peg. There are N discs
which have radius 1 to N; Given the initial configuration of the pegs
and the final configuration of the pegs, output the moves required to
transform from the initial to final configuration. You are required to
do the transformations in minimal number of moves.

A move consists of picking the topmost disc of any one of the pegs and
placing it on top of anyother peg. At anypoint of time, the decreasing
radius property of all the pegs must be maintained.


Constraints:
1 <= N <=8
3 <= K <=5


Input Format:
N K
2nd line contains N integers.
Each integer in the second line is in the range 1 to K where the i-th
integer denotes the peg to which disc of radius i is present in the
initial configuration.
3rd line denotes the final configuration in a format similar to the
initial configuration.


Output Format:
The first line contains M - The minimal number of moves required to
complete the transformation. The following M lines describe a move, by
a peg number to pick from and a peg number to place on. If there are
more than one solutions, it's sufficient to output any one of them.
You can assume, there is always a solution with less than 7 moves and
the initial configuration will not be same as the final one.


Sample Input #00:
2 3
1 1
2 2

Sample Output #00:
3
1 3
1 2
3 2


Sample Input #01:
6 4
4 2 4 3 1 1
1 1 1 1 1 1

Sample Output #01:
5
3 1
4 3
4 1
2 1
3 1


NOTE: You need to write the full code taking all inputs from stdin
and outputs to stdout. If you are using "Java", the classname is
"Solution"
'''

import sys

class ReachedFinalConfig(Exception):
    pass

class ConfigNode:
    Config = []
    ParentIndex = 0

    def __init__(self, NewConfig, NewParentIndex):
        self.Config = NewConfig
        self.ParentIndex = NewParentIndex

    def SetConfig(self, NewConfig):
        self.Config = NewConfig

    def GetConfig(self):
        return self.Config

    def SetParentIndex(self, NewParentIndex):
        self.ParentIndex = NewParentIndex

    def GetParentIndex(self):
        return self.ParentIndex

# This function takes two configurations
# and returns whether they are equivalent
def CompareConfigs(Config1, Config2):
    # Compare the config lengths first
    if len(Config1) != len(Config2):
        return False

    # Compare each individual element
    for I in range(0, len(Config1)):
        if Config1[I] != Config2[I]:
            return False

    return True

# This function determines whether a given
# configuration is already in the list of
# configurations
def ConfigAlreadyExists(NewConfig, Configs):
    for I in range(0, len(Configs)):
        if Configs[I].GetConfig() == NewConfig:
            return True

    return False

def main():
    # Read the three input lines from stdin
    NK = sys.stdin.readline().rstrip('\n')
    Config = sys.stdin.readline().rstrip('\n').split(" ")
    EndConfig = sys.stdin.readline().rstrip('\n').split(" ")

    Configs = []
    Config = [int(I) for I in Config]
    EndConfig = [int(I) for I in EndConfig]
    NumDiscs = int(NK.split(" ")[0])
    NumPegs = int(NK.split(" ")[1])
    ParentIndex = 0

    # Create the first node in the config list
    Configs.append(ConfigNode(Config, -1))

    # Until the final configuration is reached
    #     For each disc in the config from left to right:
    #         If the disc can be moved, proceed to check
    #         which pegs it could be moved to and create
    #         new configurations for each of those pegs
    #
    #         For each peg:
    #             If the disc has no discs to the left of it on
    #             the current peg, create a new config with the
    #             disc moved to that peg
    try:
        while 1:
            Config = Configs[ParentIndex].GetConfig()[:]

            for I in range(0, NumDiscs):
                DiscIsTopDisc = True

                # If the disc has another disc on top of it, we cannot
                # move it so there is no point in checking which pegs
                # the disc could be moved to
                for K in range(0, I):
                    if Config[K] == Config[I]:
                        DiscIsTopDisc = False

                if DiscIsTopDisc == True:
                    for J in range(0, NumPegs):
                        # If the current disc is already on the peg
                        # being considered, don't create a duplicate
                        # config
                        if Config[I] == (J + 1):
                            continue

                        PegIsOccupiedToLeft = False

                        for K in range(0, I):
                            if Config[K] == (J + 1):
                                PegIsOccupiedToLeft = True

                        # If the current disc can be moved to the
                        # current peg, then create a new configuration
                        # with that move
                        if PegIsOccupiedToLeft == False:
                            NewConfig = Config[:]
                            NewConfig[I] = (J + 1)

                            # If the final configuration has been
                            # reached, add the final configuration to
                            # the list of configurations and stop
                            # creating new configurations
                            if CompareConfigs(NewConfig, EndConfig) \
                               == True:

                                Configs.append( \
                                    ConfigNode(NewConfig[:], \
                                    ParentIndex))
                                raise ReachedFinalConfig

                            # Make sure that the new configuration is
                            # not the same as any previous
                            # configurations. This prevents duplicate
                            # configurations from being created.
                            else:
                                if ConfigAlreadyExists(NewConfig,
                                   Configs) == False:
                                    # Append a new configuration to
                                    # the list
                                    Configs.append(ConfigNode( \
                                                   NewConfig[:],
                                                   ParentIndex))

            # Start creating configurations from the next
            # configuration in the list
            ParentIndex += 1

    # If the final configuration has been reached, continue on to
    # print the answer
    except ReachedFinalConfig:
        pass

    # Travel from the final configuration to the starting
    # configuration by traversing the parent indexes. As the path is
    # traversed, add each move between configs to the beginning of
    # the list of moves
    Index = len(Configs) - 1
    NumMoves = 0
    Moves = ""
    while Index != 0:
        NumMoves += 1
        Config1 = Configs[Index].GetConfig()
        Config2 = Configs[Configs[Index].GetParentIndex()].GetConfig()

        # Find the move that was made between the two configurations
        # by comparing the peg numbers and finding the two that aren't
        # the same
        for I in range(0, len(Config1)):
            if Config1[I] != Config2[I]:
                Moves = str(Config2[I]) + " " + str(Config1[I]) \
                        + "\n" + Moves

        Index = Configs[Index].GetParentIndex()

    Moves = Moves.rstrip('\n')

    # Print the answer
    print(NumMoves)
    print(Moves)

if __name__ == "__main__":
    main()
