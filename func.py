import random
import requests

class Generate:

    # This function creates a random array

    def create_random_array(total , end):
        array = []
        for i in range(total):
            random_number = random.randint(1 , end-1)
            if array.count(random_number) == 0:
                array.append(random_number)
            else:
                while array.count(random_number) != 0:
                    random_number = random.randint(1 , end-1)
                array.append(random_number)
        array.sort()
        return array
    


    # This function creates a secret word and stared letters
    def star_latter(word , array):
        stared_letters = []
        for index in array:
            stared_letters.append(word[index])
            word[index] = "*"
            secret_word = "".join(word)
        return secret_word , stared_letters





class Game:

    # given word method
    def word_input():
        letter_array = []
        input_word = input("Enter a word: ")
        for letter in input_word:
            letter_array.append(letter)

        len_word = len(input_word)
        return letter_array , len_word








    # This function estimates the word
    def estimate_word(word , array , stared_letters , secret_word):
        

        is_win = False
        print("secret word is: " , secret_word)
        while is_win == False:
            guess = input("Enter missed letters: ")
            list_guess = []
            for letter in guess:
                list_guess.append(letter)

            if list_guess == stared_letters:
                print("You win")
                is_win = True
            else:
                print("You lose")
               
            


    
class Web_Generate:
    def Random_word_api_func(self):
        url = "https://random-word-api.herokuapp.com/word?number=1"
        response = requests.get(url)
        word = response.json()
        return word[0]


class Generate(Web_Generate):

    # This function creates a random array
    def create_random_array(self, total_len, end):
        array = []
        for i in range(total_len):
            random_number = random.randint(1, end - 1)
            if random_number not in array:
                array.append(random_number)
            else:
                while random_number in array:
                    random_number = random.randint(1, end - 1)
                array.append(random_number)
                break
        array.sort()
        return array

