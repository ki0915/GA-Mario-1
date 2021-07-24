import retro
import numpy as np

env = retro.make(game='SuperMarioBros-Nes', state='Level 1-1')
env.reset()


env.step(np.array([1, 0, 0, 0, 0, 0, 1, 0]))
