
import arcade

volume = 0.1

HURT = arcade.load_sound("resources/hurt.wav")
JUMP = arcade.load_sound("resources/jump.wav")
SHOOT = arcade.load_sound("resources/shoot.wav")
SLIME_JUMP = arcade.load_sound("resources/slime_jump.wav")
SKELETON_HIT = arcade.load_sound("resources/skeleton_hit.wav")

def play(sound):
    sound.play(volume)