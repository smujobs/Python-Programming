def fahrenheit_to_celsius(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

def get_real(prompt):
    real_number = float(input(prompt))
    return real_number

f_temp = get_real('변환하고자 하는 화씨 온도는? : ')
c_temp = fahrenheit_to_celsius(f_temp)
print(f'화씨 {f_temp} 도는 섭씨 {c_temp} 도')