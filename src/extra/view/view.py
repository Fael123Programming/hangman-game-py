from extra.singleton_meta.singleton_meta import SingletonMeta
import os


class View(metaclass=SingletonMeta):

    @staticmethod
    def stringify_list(a_list: list) -> str:
        string = ""
        for item in a_list:
            string += str(item)
        return string

    @staticmethod
    def msg(text: str, dashes=150, show_upper_line=True, show_lower_line=True):
        if show_upper_line:
            View.row(dashes)
        print(text.center(dashes))
        if show_lower_line:
            View.row(dashes)

    @staticmethod
    def load(msg: str, dashes: int):
        assert dashes >= 0, f"Dashes {dashes} must be non-negative!"
        from time import sleep
        messages = ["Loading packages...", "Waking database up...", "Preparing environment...", "Initializing..."]
        view = View()
        load_bar = "["
        messages_index = 0
        aux_counter = 0
        view.msg(msg, dashes)
        print(load_bar, messages[messages_index], sep="\n")
        counter = 1
        while counter < dashes - 2:
            load_bar += "*"
            sleep(0.1)
            view.clean_prompt()
            view.msg(msg, dashes)
            print(load_bar, messages[messages_index], sep="\n")
            if aux_counter == int(dashes / 4):
                messages_index += 1
                aux_counter = 0
            counter += 1
            aux_counter += 1
        view.clean_prompt()
        load_bar += "*]"
        view.msg(msg, dashes)
        print(load_bar, messages[messages_index], sep="\n")
        sleep(0.1)
        view.clean_prompt()

    @staticmethod
    def clean_prompt():
        os.system("cls" if os.name in ("nt", "dos") else "clear")

    @staticmethod
    def draw_gallows(quantity_of_errors: int):
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

    @staticmethod
    def row(dashes=150):
        assert dashes > 0, f"Dashes {dashes} must be > 0"
        print("-" * dashes)

    @staticmethod
    def stop(secs=1.0):
        from time import sleep
        sleep(secs)
