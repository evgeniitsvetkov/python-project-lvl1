#!/usr/bin/env python
import brain_games as bg


def main():
    bg.engine.play_game(bg.games.even.TASK_DESCRIPTION,
                        bg.games.even.get_task)


if __name__ == '__main__':
    main()
