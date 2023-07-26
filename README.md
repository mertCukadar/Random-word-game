# Word Guessing Game

<!-- ![Word Guessing Game](https://example.com/word-guessing-game.png) -->

This is a fun and interactive word guessing game written in Python. The game randomly selects a word using an external API and hides some of the letters. Your mission is to guess the hidden letters and complete the word.

## Installation

1. Clone the repository to your local machine.

```bash
git clone <repository_url>
```

```bash
cd word-guessing-game
```

```bash
pip install -r requirements.txt

```

## How to Play

To start playing the game, run the __main.py__ script:


```bash
python main.py
```

The program will fetch a random word from an external API and hide some of the letters, presenting you with a challenge to guess the missing ones.

    The game will prompt you to enter your guess for the missing letters.
    Keep guessing until you correctly identify all the missing letters.
    If you guess all the letters correctly, you win the game!

Features

    Randomly generates a word using an external API.
    Hides some of the letters in the word to create a challenge.
    User-friendly interface and prompts for guessing the missing letters.
    Provides feedback on whether your guesses are correct.

Requirements

The game requires the following packages to be installed:

    requests
    random

You can install these packages using the following command:


API

The game uses the Random Word API to fetch a random word for the guessing game.
Contributions

Contributions to this project are welcome. If you find any issues or have ideas for improvements, feel free to open an issue or create a pull request.
License

This project is licensed under the MIT License.

