def knapsack(wt, val, w, l):
    if l == -1 or w == 0:
        return 0
    if wt[l] <= w:
        return max(
            val[l] + knapsack(wt, val, w - wt[l], l - 1), knapsack(wt, val, w, l - 1)
        )
    else:
        return knapsack(wt, val, w, l - 1)


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

    print(knapsack(wt, val, w, l - 1))


if __name__ == "__main__":
    main()
