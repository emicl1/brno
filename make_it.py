def make_it():
    with open("input", "r") as input:
        a = {}
        for i in range(74419):
            a[i] = []
        content = input.read()
        content_list = content.splitlines()
        input.close()

        for i in range(74420, len(content_list)):
            c = content_list[i].split()
            b = []
            for i in c:
                b.append(int(i))
            a[b[0]].append((b[1], b[2]))
            a[b[1]].append((b[0], b[2]))
        for i in a.values():
            sorted(i, key=lambda tup: tup[1], reverse=True)
    return a

b = make_it()





