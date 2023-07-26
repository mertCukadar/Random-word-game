from func import Game , Generate




if __name__ == "__main__":
    word , len_word = Game.word_input()
    array = Generate.create_random_array(3 , len_word)
    secret_word , stared_letters = Generate.star_latter(word , array)


    Game.estimate_word(word , array , stared_letters ,secret_word)

    