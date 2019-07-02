with open("C:\\AsoPython\\Orif\\homeExercise\\read_file.txt") as source:
    lines = source.readlines()
    for line in lines:
        print(line.rstrip())