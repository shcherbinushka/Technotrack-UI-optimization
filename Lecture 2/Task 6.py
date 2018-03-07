print('Введите фразу')
n = input()

phrase = "".join(n.split(" "))
        
reverse = phrase[::-1]

if phrase == reverse:
    print("Палиндром")
else:
    print("Не палиндром")
