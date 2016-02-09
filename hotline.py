drake = open('HOT.ppm', 'w')
drake.write('P3 500 500 255 \n')
for x in range(500):
    for y in range(500):
        hot = (50 + x + y) % 256 #red
        line = (10 - x + (2 * y)) % 256 #green
        bling = 255 #blue
        onething = "%d %d %d " % (hot, line, bling)
        drake.write(onething)
    drake.write("\n")
drake.close()
