import arcade

from src import MainWindow

def main():
    window = MainWindow.PyGameJam2020()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()