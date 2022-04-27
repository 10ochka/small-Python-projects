import random


class CodeGuessing:
    def __init__(self, complexity: int):
        self.guessed_digit_icons = {
            1: '\u2460', 11: '\u2776',
            2: '\u2461', 12: '\u2777',
            3: '\u2462', 13: '\u2778',
            4: '\u2463', 14: '\u2779',
            5: '\u2464', 15: '\u277A',
            6: '\u2465', 16: '\u277B',
            7: '\u2466', 17: '\u277C',
            8: '\u2467', 18: '\u277D',
            9: '\u2468', 19: '\u277E',
            None: '\u229B'
        }
        self.win_message = 'Win'
        self.lose_message = 'Lose'
        self.code_length = complexity
        self.attempts = complexity
        self.code = ''
        for i in range(self.code_length):
            self.code += str(random.randint(1, 9))

    def run(self):
        print(self.code)
        guessed_numbers = 0
        while self.attempts > 0:
            user_conjecture = input().replace(' ', '')
            answer = ''
            for number in range(self.code_length):
                if user_conjecture[number] == self.code[number]:
                    answer = answer + self.guessed_digit_icons[10 + int(user_conjecture[number])] + ' '
                    guessed_numbers += 1
                elif self.code.find(user_conjecture[number]) > -1:
                    answer = answer + self.guessed_digit_icons[int(user_conjecture[number])] + ' '
                else:
                    answer = answer + self.guessed_digit_icons[None] + ' '

            self.attempts -= 1
            print(answer)

            if guessed_numbers == self.code_length:
                print(self.win_message)
        else:
            print(self.lose_message)


CodeGuessing(int(input())).run()
