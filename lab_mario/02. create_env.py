import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level 1-1')
env.reset()


print(env)
