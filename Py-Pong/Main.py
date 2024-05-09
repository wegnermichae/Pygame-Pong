import pygame
import sys
import random

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong Paddles")

    # Set up the game loop
    clock = pygame.time.Clock()
    running = True


    # Ball initial Vars
    ball_color = (255,255,255)
    ball_size = 10
    ball_pos_x = screen_width/2
    ball_pos_y = screen_height/2
    ball_pos = (ball_pos_x, ball_pos_y)

    # ball movement speeds
    ball_move_var_y = 4
    ball_move_var_x = 5

    # left paddle movement speed
    left_paddle_move = 5

    # initialize scores
    left_score = 0
    right_score = 0

    # Paddle dimensions
    paddle_width = 10
    paddle_height = 100

    # Paddle color
    paddle_color = (0, 255, 0)

    # Initial paddle positions
    left_paddle_x = 25
    left_paddle_y = screen_height // 2 - paddle_height // 2
    right_paddle_x = screen_width - 25 - paddle_width
    right_paddle_y = screen_height // 2 - paddle_height // 2

    # Main game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Update right paddle position based on mouse y-coordinate
        right_paddle_y = mouse_y - paddle_height // 2

        # Clamp paddle position to screen boundaries
        right_paddle_y = max(0, min(right_paddle_y, screen_height - paddle_height))

        # Clear the screen
        screen.fill((0, 0, 0))  # Fill screen with black color

        # add score to screen
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"{left_score} - {right_score}", True, (255, 255, 255))
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

        # ball movement
        ball_pos_x = random.uniform(ball_pos_x, ball_pos_x + ball_move_var_x)
        ball_pos_y = random.uniform(ball_pos_y, ball_pos_y + ball_move_var_y)
        ball_pos = (ball_pos_x, ball_pos_y)

        # left paddle movement
        left_paddle_y = random.uniform(left_paddle_y, (left_paddle_y + left_paddle_move))

        # Detect left paddle collision with bottom of screen
        if (float(left_paddle_y + paddle_height)) >= (float(screen_height) - 10):
            left_paddle_move = -left_paddle_move

        # Detect left paddle collision with top of screen
        if (float(left_paddle_y)) <= float(10):
            left_paddle_move = -left_paddle_move

        # Detect ball collision with bottom of screen
        if (float(ball_pos_y) + ball_size) >= (float(screen_height) - 5):
            ball_move_var_y = -ball_move_var_y
            ball_pos_y = random.uniform(ball_pos_y, ball_pos_y + ball_move_var_y)

        # Detect ball collision with top of screen
        if (float(ball_pos_y) - ball_size) <= float(5):
            ball_move_var_y = -ball_move_var_y
            ball_pos_y = random.uniform(ball_pos_y, ball_pos_y + ball_move_var_y)

        # Detect ball collision with right paddle
        # add fix for being behind paddle (do this for both paddle detection methods)
        if (float(ball_pos_x) + ball_size) >= float(right_paddle_x) and (float(ball_pos_y) - ball_size) >= float(right_paddle_y) and (float(ball_pos_y) + ball_size) <= float(right_paddle_y + paddle_height):
            ball_move_var_x = -ball_move_var_x
            ball_pos_x = random.uniform(ball_pos_x, ball_pos_x + ball_move_var_x)
            ball_pos_y = random.uniform(ball_pos_y, ball_pos_y + ball_move_var_y)

        # Detect ball collision with left paddle
        if (float(ball_pos_x) - ball_size) <= float(left_paddle_x + paddle_width) and (float(ball_pos_y) - ball_size) >= float(left_paddle_y) and (float(ball_pos_y) + ball_size) <= float(left_paddle_y + paddle_height):
            ball_move_var_x = -ball_move_var_x
            ball_pos_x = random.uniform(ball_pos_x, ball_pos_x + ball_move_var_x)
            ball_pos_y = random.uniform(ball_pos_y, ball_pos_y + ball_move_var_y)

        # Detect ball collision with right right of screen and reset to center
        if (float(ball_pos_x + ball_size)) >= float(screen_width):
            ball_pos_x = screen_width/2
            ball_move_var_x = -ball_move_var_x
            left_score = left_score + 1

        # Detect ball collision with left of screen and reset to center
        if (float(ball_pos_x) - ball_size) <= float(0):
            ball_pos_x = screen_width/2
            ball_move_var_x = -ball_move_var_x
            right_score = right_score + 1

        # Draw ball
        pygame.draw.circle(screen, ball_color, ball_pos, ball_size)

        # Draw paddles
        pygame.draw.rect(screen, paddle_color, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(screen, paddle_color, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
