#!/usr/bin/env python
import brain_games as bg


def main():
    bg.engine.play_game(bg.games.gcd.TASK_DESCRIPTION,
                        bg.games.gcd.get_task)


if __name__ == '__main__':
    main()
