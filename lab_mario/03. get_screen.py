import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')

env.reset()

screen = env.get_screen()

print(screen.shape[0], screen.shape[1])
print(screen)
