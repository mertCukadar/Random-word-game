from deneme import Deneme




if __name__ == "__main__":
    word , len_word = Deneme.word_input()
    array = Deneme.create_random_array(3 , len_word)
    secret_word , stared_letters = Deneme.star_latter(word , array)


    Deneme.estimate_word(word , array , stared_letters ,secret_word)