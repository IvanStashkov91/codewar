def dig_pow(n, p):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += pow(int((n[i])), (p + i))
    if sum % int(n) == 0:
        return sum / int(n)
    return -1

print(dig_pow(46288, 3))
#################################################
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

print(dig_pow(46288, 3))

# # dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# # dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# # dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# # dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51