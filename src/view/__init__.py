class View:
    @staticmethod
    def print_list(a_list: list):
        for item in a_list:
            print(item, end="")

    @staticmethod
    def msg(text: str, dashes: int):
        print("-" * dashes)
        print(text.center(dashes))
        print("-" * dashes)

    @staticmethod
    def clean_prompt():
        from os import system, name
        system("cls" if name == "nt" else "clear")

    @staticmethod
    def draw_gallows(quantity_of_errors):
        if quantity_of_errors == 0:
            print("\u2796\u2796\u2796\u2796\u2796\u2796")  # Unicode character minus.
            print("|           |")
            print("|")
            print("|")
            print("|")
        elif quantity_of_errors == 1:
            print("\u2796\u2796\u2796\u2796\u2796\u2796")
            print("|           |")
            print("|         ", u"\U0001F635")  # Unicode's character face with crossed-out eyes.
            print("|")
            print("|")
        elif quantity_of_errors == 2:
            print("\u2796\u2796\u2796\u2796\u2796\u2796")
            print("|           |")
            print("|         ", u"\U0001F635")
            print("|          \\")
            print("|")
        elif quantity_of_errors == 3:
            print("\u2796\u2796\u2796\u2796\u2796\u2796")
            print("|           |")
            print("|         ", u"\U0001F635")
            print("|          \\/")
            print("|")
        elif quantity_of_errors == 4:
            print("\u2796\u2796\u2796\u2796\u2796\u2796")
            print("|           |")
            print("|         ", u"\U0001F635")
            print("|          \\/")
            print("|          /")
        else:
            print("\u2796\u2796\u2796\u2796\u2796\u2796")
            print("|           |")
            print("|         ", u"\U0001F635")
            print("|          \\/")
            print("|          /\\")
