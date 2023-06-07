n = int(input())

totPoke = 151
pokemons = []
for c in range(n):
    poke = input()
    if poke not in pokemons:
        totPoke -= 1
        pokemons.append(poke)
    else:
        pass

print(f'Falta(m) {totPoke} pomekon(s)')