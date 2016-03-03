def rabbitsPop(n, k):
    adultsPerMonth = [0, 1]

    for i in range(2, n-1):
        adultsPerMonth.append(adultsPerMonth[i-1] + k  * adultsPerMonth[i-2])

    totalPop = adultsPerMonth[n-2] + k * (adultsPerMonth[n-2] + adultsPerMonth[n-3])

    return totalPop

n = int(raw_input("insert variable n:"))
k = int(raw_input("insert variable k:"))

print rabbitsPop(n, k)
