import random
import match

# Put your DB here
words_list = ["Apple", "Banana", "Orange", "Pear", "Peach", "Grape", "Strawberry", "Blueberry", "Raspberry",
              "Blackberry", "Watermelon", "Pineapple", "Mango", "Lemon", "Lime", "Cherry", "Apricot", "Plum",
              "Pomegranate", "Kiwi", "Cantaloupe", "Cucumber", "Tomato", "Potato", "Onion", "Garlic", "Carrot",
              "Broccoli", "Cabbage", "Spinach", "Lettuce", "Corn", "Peas", "Mushroom", "Pumpkin", "Squash", "Zucchini",
              "Cauliflower", "Asparagus", "Eggplant", "Avocado", "Cranberry", "Papaya", "Coconut", "Peanut", "Almond",
              "Cashew", "Walnut", "Hazelnut", "Pistachio", "Macadamia", "Pecan", "Sunflower", "Sesame", "Pine", "Oak",
              "Maple", "Birch", "Cedar", "Elm", "Hickory", "Ash", "Beech", "Cottonwood", "Sycamore", "Willow", "Pine",
              "Oak", "Maple", "Birch", "Cedar", "Elm", "Hickory", "Ash", "Beech", "Cottonwood", "Sycamore", "Willow",
              "Pine", "Oak", "Maple", "Birch", "Cedar", "Elm", "Hickory", "Ash", "Beech", "Cottonwood", "Sycamore",
              "Willow", "Pine", "Oak", "Maple", "Birch", "Cedar", "Elm", "Hickory", "Ash", "Beech", "Cottonwood",
              "Sycamore", "Willow", "Pine", "Oak", "Maple", "Birch", "Cedar", "Elm", "Hickory", "Ash", "Beech",
              "Cottonwood", "Sycamore", "Willow", "Pine", "Oak", "Maple"]


def main():
    chosen_word = random.choice(words_list).lower()

    print("Enter exit to quit, or enter a letter to guess the word")
    print("I will reveal the word if you will choose to quit")

    while True:
        word_input = input("\n\nEnter input: ").lower()

        if "exit" == word_input or "quit" == word_input:
            print("\n\nThe word was:", chosen_word)
            break

        print("\nThe total match to the real word is " + str(match.compare_words(chosen_word, word_input)) + "%")
        print("Length match:", match.get_length_score(chosen_word, word_input) * 100, "%")
        print("Letters match:", match.get_letters_score(chosen_word, word_input) * 100, "%")
        print("Order match:", match.get_order_score(chosen_word, word_input) * 100, "%")

        if word_input.lower() == chosen_word.lower():
            print("\nYou got it!!!\n")
            break


if __name__ == '__main__':
    main()
