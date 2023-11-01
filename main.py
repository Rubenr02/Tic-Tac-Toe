import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 300, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define the board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

# Define the player
current_player = "X"

# Set up the game clock
clock = pygame.time.Clock()

# Function to draw the Tic-Tac-Toe board
def draw_board():
    window.fill(WHITE)
    pygame.draw.line(window, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(window, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(window, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(window, BLACK, (0, 200), (300, 200), 3)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(window, BLUE, (col * 100 + 25, row * 100 + 25), (col * 100 + 75, row * 100 + 75), 3)
                pygame.draw.line(window, BLUE, (col * 100 + 25, row * 100 + 75), (col * 100 + 75, row * 100 + 25), 3)
            elif board[row][col] == "O":
                pygame.draw.circle(window, BLUE, (col * 100 + 50, row * 100 + 50), 40, 3)

# Function to check for a winner
def check_winner(player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_player == "X":
                pos = pygame.mouse.get_pos()
                col = pos[0] // 100
                row = pos[1] // 100
                if board[row][col] == "":
                    board[row][col] = "X"
                    if check_winner("X"):
                        print("Player X wins!")
                        running = False
                    current_player = "O"
            elif current_player == "O":
                pos = pygame.mouse.get_pos()
                col = pos[0] // 100
                row = pos[1] // 100
                if board[row][col] == "":
                    board[row][col] = "O"
                    if check_winner("O"):
                        print("Player O wins!")
                        running = False
                    current_player = "X"

    # Draw the board
    draw_board()

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)  # Adjust the value to control the game speed

# Quit the game
pygame.quit()
