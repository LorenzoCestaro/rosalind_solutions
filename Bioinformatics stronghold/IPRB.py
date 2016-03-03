import math

k = int(raw_input("Insert number of dominant homozygous individuals:"))
m = int(raw_input("Insert number of dominant heterozygous individuals:"))
n = int(raw_input("Insert number of recessive homozygous individuals:"))

tot_pop = k+m+n

# CALCULATE TOTAL POSSIBLE CHILD OUTCOMES
tot_childs = 0
i = tot_pop-1
while i >= 1:
    tot_childs += i*4
    i-=1

# CALCULATE TOTAL POSSIBLE A_CHILDS DERIVING FROM k ONLY COUPLES
kk_childs = 0
i = k-1
while i >= 1:
    kk_childs += i*4
    i-=1

# CALCULATE TOTAL POSSIBLE A_CHILDS DERIVING FROM k-m COUPLES
km_childs = k*m*4

# CALCULATE TOTAL POSSIBLE A_CHILDS DERIVING FROM k-n COUPLES
kn_childs = k*n*4

# CALCULATE TOTAL POSSIBLE A_CHILDS DERIVING FROM m ONLY COUPLES
mm_childs = 0
i = m-1
while i >= 1:
    mm_childs += i*3
    i-=1

# CALCULATE TOTAL POSSIBLE A_CHILDS DERIVING FROM m-n COUPLES
mn_childs = m*n*2


A_childs = kk_childs + km_childs +kn_childs + mm_childs + mn_childs


print float(A_childs)/tot_childs
