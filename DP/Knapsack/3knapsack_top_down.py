def main():
    wt = []
    val = []

    w = int(input("Enter weight of the knapsack: "))
    l = int(input("Enter size of input: "))

    for i in range(0, l):
        ewt = int(input("weight: "))
        evl = int(input("Value: "))

        wt.append(ewt)
        val.append(evl)

    arr = [[0 for x in range(w + 1)] for x in range(l + 1)]

    for i in range(l + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            if wt[i - 1] <= j:
                arr[i][j] = max(val[i - 1] + arr[i - 1][j - wt[i - 1]], arr[i - 1][j])
            else:
                arr[i][j] = arr[i - 1][j]

    print(arr[l][w])


if __name__ == "__main__":
    main()
