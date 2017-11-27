# Bomberman-Terminal-Game

## How to run the game

* To run the game, enter the following command:

        sudo ./game.sh

*	If the game view is not proper(not fiting in your terminal), change the terminal font size to 10

*   If the above command results in an error saying `command not found`, enter the following command first:

    `chmod +x game.sh`

*   Sudo permissions are required for setting all the cpu governors to `performance` temporarily.
    After the game is over the original values will be reset.

*   If you don not wish to give sudo permission you may run this command:

    `python3 bomberman.py` or `python bomberman.py` 

## Controls:

|    Moves   | Keyboard input |
|:----------:|:--------------:|
| Move left  |        a       |
| Move right |        d       |
| Move up    |        w       |
| Move down  |        s       |
| Drop bomb  |   b or space   |
| Quit       |        q       |
