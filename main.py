from func import Game , Generate



if __name__ == "__main__":
    game = Game()
    generate = Generate()

   
    word = generate.Random_word_api_func()
    latter_array, len_word = game.word_input(word)
    random_array = generate.create_random_array(len_word, len_word - 1) 
    
    
    
    secret_word, stared_letters = generate.star_latter(word, random_array)
    game.estimate_word(stared_letters, secret_word)