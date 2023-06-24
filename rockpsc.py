import random

print('Sveiki, ar nori pradeti zaidima vaski ci?(y/n)')
a = input()

while a == 'y':
    c = ['zirkles', 'popierius', 'sulinys']
    choices = random.choice(c)
    print("Pasrinkite viena is variantu (zirkles,popierius,sulinys): \n")
    b = input()
    print('Kompiuteris renkasi!!\n')

    if choices == b:
        print('Lygiosios')
    elif choices == 'zirkles':
        if b == 'sulinys':
            print('Tu laimejai!! Kompiuterio pasirinkimas buvo, ', choices, ' ,tavo pasirinkimas buvo ', b)
        else:
            print('Tu pralaimejai... :(. Kompiuterio pasirinkimas buvo, ', choices, ' ,tavo pasirinkimas buvo ', b)
    elif choices == 'popierius':
        if b == 'zirkles':
            print('Tu laimejai!! Kompiuterio pasirinkimas buvo, ',choices,' ,tavo pasirinkimas buvo ',b )
        else:
            print('Tu pralaimejai... :(. Kompiuterio pasirinkimas buvo, ',choices,' ,tavo pasirinkimas buvo ',b )
    elif choices == 'sulinys':
        if b == 'lapas':
            print('Tu laimejai!! Kompiuterio pasirinkimas buvo, ',choices,' ,tavo pasirinkimas buvo ',b )
        else:
            print('Tu pralaimejai... :(. Kompiuterio pasirinkimas buvo, ',choices,' ,tavo pasirinkimas buvo ',b )

    print('Sveikiname suzaidus zaidima, ar noretumete dar karta pameginti?\n')
    play_again = input('(y/n): ')
    if play_again != 'y':
        break
print('Viso geriausio!\n')
print('testinis variantas')