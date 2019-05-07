# write a Python program to convert temperatures to and from celsius, fahrenheit.


def cel_to_fahr(temperature):
    fahr = temperature * 1.8 + 32
    return fahr


def fahr_to_cel(temperature):
    cel = (temperature - 32)/1.8
    return cel

print("To program do zamiany temperatury w celcjuszach na fahrenheit i odwrotnie")

question = input("Podaj jednostkę do zmiany C/F: ")

temperature = float(input("Podaj wartość temperatury: "))

if question == "C":
    temp = cel_to_fahr(temperature)
    print(str(temperature) + "C", "to", str(temp) + "F" )
else:
    temp = fahr_to_cel(temperature)
    print(str(temperature) + "F", "to", str(temp) + "C")


