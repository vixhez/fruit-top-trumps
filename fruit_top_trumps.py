import random
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
​
def random_fruit():
    requests.get("https://www.fruityvice.com/api/fruit/all/", verify=False)
    fruit_number = random.randint(1, 6)
    url = 'https://www.fruityvice.com/api/fruit/{}/'.format(fruit_number)
    response = requests.get(url, verify=False)
    fruit = response.json()
    return {
        'name': fruit['name'],
        'id': fruit['id'],
        'protein': fruit['nutritions']['protein'],
        'sugar': fruit['nutritions']['sugar'],
}
​
random_fruit()
​
def run():
    print("Welcome to the War of the Fruits! May the pineapple and raspberry Goddesses be in your favour...")
    time.sleep(0.5)
    print(" ")
    print(". ~ . ~ .")
    print(" ")
    time.sleep(2)
    print("Gaaah, the suspense!")
    time.sleep(0.5)
    print(" ")
    print(". ~ . ~ .")
    print(" ")
    my_fruit = random_fruit()
    time.sleep(2)
    print('Your fruit is the almighty {}!'.format(my_fruit['name']))
    time.sleep(0.5)
    print(" ")
    print(". ~ . ~ .")
    print(" ")
    time.sleep(2)
    stat_choice = input('How would you like to compare your fruit to that of your opponent?!! ... By ID number, protein content or sugar levels? [ id / protein / sugar ] ')
    opponent_fruit = random_fruit()
    time.sleep(0.5)
    print(" ")
    print(". ~ . ~ .")
    print(" ")
    time.sleep(2)
    print('Your fruity opponent chose {}!'.format(opponent_fruit['name']))
    my_stat = my_fruit[stat_choice]
    opponent_stat = opponent_fruit[stat_choice]
    if my_stat > opponent_stat:
        time.sleep(2)
        print(" ")
        print("\U0001F929 \U0001F929 \U0001F929 \U0001F929")
        time.sleep(1)
        print(" ")
        print('You are the fruitiest!! Congratulations!')
        time.sleep(1)
        print(" ")
        answer = input("Play again? [yes / no] ")
        if answer == "yes":
            time.sleep(1)
            print(" ")
            print(".................")
            print(" ")
            run()
        else:
            quit()
​
    elif my_stat < opponent_stat:
        time.sleep(2)
        print(" ")
        print("\U0001F635 \U0001F635 \U0001F635 \U0001F635")
        time.sleep(1)
        print('Unfortunately, you are not the fruitiest...')
        time.sleep(1)
        print(" ")
        answer = input("Play again? [yes / no] ")
        if answer == "yes":
            time.sleep(1)
            print(" ")
            print(".................")
            print(" ")
            run()
        else:
            quit()
    else:
        time.sleep(2)
        print(" ")
        print("\U0001F46F \U0001F46F \U0001F46F \U0001F46F")
        time.sleep(1)
        print('Both you and your opponent are incredibly fruity!')
        time.sleep(1)
        print(" ")
        answer = input("Play again? [yes / no] ")
        if answer == "yes":
            time.sleep(1)
            print(" ")
            print(".................")
            print(" ")
            run()
        else:
            quit()
​
run()