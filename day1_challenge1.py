def main():

    frequency = 0
    filename = "input/day1_challenge1.txt"
    file = open(filename, "r")
    for line in file:
        frequency += int(line)

    # Answer
    print frequency

if __name__ == "__main__":
    main()