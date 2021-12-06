from make_it import make_it

dict_of_roads = make_it()
print(dict_of_roads)


def check_if_visited(array, visited):
    """
    Tato funkce ověří, jestli nejde už o navštívenou node
    :param array: ten array co je v dictu
    :param visited: průběžný visited,co jsou
    :return: True/ False array, kde True znamená, že to nejde použít
    """
    b = []
    for i in array:
        if i[0] in visited:
            b.append(True)
        else:
            b.append(False)
    return b


def check_length_from_node(array, dict_of_roads, visited):
    """
    Tato funkce ověří, že příští bod, splňuje podmínku 2 km
    :param array: ten array co je v dictu
    :param dict_of_roads: to původní co je udělaný díky funkci make_it
    :param visited: průběžný visited
    :return: vratí to list True/False, Kde True zanemná, že to nejde použít
    """
    b = []
    for i in array:
        c = dict_of_roads[i[0]]
        r = []
        for j in c:
            if j[1] <= 2:
                if j[0] in visited:
                    r.append(True)
                else:
                    r.append(False)
            else:
                r.append(False)
        b.append(any(r))
    return b


def main(dict_of_roads, where_wanna_start):
    visited = []
    sum = 0
    value_where_are_we_now = where_wanna_start
    been_check_the_length_and_visited = check_length_from_node(dict_of_roads[value_where_are_we_now], dict_of_roads,
                                                               visited)
    while not all(been_check_the_length_and_visited):
        visited.append(value_where_are_we_now)
        for i in range(len(been_check_the_length_and_visited)):
            if been_check_the_length_and_visited[i] is False:
                if dict_of_roads[value_where_are_we_now][i][0] in visited:
                    been_check_the_length_and_visited[i] = True
                    continue
                else:
                    sum += dict_of_roads[value_where_are_we_now][i][1]
                    value_where_are_we_now = dict_of_roads[value_where_are_we_now][i][0]
                    been_check_the_length_and_visited = check_length_from_node(dict_of_roads[value_where_are_we_now],
                                                                               dict_of_roads, visited)
                    break
    return sum


a = main(dict_of_roads, 2)


where_we_are = 0
sum = 0
for i in range(74418):
    b = main(dict_of_roads, i)
    if b > sum:
        sum = b
        where_we_are = i
print(sum)







