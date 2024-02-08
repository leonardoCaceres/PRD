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
fileNumber = 0
while ".py" in listOfFiles[fileNumber] or "saidaDeDados" in listOfFiles[fileNumber]:
    fileNumber += 1
f = open(pathString + listOfFiles[fileNumber], "r")

lines = []
for line in f.readlines():
    lineData = []
    dataInString = line.replace("\n", "").split(sep=" ")
    for data in dataInString:
        lineData.append(int(data))
    lines.append(lineData)
lines = np.array(lines)

min_value = np.argmin(lines[:, 1])

for value in lines:
    value[1] = -1 * (value[1]) * (4.71e-3) + 39558


def getImportantPoints():
    data = lines[min_value - pointsBefore : min_value + pointsAfter].copy()
    for value in data:
        value[0] = value[0] - lines[min_value - 1 - pointsBefore, 0] - 12
    return data


##################################################################################
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
        data = getImportantPoints()
        plt.legend(["Teste 1"])
        plt.title("Tyto II - 27/01")
        plt.xlabel("Tempo(ms)")
        plt.ylabel("Força (N)")
        plt.plot(
            data[:, 0],
            data[:, 1],
            "o",
        )
        plt.show()
    else:
        if os.path.exists("saidaDeDados.txt"):
            os.remove("saidaDeDados.txt")
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
