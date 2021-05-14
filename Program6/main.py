# Print perfect square numbers between 1to50


for i in range(1, int(50 / 5)):
    x = pow(i, 2)
    if x < 50:
        print(x)
    else:
        break
