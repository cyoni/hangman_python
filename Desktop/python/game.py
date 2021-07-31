from shapes import shapes

class game:

    MAX_TRIES = 6
    TRIES_USED = 0

    def __init__(self):
        pass

    def start_guessing(self):
        old_letters_guessed = []
        while self.MAX_TRIES > 0:
            letter_guessed = input("Guess a letter: ")
            is_good_input = self.try_update_letter_guessed(letter_guessed, old_letters_guessed)
            if is_good_input:
                self.show_hidden_word(self.secret_word, old_letters_guessed)
                is_win = self.check_win(self.secret_word, old_letters_guessed)
                if is_win:
                    print("YOU WIN")
                    return
            else:
                self.TRIES_USED = self.TRIES_USED + 1
                print(' -> '.join(old_letters_guessed))
                print(shapes.dictonaty[self.TRIES_USED])
                self.show_hidden_word(self.secret_word, old_letters_guessed)
                self.MAX_TRIES = self.MAX_TRIES - 1
        print(shapes.dictonaty['lose'])
        print("YOU LOSE")
        print("THE WORD WAS:", self.secret_word)

    def is_letter_valid(self, letter):
        is_valid = True
        if not len(letter) == 1:
            is_valid = False

        return is_valid

    def try_update_letter_guessed(self, letter_guessed, old_letters_guessed):
        if not self.is_letter_valid(letter_guessed) or letter_guessed in old_letters_guessed:
            print("X")
            return False

        old_letters_guessed.append(letter_guessed)

        if letter_guessed not in self.secret_word:
            print("X")
            return False

        return True

    def show_hidden_word(self, secret_word, old_letters_guessed):
        answer = ['_'] * len(secret_word)
        for i in range(0, len(secret_word)):
            if secret_word[i] in old_letters_guessed:
                answer[i] = secret_word[i]
        print(" ".join(answer))
        return answer    

    def check_win(self, secret_word, old_letters_guessed):
        for i in secret_word:
            if i not in old_letters_guessed:
                return False
        return True

    def load_secret_word(self):
        f = open("secret_word.txt", "r")
        self.secret_word = f.read()

    def start_game(self):
        print("Hello!")
        self.load_secret_word()
        secret_word_length = len(self.secret_word)
        print('_ ' * secret_word_length)
        self.start_guessing()
