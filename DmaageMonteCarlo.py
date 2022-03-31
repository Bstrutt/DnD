import numpy.random as rn


def turnDamage():
    SHORTSWORD_FREE_DAM = 6
    UNARMED_FREE_DAM = 4
    damage = 0
    a = rn.randint(1, 5)
    if a == 1:
        return damage
    else:
        damage = a + rn.randint(1, 3) + SHORTSWORD_FREE_DAM

    b = rn.randint(1, 5)
    if b == 1:
        return damage
    else:
        damage = damage + b + rn.randint(1, 3) + SHORTSWORD_FREE_DAM

    c = rn.randint(1, 5)
    if c == 1:
        return damage
    else:
        damage = damage + c + UNARMED_FREE_DAM

    d = rn.randint(1, 5)
    if d == 1:
        return damage
    else:
        damage = damage + d + UNARMED_FREE_DAM

    return damage

def damageSim(x):
  totalDamage = 0
  for i in range (0, x):
    totalDamage = totalDamage + turnDamage()
  return totalDamage


print(damageSim(10000)/ 10000)
