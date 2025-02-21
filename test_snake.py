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

# Цвета:
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, position=(0, 0), body_color=SNAKE_COLOR):
        """Инициализация объекта."""
        self.position = position
        self.body_color = body_color

    def draw(self, screen):
        """Отображение объекта на экране."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс змейки, управляемой игроком."""

    def __init__(self):
        """Инициализация змейки."""
        self.length = 1
        self.positions = [(GRID_SIZE * 2, 0)]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.position = None

    def move(self):
        """Перемещение змейки по игровому полю."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

        new_head = (
            self.positions[0][0] + self.direction[0] * GRID_SIZE,
            self.positions[0][1] + self.direction[1] * GRID_SIZE
        )
        new_head = (new_head[0] % SCREEN_WIDTH, new_head[1] % SCREEN_HEIGHT)
        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, screen):
        """Отображение змейки на экране."""
        for position in self.positions[:self.length]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

    def get_head_position(self):
        """Возвращает текущую позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [(GRID_SIZE * 2, 0)]
        self.direction = RIGHT
        self.next_direction = None

    def update_direction(self, new_direction):
        """Обновляет направление движения змейки."""
        self.next_direction = new_direction


class Apple(GameObject):
    """Класс яблока, которое ест змейка."""

    def __init__(self):
        """Инициализация яблока."""
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self):
        """Генерирует случайную позицию для яблока."""
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )

    def draw(self, screen):
        """Отображение яблока на экране."""
        super().draw(screen)


def handle_keys(snake):
    """Обработка нажатий клавиш для управления змейкой."""
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
    """Главная функция игры."""
    snake = Snake()
    food = Apple()

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()

        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
