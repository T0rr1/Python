class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def status(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                selection = input(
                    'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                if selection == '1':
                    self.espresso()
                    continue
                elif selection == '2':
                    self.latte()
                    continue
                elif selection == '3':
                    self.cappuccino()
                    continue
                elif selection == 'back':
                    continue
            elif action == 'fill':
                add_water = int(input('Write how many ml of water do you want to add:'))
                add_milk = int(input('Write how many ml of milk do you want to add:'))
                add_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
                add_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
                self.water += add_water
                self.milk += add_milk
                self.beans += add_coffee
                self.cups += add_cups

            elif action == 'take':
                print(f'I gave you ${self.money}')
                self.money -= self.money

            elif action == 'remaining':
                print('The coffee machine has:')
                print(f'{self.water} of water')
                print(f'{self.milk} of milk')
                print(f'{self.beans} of coffee beans')
                print(f'{self.cups} of disposable cups')
                print(f'{self.money} of money')
            elif action == 'exit':
                break

    def espresso(self):
        # Espresso
        esp_water = 250
        esp_coffee = 16
        esp_cost = 4
        # Check if there is enough water to make the espresso
        if esp_water > self.water:
            print('Sorry, not enough water!')
        # Check if there is enough coffee to make the espresso
        elif esp_coffee > self.beans:
            print('Sorry, not enough coffee!')
        # If there is enough then make it and re-calculate amounts
        elif self.water >= esp_water and self.beans >= esp_coffee:
            print('I have enough resources, making you a coffee!')
            self.water -= esp_water
            self.milk += 0
            self.beans -= esp_coffee
            self.cups -= 1
            self.money += esp_cost

    def latte(self):
        # Latte
        lat_water = 350
        lat_milk = 75
        lat_coffee = 20
        lat_cost = 7
        # Check if there is enough water to make the latte
        if lat_water > self.water:
            print('Sorry, not enough water!')
        # Check if there is enough coffee to make the latte
        elif lat_milk > self.milk:
            print('Sorry, not enough milk!')
        # Check if there is enough milk to make the latte
        elif lat_coffee > self.beans:
            print('Sorry, not enough coffee!')
        # If there is enough then make it and re-calculate amounts
        elif self.water >= lat_water and self.beans >= lat_coffee and self.milk >= lat_milk:
            print('I have enough resources, making you a coffee!')

            self.water -= lat_water
            self.milk -= lat_milk
            self.beans -= lat_coffee
            self.cups -= 1
            self.money += lat_cost

    def cappuccino(self):
        # Cappuccino
        cap_water = 200
        cap_milk = 100
        cap_coffee = 12
        cap_cost = 6
        # Check if there is enough water to make the cap
        if cap_water > self.water:
            print('Sorry, not enough water!')
        # Check if there is enough coffee to make the cap
        elif cap_milk > self.milk:
            print('Sorry, not enough milk!')
        # Check if there is enough milk to make the cap
        elif cap_coffee > self.beans:
            print('Sorry, not enough coffee!')
        # If there is enough then make it and re-calculate amounts
        elif self.water >= cap_water and self.beans >= cap_coffee and self.milk >= cap_milk:
            print('I have enough resources, making you a coffee!')

            self.water -= cap_water
            self.milk -= cap_milk
            self.beans -= cap_coffee
            self.cups -= 1
            self.money += cap_cost


new_cm = CoffeeMachine(400, 540, 120, 9, 550)
new_cm.status()
