def fact_recur(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_recur(n - 1)


number = 7
res = fact_recur(number)
print("The factorial of {} is {}.".format(number, res))