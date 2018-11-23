lines = [x.strip() for x in open("data/AdventureTime_S1.csv").readlines()]

even = True
row = ""
episodes = []
for line in lines:
    x = line.split("\t")

    if even:
        overall, season, title = x[0], x[1], x[2]
        row = "- [ ] " + overall + ", " + season + ", " + title
        print(row)

    even = not even


# end
