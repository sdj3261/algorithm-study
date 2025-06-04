count = 0
num = 666
while True:
    if '666' in str(num):
        count += 1
        if count % 1000 == 0:
            print(f"{count}번째: {num}, 자릿수: {len(str(num))}")
        if count == 9999:
            break
    num += 1
