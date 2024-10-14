def fibonaccci(n):
    if not dict.items(n):
        return dict[n]
    else:
        dict[n] = fibonaccci(n-2)+fibonaccci(n-1)
        return dict[n]


dict = {
    1: 1, 2: 1
}
print(fibonaccci(2))
