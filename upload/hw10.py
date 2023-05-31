import pickle
import os

class Score_file:
    
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
    
    def get_user_input(self, message_to_show: str) -> str:
        user_input: str = input(message_to_show)
        return user_input
    
    def calculate_average(self, list_of_nums: list) -> float:
        average_of_nums: float = sum(list_of_nums) / len(list_of_nums)
        return average_of_nums
    
    def check_file_existence(self) -> bool:
        is_file_exists: bool = os.path.isfile(self.filename)
        return is_file_exists
    
    def get_score_input(self) -> list:
        score_number_counter: int = 1
        inputed_score_list:list = []

        print('[Input Scores:]')
        while True:
            user_input: int = int(self.get_user_input(f'#{score_number_counter}?: '))

            if user_input >= 0:
                inputed_score_list.append(user_input)
                score_number_counter += 1
            else:
                break
                
        return inputed_score_list
    
    def write_file(self, score_list) -> None:
        with open(self.filename, 'wb') as file:
            pickle.dump(score_list, file)
            pickle.dump(self.calculate_average(score_list), file)
    
    def read_file(self) -> None:
        with open(self.filename, 'rb') as file:
            read_score_list = pickle.load(file)
            average_of_scores = pickle.load(file)
            rounded_average_of_scores = round(average_of_scores, 1)


            print('[Scores]')
            print('Individual score: ', end='')

            for score in read_score_list:
                print(score, end=' ')

            print(f'\nAverage: {rounded_average_of_scores}')

# Main Program

score_file = Score_file(input('Enter file name: '))

if score_file.check_file_existence():
    score_file.read_file()
else:
    score_list: list = score_file.get_score_input()
    score_file.write_file(score_list)
    score_file.read_file()