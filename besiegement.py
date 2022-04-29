import random
import re


class HRWeapon:
    """ high-range weapon """

    def __init__(self):
        self.attack_range = 70
        self.ammo = 380


class LRWeapon:
    """ low-range weapon """

    def __init__(self):
        self.attack_range = 15
        self.ammo = 180


class Wind:
    """ wind """

    def __init__(self):
        self.speed = 0
        self.speed_values = [
            random.randint(10, 20),
            random.randint(40, 60),
            random.randint(90, 100),
        ]
        self.direction = None
        self.direction_values = {
            'N': [0, -10], 'S': [0, 10],
            'W': [-10, 0], 'E': [10, 0],
            'N-W': [-10, -10], 'N-E': [-10, 10],
            'S-W': [10, -10], 'S-E': [10, 10]
        }


class Enemies:
    """ enemies """

    def __init__(self):
        self.value = 0
        self.speed = 0
        self.speed_values = [
            random.randint(15, 25),
            random.randint(50, 70),
            random.randint(110, 130),
            random.randint(170, 180)
        ]
        self.coordinates = []
        self.direction = None
        self.direction_values = {
            'N': [0, -10],
            'W': [-10, 0],
            'N-W': [-10, -10]
        }


class Base:
    """ base """

    def __init__(self):
        self.hp = 100


