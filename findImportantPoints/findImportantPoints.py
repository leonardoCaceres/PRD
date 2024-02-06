import numpy as np
import os
import pathlib
import matplotlib.pyplot as plt

actualPath = str(pathlib.Path(__file__).parent.resolve())

pathList = actualPath.split("\\")
pathString = ""

for path in pathList:
    pathString += path + "\\"

listOfFiles = os.listdir(actualPath)
f = open(pathString + listOfFiles[0], "r")

lines = []
for line in f.readlines():
    lineData = []
    dataInString = line.replace("\n", "").split(sep=" ")
    for data in dataInString:
        lineData.append(int(data))
    lines.append(lineData)
lines = np.array(lines)

min_value = np.argmin(lines[:, 1])

clear = lambda: os.system("cls")
command = -1
pointsBefore = 25
pointsAfter = 35
while command != "0":
    print("digite o comando:")
    print("1 - Definir a quantidade de pontos antes do apice")
    print("2 - Definir a quantidade de pontos depois do apice")
    print(
        "3 - Pré-visualizar, ponto a serem vistos antes do apice: "
        + str(pointsBefore)
        + " e ponto a serem vistos depois do apice: "
        + str(pointsAfter)
    )
    print("0 - encerrar e gerar arquivo com os pontos")
    command = input()
    if command == "1":
        print("Defina a quantidade de pontos a serem visualizados antes do apice!")
        pointsBefore = int(input())
    elif command == "2":
        print("Defina a quantidade de pontos a serem visualizados depois do apice!")
        pointsAfter = int(input())
    elif command == "3":
        plt.plot(
            lines[min_value - pointsBefore : min_value + pointsAfter, 0],
            lines[min_value - pointsBefore : min_value + pointsAfter, 1],
        )
        plt.show()
    else:
        g = open("saidaDeDados.txt", "a")
        for i in range(min_value - pointsBefore, min_value + pointsAfter, 1):
            for data in lines[i]:
                g.write(str(data) + " ")
            g.write("\n")
        g.close
    clear()
print("Fim do programa aperte enter para continuar!")
print("Avante PRD")
input()
