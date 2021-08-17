def main():
    #escribe tu código abajo de esta línea
    area1 = float(input("Area a pintar en metros: "))
    rendimiento = float(input("Rendimiento (m2/l): "))
    litros = area1/rendimiento
    litros = int(round(litros,0))
    print("Litros a comprar:",litros)

if __name__ == '__main__':
    main()
