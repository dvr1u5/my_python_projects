n = input()
num = int(n[1:])
comments = []
for i in range(2, int(num)):
    text = input()
    if text.find('#') == -1:
        print(text)
    else:
        print(text[:text.find('#')])
