memo = {0:1, 1:0, 2:1}
def adultRabbits(n, m):
    arg = n
    if arg in memo:
        return memo[arg]
    
    if n < 0:
        result = 0

    else:
        result = adultRabbits(n-1, m) + adultRabbits(n-2, m) - adultRabbits(n-1-m, m)
        memo[arg] = result
        
    return result

def totRabbits(n, m):
    return adultRabbits(n, m) + adultRabbits(n-1, m)



n = int(raw_input("insert variable n:"))
m = int(raw_input("insert variable m:"))

print totRabbits(n, m)
