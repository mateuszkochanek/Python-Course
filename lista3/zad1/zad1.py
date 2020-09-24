def transpozition(matrix):
    return [' '.join([(matrix[j]).split(" ")[i] for j in range(len(matrix[i].split(" ")))]) for i in range(len((matrix[0]).split(" ")))]


matrix = ["1.1 2.2 3.3 4.4", "5.5 6.6 7.7 8.8", "9.9 10.10 11.11 12.12", "13.13 14.14 15.15 16.16"]
print(transpozition(matrix))