import pygame 
pygame.init()

# set up
blockSize = 25
BLOCK_WIDTH = 20
SCREEN_SIZE = BLOCK_WIDTH * blockSize + (BLOCK_WIDTH - 1)  
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
screen.fill((0, 0, 0))
pygame.display.set_caption("Snake")
pygame.display.flip()   


# pygame values
down, up, left, right = pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT

# game statics and values
snake_c, bkgrnd_c, line_c = (100, 200, 80), (12, 12, 12), (72, 72, 72)
dir, x, y = 0, 0, 0



def updateDir(type):
    if not (type == down or type == up or type == left or type == right):
        return

    global dir
    dir = type
    print(dir)

def drawBlock(x, y, color):
    pygame.draw.rect(screen, color, (x, y, blockSize, blockSize))

def drawLines():

    x = 1
    while x <= BLOCK_WIDTH:
        pygame.draw.line(screen, line_c, (x*blockSize + x - 1, 0), (x*blockSize + x - 1, SCREEN_SIZE), 1)
        x += 1

    y = 1
    while y <= BLOCK_WIDTH:
        pygame.draw.line(screen, line_c, (0, y*blockSize + y - 1), (SCREEN_SIZE, y*blockSize + y - 1), 1)
        y += 1
            
            
def move():
    global dir
    global x
    global y

    if dir == down:
        if SCREEN_SIZE - y >= blockSize:
            y += blockSize + 1
    elif dir == up:
        y -= blockSize + 1
    elif dir == left:
        x -= blockSize + 1
    elif dir == right:
        x += blockSize + 1

    drawBlock(x, y, snake_c)


def __main__():
    running = True

    while running:
        pygame.time.delay(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN:
                updateDir(event.key)

        screen.fill(bkgrnd_c)
        drawLines()
        move()
        pygame.display.update()


if __name__ == "__main__":
    __main__()






