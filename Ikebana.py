import random


class Ikebana:
    """Цветы ставить игра стратегия красиво разный радуга банка"""

    def __init__(self):
        self.__player_turn_flower_type = None
        self.__player_turn_flower_number = None
        self.__vase_flower_limit = 3
        self.__flower_types = {
            "красный": 0,
            "зелёный": 0,
            "голубой": 0,
            "фиолетовый": 0,
            "желтый": 0
        }
        self.__start_message = 'Обыграй рандомайзер!'
        self.__player_win_message = 'ты победил'
        self.__player_lose_message = 'ты проиграл'
        self.__asking_for_number = 'сколько штук?'
        self.__asking_for_type = 'какой цвет?'
        self.__wrong_flower_type = 'wrong flower type'
        self.__bot_making_move = 'оппонент делает ход'
        self.__number_is_out_of_vase_limit = 'number out of vase limit'
        self.__message_being_sent = f'красный = {self.__flower_types["красный"]}\n' \
                                    f'зелёный = {self.__flower_types["зелёный"]}\n' \
                                    f'голубой = {self.__flower_types["голубой"]}\n' \
                                    f'фиолетовый = {self.__flower_types["фиолетовый"]}\n' \
                                    f'желтый = {self.__flower_types["желтый"]}'

    def run(self):
        print(self.__start_message)

        while self.__flower_types["красный"] + self.__flower_types["зелёный"] + \
                self.__flower_types["голубой"] + self.__flower_types["фиолетовый"] + \
                self.__flower_types["желтый"] != 15:
            print(self.__message_being_sent)
            print(self.__asking_for_type)

            while self.__player_turn_flower_type is None:
                self.__player_turn_flower_type = input().replace(' ', '').lower()
                if not (self.__player_turn_flower_type in self.__flower_types.keys()):
                    self.__player_turn_flower_type = None
                    print(self.__wrong_flower_type)

            print(self.__asking_for_number)
            while self.__player_turn_flower_number is None:
                self.__player_turn_flower_number = int(input())
                if self.__vase_flower_limit - self.__flower_types[self.__player_turn_flower_type] < \
                        self.__player_turn_flower_number:
                    print(self.__number_is_out_of_vase_limit)
                    self.__player_turn_flower_number = None

            self.__flower_types[self.__player_turn_flower_type] += self.__player_turn_flower_number

            self.__message_being_sent = f'красный = {self.__flower_types["красный"]}\n' \
                                        f'зелёный = {self.__flower_types["зелёный"]}\n' \
                                        f'голубой = {self.__flower_types["голубой"]}\n' \
                                        f'фиолетовый = {self.__flower_types["фиолетовый"]}\n' \
                                        f'желтый = {self.__flower_types["желтый"]}'
            self.__player_turn_flower_type = None
            self.__player_turn_flower_number = None

            if self.__flower_types["красный"] + self.__flower_types["зелёный"] + \
                    self.__flower_types["голубой"] + self.__flower_types["фиолетовый"] + \
                    self.__flower_types["желтый"] == 15:
                print(self.__player_lose_message)
                return False

            print(self.__bot_making_move)
            self.bot_move()
            self.__message_being_sent = f'красный = {self.__flower_types["красный"]}\n' \
                                        f'зелёный = {self.__flower_types["зелёный"]}\n' \
                                        f'голубой = {self.__flower_types["голубой"]}\n' \
                                        f'фиолетовый = {self.__flower_types["фиолетовый"]}\n' \
                                        f'желтый = {self.__flower_types["желтый"]}'

        else:
            print(self.__player_win_message)
            return False

    def bot_move(self):
        __vases = self.__flower_types.keys()
        __free_vases = []
        for __vase in __vases:
            if self.__flower_types[__vase] != 3:
                __free_vases.append(__vase)
        __random_vase = random.choice(__free_vases)
        self.__flower_types[__random_vase] += random.randint(1, 3 - self.__flower_types[__random_vase])


Ikebana().run()
