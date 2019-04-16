def main():

    frequency = 0
    frequency_tracker = {'0': "seen"}
    filename = "input/day1_challenge1.txt"
    found_duplicate = False
    while not found_duplicate:
        file = open(filename, "r")
        for line in file:
            frequency += int(line)
            # Seen twice
            if frequency_tracker.get(frequency):
                found_duplicate = True
                break
            else:
                frequency_tracker[frequency] = "seen"

    # Answer
    print frequency

if __name__ == "__main__":
    main()