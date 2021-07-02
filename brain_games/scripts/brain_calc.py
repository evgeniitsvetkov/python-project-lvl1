#!/usr/bin/env python
import brain_games.games.calc as game
import brain_games.engine as engine


def main():
    engine.play_game(game.task, game.get_question, game.get_answer)


if __name__ == '__main__':
    main()
