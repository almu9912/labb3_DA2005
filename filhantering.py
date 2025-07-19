def number_lines(f):
    """Öppna och läs original filen."""
    with open (f, 'r') as infile:
        lines = infile.readlines()
    #infile.close()

    with open('numbered_' + f, 'w') as outfile:
        for i in range(len(lines)):
            outfile.write(f"{i} {lines[i]}")
    #outfile.close()
    #print(outfile)

number_lines('poem.txt')
