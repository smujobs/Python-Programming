def get_input(prompt_message):
    user_input = input(prompt_message)
    return user_input

def rep_char(char, num):
    print(char * num)

def draw_line_string(name_to_welcome):
    msg1 = f'Hello {name_to_welcome},'
    msg2 = 'Welcome to Seoul.'
    length_of_border = len(msg1) if len(msg1) > len(msg2) else len(msg2)

    rep_char('-', length_of_border + 2)
    print(f' {msg1}')
    print(f' {msg2}')
    rep_char('-', length_of_border + 2)

name_to_welcome = get_input('Input his/her name: ')
draw_line_string(name_to_welcome)