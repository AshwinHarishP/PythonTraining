from functools import reduce
res = lambda x: x * 10
print(res(10))

mul = lambda a, b, c: a * b * c
print(mul(10, 20, 30))


salary = [1000, 2000, 3000, 4000, 5000, 51555]
print(list(map(lambda x: x + 500, salary)))

filterEg = list(filter(lambda x:(x % 2 != 0), salary))
print(filterEg)

reduceEg = reduce(lambda x, y: x + y, salary)
print(reduceEg)

no = [20, 30, 40, 50]
res = iter(no)

for i in res:
    print(res)
print(next(res))
print(next(res))