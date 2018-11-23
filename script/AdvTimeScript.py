lines = [x.strip() for x in open("data/AdventureTime_S1.csv").readlines()]

even = True
row = ""
episodes = []
for line in lines:
    x = line.split("\t")

    if even:
        overall, title = x[0], x[2]
        row = "- [ ] " + overall + ", " + title
        print(row)

    even = not even


# end
