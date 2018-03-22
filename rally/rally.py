# NOTE: Help was obtained through Wikipedia and Stack Overflow as sources of consultation
# Other documentation for proofs and ideas are found in Documentation.pdf

import sys

# PARAMETERS:
#   graph: dictionary with key being a string and value being a dictionary of 
#       strings and weights. Of the form { string: {string : int, ..} ..}
#   start: start string
#   end: end string (target)
# DESCRIPTION:
#   This performs Dijkstra's shortest path algorithm on a weighted directed graph.
def dijkstra_shortest_path(graph, start, end):
    
    # words not in dictionary check
    if start not in graph:
        return -1

    if end not in graph:
        return -1

    # if start and end are the same check
    if start == end:
        return -1

    # variables for algorithm
    undiscovered = {start}
    visited = set()
    distances = {start: 0}
    parents = {}

    # going through undiscovered part of graph
    while undiscovered:
        current = min([(distances[node], node) for node in undiscovered])[1]

        if current == end:
            break

        undiscovered.discard(current)
        visited.add(current)

        edges = graph[current]
        unvisited_neighbours = set(edges).difference(visited)

        for neighbour in unvisited_neighbours:
            neighbour_distance = distances[current] + edges[neighbour]

            if neighbour_distance < distances.get(neighbour, float('inf')):
                distances[neighbour] = neighbour_distance
                parents[neighbour] = current
                undiscovered.add(neighbour)
    
    # return shortest distance, or -1 if no path exists
    if end in distances.keys():
        return distances[end]
    else:
        return -1
    

# PARAMETERS:
#   filename: name of text file used to read inputs
# DESCRIPTION:
#   This parses inputs and organizes accordingly. Returns -1 if invalid.
def read_file(filename):
    try:
        file = open(filename, 'r')
        try:
            weights = [int(i) for i in file.readline().split()]
            # invalid number of weights check
            if len(weights) != 4:
                return -1

            # negative number check
            for i in weights:
                if i < 0:
                    return -1
            add_weight = weights[0]
            del_weight = weights[1]
            change_weight = weights[2]
            anagram_weight = weights[3]

        except:
            # print "Invalid first line. Please enter 4 integers separated by a space."
            return -1

        # invalid number of words per line check, makes every input uppercase
        start = [i for i in file.readline().strip('\n').upper().split()]
        if len(start) != 1:
            return -1
        else:
            start = start[0]

        end = [i for i in file.readline().strip('\n').upper().split()]
        if len(end) != 1:
            return -1
        else:
            end = end[0]

        word_list = {
            'HEALTH': {'HEATH': del_weight},
            'HEATS': {'HENTS': change_weight, 'HEAT': del_weight},
            'HEAT': {'HEATS': add_weight, 'HENT': change_weight},
            'HEATH': {'HEATS': change_weight, "HEALTH": add_weight},
            'HENTS': {'HENDS': change_weight, 'HENT': del_weight},
            'HENT': {'HENTS': add_weight, 'HEAT': change_weight},
            'HENDS': {'HANDS': change_weight, 'HEND': del_weight},
            'HEND': {'HENDS': add_weight, 'HAND': change_weight},
            'HAND': {'HANDS': add_weight, 'HEND': change_weight},
            'HANDS': {'HAND': del_weight, 'HENDS': change_weight},
            'TEAM': {'MATE': anagram_weight},
            'MATE': {'TEAM': anagram_weight},
            'OPHTHALMOLOGY': {},
            'GLASSES': {'CLASSES': change_weight},
            'CLASSES': {'GLASSES': change_weight}
        }
            
        return dijkstra_shortest_path(word_list, start, end)

    # catch exception if file does exist or is a bad file
    except IOError:
        return -1
        sys.exit()


# MAIN CODE RUNNING TESTS
if __name__ == "__main__":
    # operation check tests
    assert read_file('string_tests/test1.txt') == 7 # normal working test with insert/delete/change
    assert read_file('string_tests/test2.txt') == 3 # anagram, case does not matter
    assert read_file('string_tests/test3.txt') == -1 # no path

    # invalid input in textfile tests
    assert read_file("this file does not exist") == -1 # bad file 
    assert read_file('input_tests/test4.txt') == -1 # start not in the word list
    assert read_file('input_tests/test5.txt') == -1 # end not in the word list
    assert read_file('input_tests/test6.txt') == -1 # start and end are the same
    assert read_file('input_tests/test7.txt') == -1 # non-integer(s) in first line
    assert read_file('input_tests/test8.txt') == -1 # too many values
    assert read_file('input_tests/test9.txt') == -1 # second line is not one word
    assert read_file('input_tests/test10.txt') == -1 # third line is not one word
    assert read_file('input_tests/test11.txt') == -1 # first line has negative number(s) 

    # all tests have been completed
    print "All the tests have been passed."