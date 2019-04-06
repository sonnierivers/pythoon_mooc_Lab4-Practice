# -*- coding: utf-8 -*-


#input
def input_celsius_value():
      user_input=input("input the celsius value you want to convert:")
      celsius=float(user_input)
      return(celsius)

#converting
def convert_celsius_fahrenheit(celsius_value):
    fahrenheit=((9/5)*float(celsius_value))+32
    return(fahrenheit)

def print_fahrenheit_value(celsius_value,fahrenheit):
    print("celsius_value:",celsius_value)
    print("fahrenheit:",fahrenheit)
    return

def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    celsius_value=input_celsius_value()
    fahrenheit_value=convert_celsius_fahrenheit(celsius_value)
    print_fahrenheit_value(celsius_value,fahrenheit_value)
    # ======================================

    print("===========================")
    print("프로그램이 종료 되었습니다.")

#calling the main function
if __name__ == '__main__':
    celsius_value = input_celsius_value()
    print(celsius_value)

    main()
