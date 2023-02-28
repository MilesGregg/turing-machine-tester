




file = open('problem1Tests.txt', 'r')

print(sum(1 for _ in file))

file.seek(0)

print(file.readlines()[0])