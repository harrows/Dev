import pygame

from random import randint

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()

class GameObject:
    def __init__(self, position=(0, 0), body_color=(255, 255, 255)):
        self.position = position
        self.body_color = body_color

    def draw(self, screen):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    def __init__(self, position=(0, 0), body_color=(0, 255, 0), length=1):
        # Изначально змейка состоит из 1 сегмента
        super().__init__(position, body_color)
        self.length = length
        self.positions = [position]
        self.direction = RIGHT
        self.next_direction = RIGHT

    def move(self):
        if self.next_direction:
            self.direction = self.next_direction
            
        
        # Новая голова змейки
        new_head = (self.positions[0][0] + self.direction[0] * GRID_SIZE, self.positions[0][1] + self.direction[1] * GRID_SIZE)
        
        # Проверка выхода за границы и перемещение на противоположную сторону
        new_head = (new_head[0] % SCREEN_WIDTH, new_head[1] % SCREEN_HEIGHT)
        
        self.positions.insert(0, new_head)

        # Если змейка съела яблоко, она растёт
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, screen):
        for position in self.positions[:self.length]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    def get_head_position(self):
        return self.positions[0]

    def reset(self):
        self.length = 1  # Змейка снова состоит из 1 сегмента
        self.positions = [(GRID_SIZE * 2, 0)]  # Только один сегмент
        self.direction = RIGHT
        self.next_direction = None
    
    def update_direction(self, new_direction):
        # Обновляем направление змейки, если оно не противоположное текущему
        if (new_direction == UP and self.direction != DOWN) or \
           (new_direction == DOWN and self.direction != UP) or \
           (new_direction == LEFT and self.direction != RIGHT) or \
           (new_direction == RIGHT and self.direction != LEFT):
            self.direction = new_direction


class Apple(GameObject):
    def __init__(self):
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        # Генерация случайной позиции яблока
        self.position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE, randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, screen):
        super().draw(screen)


def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT


def main():
    snake = Snake()
    food = Apple()

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()

        # Проверка на столкновение с самим собой
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        # Проверка, съела ли змейка яблоко
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    main()
