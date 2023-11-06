import numpy as np
import cv2
import random

N_SQUARES = 100  # Number of squares in the population
MUTATION_RATE = 0.2  # Mutation rate
IMG_FILE = "pic.jpg"  # Input image file

# Load the input image
input_image = cv2.imread(IMG_FILE)

# Get the dimensions of the input image
IMG_HEIGHT, IMG_WIDTH, _ = input_image.shape

# Create a blank canvas
canvas = np.zeros((IMG_HEIGHT, IMG_WIDTH, 3), dtype=np.uint8)

# Define a square class to represent squares
class Square:
    def _init_(self):
        self.x = random.randint(0, IMG_WIDTH)
        self.y = random.randint(0, IMG_HEIGHT)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.opacity = random.uniform(0, 1)

    def mutate(self):
        if random.random() < MUTATION_RATE:
            # Mutate the square (e.g., change position, color, or opacity)
            self.x = random.randint(0, IMG_WIDTH)
            self.y = random.randint(0, IMG_HEIGHT)
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.opacity = random.uniform(0, 1)

    def draw(self, img):
        # Draw the square on the canvas
        overlay = img.copy()
        cv2.rectangle(overlay, (self.x, self.y), (self.x + 10, self.y + 10), self.color, -1)
        cv2.addWeighted(overlay, self.opacity, img, 1 - self.opacity, 0, img)

# Create an initial population of squares
population = [Square() for _ in range(N_SQUARES)]

# Main GA loop
for generation in range(100):  # Replace with your desired number of generations
    for square in population:
        square.mutate()
        square.draw(canvas)

    # Display the canvas (you can save it to an image file)
    cv2.imshow('Image Generation', canvas)
    cv2.waitKey(10)  # Adjust the delay as needed

cv2.destroyAllWindows()