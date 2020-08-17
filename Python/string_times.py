
def string_time(str, times):
    message = ""
    for i in range(times):
        message += str
    print(message)

txt = input("Enter string: ")
times = int(input("Number: "))

string_time(txt, times)