class Besiegement:
    """ Besiegement """

    def __init__(self):
        self.starting_message = 'start\n'
        self.win_message = 'win'
        self.lose_message = 'lose'
        self.chose_weapon = 'chose weapon (high-range (high) / low-range (low)) or wait?'
        self.weapon_use = ('high', 'low', 'wait')
        self.charge_use = ('small', 'average', 'large')
        self.chose_charge = 'how much to charge?\n-small (20-25)\n-average (40-50)\n-large (80-95)'
        self.chose_supply = f'1)low-range - 60\n2)low-range - 30, high-range - 50\n3)high-range - 100'
        self.weapon_choice_error = f'choice error, select from the proposed list: {self.weapon_use}'
        self.charge_choice_error = f'choice error, select from the proposed list: {self.charge_use}'
        self.chose_shot_coordinates = 'chose shot coordinates (x y). remember, the weather affects the shot'
        self.shot_coordinates_error = f'wrong format, entered coordinates must be of the form "x y"'
        self.excess = 'selected coordinates are greater than the attack range'
        self.complexity = 0
        self.high_range_weapon = HRWeapon()
        self.low_range_weapon = LRWeapon()
        self.enemies = Enemies()
        self.base = Base()
        self.wind = Wind()
        self.player_weapon_type_choice = None

    def spawn_enemies(self):
        """ increases amount of enemies """

        self.enemies.value = random.randint(2 * self.complexity + 10, 2 * self.complexity + 30)
        self.enemies.speed = random.choice(self.enemies.speed_values)
        self.enemies.direction = random.choice(list(self.enemies.direction_values.keys()))
        self.enemies.coordinates = [random.randint(50, 70), random.randint(50, 70)]
        self.complexity += 1

    def spawn_wind(self):
        """ change weather """

        self.wind.speed = random.choice(self.wind.speed_values)
        self.wind.direction = random.choice(list(self.wind.direction_values.keys()))

    def use_hrweapon(self):
        pass

    def run(self):
        """ main game loop """

        print(self.starting_message)
        while self.base.hp > 0:
            print(f'base integrality = {self.base.hp}')
            print(f'low-range: {self.low_range_weapon.ammo}')
            print(f'high-range: {self.high_range_weapon.ammo}\n')

            if self.player_weapon_type_choice != self.weapon_use[2]:
                # generate enemies and weather
                self.spawn_enemies()

            self.spawn_wind()

            enemies_information = 'enemy detected:\n' \
                                  f'amount = {self.enemies.value}\n' \
                                  f'speed = {self.enemies.speed}\n' \
                                  f'coordinates = {(self.enemies.coordinates[0], self.enemies.coordinates[1])}\n' \
                                  f'direction = {self.enemies.direction}\n'
            print('scanning territory... ')

            print(enemies_information)

            wind_information = 'weather changes detected:\n' \
                               f'speed = {self.wind.speed}\n' \
                               f'direction = {self.wind.direction}\n'
            print('analyze data from weather stations...')

            print(wind_information)

            # chose weapon type
            print(self.chose_weapon)
            self.player_weapon_type_choice = None
            while self.player_weapon_type_choice is None:
                self.player_weapon_type_choice = input().replace(' ', '').lower()
                if not (self.player_weapon_type_choice == self.weapon_use[0] or
                        self.player_weapon_type_choice == self.weapon_use[1] or
                        self.player_weapon_type_choice == self.weapon_use[2]):
                    print(self.weapon_choice_error)
                    self.player_weapon_type_choice = None

            if self.player_weapon_type_choice != self.weapon_use[2]:

                # chose amount of charging
                print(self.chose_charge)
                player_weapon_charge_choice = None
                while player_weapon_charge_choice is None:
                    player_weapon_charge_choice = input().replace(' ', '').lower()
                    if not (player_weapon_charge_choice == self.charge_use[0] or
                            player_weapon_charge_choice == self.charge_use[1] or
                            player_weapon_charge_choice == self.charge_use[2]):
                        print(self.charge_choice_error)
                        player_weapon_charge_choice = None
                else:
                    if player_weapon_charge_choice == self.charge_use[0]:
                        charged_ammo = random.randint(20, 25)
                    elif player_weapon_charge_choice == self.charge_use[1]:
                        charged_ammo = random.randint(40, 50)
                    else:
                        charged_ammo = random.randint(80, 95)

                # chose shot coordinates
                print(self.chose_shot_coordinates)
                player_shot_coordinates_choice = None
                while player_shot_coordinates_choice is None:
                    player_shot_coordinates_choice = input()
                    if not re.fullmatch(r'\d{,2} \d{,2}', player_shot_coordinates_choice):
                        print(self.shot_coordinates_error)
                        player_shot_coordinates_choice = None
                    else:
                        match = re.findall(r'\d\d', player_shot_coordinates_choice)
                        player_shot_coordinates_choice = [int(match[0]), int(match[1])]
                        if self.player_weapon_type_choice == self.weapon_use[0] and \
                                (self.high_range_weapon.attack_range < int(match[0]) or
                                 self.high_range_weapon.attack_range < int(match[1])):
                            print(self.excess)
                            player_shot_coordinates_choice = None
                        if self.player_weapon_type_choice == self.weapon_use[1] and \
                                (self.high_range_weapon.attack_range < int(match[0]) or
                                 self.high_range_weapon.attack_range < int(match[1])):
                            print(self.excess)
                            player_shot_coordinates_choice = None

                # change enemies coordinates, making a shot
                direction = self.enemies.direction
                self.enemies.coordinates = [
                    self.enemies.coordinates[0] + (self.enemies.speed // 50) *
                    self.enemies.direction_values[direction][0],
                    self.enemies.coordinates[1] + (self.enemies.speed // 50) *
                    self.enemies.direction_values[direction][1]
                ]

                shot_coordinates = [
                    player_shot_coordinates_choice[0] + (self.wind.speed // 50) *
                    self.wind.direction_values[self.wind.direction][0],
                    player_shot_coordinates_choice[1] + (self.wind.speed // 50) *
                    self.wind.direction_values[self.wind.direction][1]
                ]

                if shot_coordinates == self.enemies.coordinates:
                    self.enemies.value -= charged_ammo
                    print(f'you destroyed {charged_ammo} enemies')
                if self.player_weapon_type_choice == self.weapon_use[0]:
                    self.high_range_weapon.ammo -= charged_ammo
                    print(f'{self.high_range_weapon.ammo} left')
                else:
                    self.low_range_weapon.ammo -= charged_ammo
                    print(f'{self.low_range_weapon.ammo} left')

            else:
                print('supply or skip?')
                supply_fork = None
                while supply_fork is None:
                    supply_fork = input().replace(' ', '').lower()
                    if supply_fork not in ('supply', 'skip'):
                        print('choice error')
                        supply_fork = None

                if supply_fork == 'skip':
                    direction = self.enemies.direction
                    self.enemies.coordinates = [
                        self.enemies.coordinates[0] + (self.enemies.speed // 50) *
                        self.enemies.direction_values[direction][0],
                        self.enemies.coordinates[1] + (self.enemies.speed // 50) *
                        self.enemies.direction_values[direction][1]
                    ]
                    if self.enemies.coordinates[0] <= 0 or self.enemies.coordinates[1] <= 0:
                        self.base.hp -= self.enemies.value
                        self.player_weapon_type_choice = None
                else:
                    print(self.chose_supply)
                    supply = None
                    while supply is None:
                        supply = int(input())
                        if supply not in (1, 2, 3):
                            print('choice error')
                            supply = None
                        elif supply == 1:
                            self.low_range_weapon.ammo += 60
                            print('supplied 60 ammo for low range weapon')
                        elif supply == 2:
                            self.low_range_weapon.ammo += 30
                            self.high_range_weapon.ammo += 50
                            print('supplied 30 ammo for low range weapon')
                            print('supplied 50 ammo for high range weapon')
                        else:
                            self.high_range_weapon.ammo += 100
                            print('supplied 100 ammo for high range weapon')

        else:
            print(self.lose_message)


Besiegement().run()
