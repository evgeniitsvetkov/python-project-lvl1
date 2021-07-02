#!/usr/bin/env python
import brain_games.engine as engine
import brain_games.games.progression as game


def main():
    engine.play_game(game.task_description, game.get_task)


if __name__ == '__main__':
    main()
