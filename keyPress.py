import pygame

def init():
    pygame.init()
    win = pygame.display.pygame.display.set_mode(resolution=400, 400)

def getKey(keyname):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()

return ans

def main():
    print(getKey("a"))

    if __name__ == '__main__':
        init()
        while True:
            main()