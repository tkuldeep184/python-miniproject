import time
import os

def clear_screen():
    os.system("cls")
    
def coin_animation():
    frames = [
        "   _____   \n"
        "  /     \\  \n"
        " | Heads | \n"
        "  \\_____/  ",
        
        "   _____   \n"
        "  /     \\  \n"
        " |       | \n"
        "  \\_____/  ",
        
        "   _____   \n"
        "  /     \\  \n"
        " | Tails | \n"
        "  \\_____/  ",
        
        "   _____   \n"
        "  /     \\  \n"
        " |       | \n"
        "  \\_____/  "
    ]

    for _ in range(3):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.2)
            
            
def dice_animation():
    frames = [
        " _______\n"
        "|       |\n"
        "|   *   |\n"
        "|_______|",
        
        " _______\n"
        "| *     |\n"
        "|       |\n"
        "|_____ *|",
        
        " _______\n"
        "| *   * |\n"
        "|       |\n"
        "| *   * |",
        
        " _______\n"
        "| *   * |\n"
        "|   *   |\n"
        "| *   * |",
        
        " _______\n"
        "| *   * |\n"
        "| *   * |\n"
        "| *   * |",
        
        " _______\n"
        "| * * * |\n"
        "|       |\n"
        "| * * * |"
    ]

    for _ in range(3):
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.2)