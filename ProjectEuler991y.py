from timeit import default_timer as timer
from math import isqrt, gcd

# The eq. is a/(b+p) + (b+p)/(a+p) = 4
#
# If (a,b,p) with a,b,p in N is a solution, then for any k in N, k*(a,b,p) is also a solution.
# Therefore, for each primitive solution, we must add all scaled versions
# sum + 2*sum + ... + k_max*sum = sum*k_max*(k_max+1)//2 
# where k_max = limit // (a+b+p) and sum = a+b+p
#
# Let x = a+p and y = b+p.
# The eq. becomes p = ( x**2 -4xy +y**2) // x
# For p to be an integer, x must divide y**2, i.e. x | y**2.
# Let d = gcd(x,y).
# x=du and y=dv with gcd(u,v)=1.
# Then u | dv**2 => u | d => d=ku for some integer k.
# Hence x = ku**2 and y = kuv.
# Substituting back, we obtain
# p = k(u**2 -4uv + v**2)
# and a = kv(4u - v), b = k(-u**2 +5uv -v**2), sum = kv(5u - v)
#
# To ensure a > 0, b > 0, p > 0, u and v must satisfy 
# (1) 1/4 < u/v < 2-sqrt(3) 
# or 
# (2) 2+sqrt(3) < u/v < (5+sqrt(21)) / 2
#
# From (1), u < v and since sum <= 10**7, we get
# u < sqrt(10**7 / 4)
#
# From (2), u_max = v(5+sqrt(21)) / 2 => 10v**2 < sum_u_max <= 10**7, and we have
# v < 10**3

# sol: 23871972654940
def pr991(): # execution time: 0.0955
    start = timer()
    
    limit = 10_000_000
    total = 0

    for u in range( 1, isqrt(limit//4) ):
        v_min = 2*u + isqrt(3*u*u) + 1
        v_max = 4*u - 1

        for v in range( v_min, v_max+1 ):
            if gcd(u,v) == 1:
                sum = v*(5*u - v)
                if sum < limit:
                    k_max = limit // sum
                    total += sum*k_max*(k_max+1) // 2

    for v in range( 1, 1000 ):
        u_min = 2*v + isqrt(3*v*v) + 1
        u_max = (5*v + isqrt(21*v*v)) // 2

        for u in range( u_min, u_max+1 ):
            if gcd(u,v) == 1:
                sum = v*( 5*u-v )
                if sum < limit:
                    k_max = limit // sum
                    total += sum*k_max*(k_max+1) // 2

    print(f'execution time: {timer()-start:.4f}')
    return total

print(f'result pr991: {pr991()}')