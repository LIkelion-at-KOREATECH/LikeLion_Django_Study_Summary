'''
Statement
Given a three-digit integer X consisting of three different digits, print "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.

Example input #1
179

Example output #1
YES

Example input #2
197

Example output #2
NO
'''
X = input()

if X[0] > X[1] or X[1] > X[2]:
    print("NO")

else:
    print("YES")
