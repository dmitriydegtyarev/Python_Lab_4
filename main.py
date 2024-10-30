import re

lorem_ipsum = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."

def count_word():
    """
    Підраховує кількість слів у реченні.
    """
    print(f"В даному реченні {len(lorem_ipsum.split())} слово (слів)")

def replace_space():
    """
    Замінює пробіли на символи нижнього підкреслювання (2 способами).
    """
    change_lorem = lorem_ipsum.split()
    print(f"Заміна пробілів за допомогою функцій split та join ->>>\n{'_'.join(change_lorem)}")

    print(f"Заміна пробілів за допомогою функції replace ->>>\n{lorem_ipsum.replace(' ', '_')}")

def find_numbers():
    """
    Добуває всі числа з рядка.
    """
    pattern = r"\d+"
    numbers = re.findall(pattern, lorem_ipsum)

    print(f"В даному реченні зустрічаються наступні числові значення ->>>\n{numbers}")

def to_upper():
    """
    Переводить всі символи рядка в верхній регістр.
    """
    print(f"Речення в верхньому регістрі ->>>\n{lorem_ipsum.upper()}")

count_word()
replace_space()
find_numbers()
to_upper()