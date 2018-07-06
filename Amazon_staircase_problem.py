'''
This problem is adapted from Amazon interview question https://www.youtube.com/watch?v=5o-kdjv7FD0 (described in 1st 55 s - 2m)
'''

N = 3
max_steps = 2
X = [i for i in range (1, max_steps+1)]

print (f'Start of problem - N: {N}, max_steps: {max_steps}, X: {X} \n\n')



glob = 0
# input N, output is number of ways to reach the top.
def num_ways(n):
    global glob
    glob +=1
    print(f'{glob}: num_ways called with {n}')
    m = 0
    if n < 0:
        print(f'{glob}: returning 0')
        glob -=1
        return 0
    elif n==0:
        print(f'{glob}: returning 1')
        glob -=1
        return 1
    else:
        for each in X:
            print(f'{glob}: calling numways n:{n}, each:{each} n-each: {n-each} ')
            m += num_ways(n-each)
            print(f'{glob}: m now is {m}')
        print(f'{glob}: returning {m}')
        glob -=1
    return m

print (f'number of ways = {num_ways(N)}')
