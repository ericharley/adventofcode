items = [[79, 98],
         [54, 65, 75, 74],
         [79, 60, 97],
         [74]]

ops = [lambda old : old * 19,
       lambda old : old + 6,
       lambda old : old * old,
       lambda old : old + 3]

mods = [23, 19, 13, 17]
def prod(l):
  if l == []:
    return 1
  else:
    return l[0] * prod(l[1:])

mod = prod(mods)

d = {}
d[0] = {True: 2, False: 3}
d[1] = {True: 2, False: 0}
d[2] = {True: 1, False: 3}
d[3] = {True: 0, False: 1}

N = len(items)


class Monkey:
  def __init__(self, items, l, m, t):
    self.items = items
    self.op = l
    self.mod = m
    self.t = t
    self.count = 0

Monkeys = list(range(N))
for i in range(N):
 Monkeys[i] = Monkey(items[i], ops[i], mods[i], d[i])
#Monkeys[1] = Monkey(items[1], ops[1], mods[1], d[1])
#Monkeys[2] = Monkey(items[2], ops[2], mods[2], d[2])
#Monkeys[3] = Monkey(items[3], ops[3], mods[3], d[3])

def print_monkeys():
  for m in range(N):
    M = Monkeys[m]
    print(f'Monkey {m}: {M.items}')
  print()

def print_monkeys_count():
  for m in range(N):
    M = Monkeys[m]
    print(f'Monkey {m} inspected items {M.count} times.')
  print()

p = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

for r in range(10000):
#  print('.',end='')
#  if r % 100 == 0:
#    print()
  if r in p:
    print(f"Round {r}:")
    print_monkeys_count()

  for m in range(N):
    M = Monkeys[m]
    while M.items:
      M.count += 1
      item = M.items.pop(0)
      item = M.op(item) % mod
      Monkeys[M.t[item % M.mod == 0]].items.append(item)

#print(f"Round 20:")
#print_monkeys()

r = 10000
print(f"Round {r}:")
print_monkeys_count()

#print_monkeys_count()

l = [ Monkeys[r].count for r in range(N) ]
l.sort()
monkey_business = l[-1]*l[-2]
print(monkey_business)
