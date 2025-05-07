def render(sc, size):
    x = 0
    y = 0

    with open("lvl1.txt", "r") as reader:
        for radek in reader.readlines():
            x = 0

            for char in radek.strip():

                if char == "0":
                    sc.blit("grass", (x, y))
                if char == "1":
                    sc.blit("wall", (x, y))

                x += size
                
            y += size