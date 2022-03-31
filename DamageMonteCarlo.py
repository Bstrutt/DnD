import numpy.random as rn
import statistics

def turnDamage(enemy_ac):
    SHORTSWORD_FREE_DAM = 5
    UNARMED_FREE_DAM = 3
    SHORTSWORD_HIT_PLUS = 8
    UNARMED_HIT_PLUS = 6
    damage = 0

    a = rn.randint(1, 21)
    if a == 1:
        return damage
    elif a == 20:
      damage = damage + rn.randint(1,7) + rn.randint(1,7) + rn.randint(1, 5) + SHORTSWORD_FREE_DAM
    elif (a + SHORTSWORD_HIT_PLUS) >= enemy_ac:
        damage = damage + rn.randint(1,7) + rn.randint(1, 5) + SHORTSWORD_FREE_DAM

    b = rn.randint(1, 21)
    if b == 1:
        return damage
    elif b == 20:
      damage = damage + rn.randint(1,7) + rn.randint(1,7) + rn.randint(1, 5) + SHORTSWORD_FREE_DAM
    elif (b + SHORTSWORD_HIT_PLUS) >= enemy_ac:
        damage = damage + rn.randint(1,7) + rn.randint(1, 5) + SHORTSWORD_FREE_DAM

    c = rn.randint(1, 21)
    if c == 1:
        return damage
    elif c == 20:
      damage = damage + rn.randint(1,7) + rn.randint(1,7) + UNARMED_FREE_DAM  
    elif (c + UNARMED_HIT_PLUS) >= enemy_ac:
        damage = damage + rn.randint(1,7) + UNARMED_FREE_DAM

    d = rn.randint(1, 21)
    if d == 1:
        return damage
    elif d == 20:
      damage = damage + rn.randint(1,7) + rn.randint(1,7) + UNARMED_FREE_DAM  
    elif (d + UNARMED_HIT_PLUS) >= enemy_ac:
        damage = damage + rn.randint(1,7) + UNARMED_FREE_DAM

    return damage

def damageSim(x, enemy_ac):
  totalDamage = []
  for i in range (0, x):
    totalDamage.append(turnDamage(enemy_ac))
  return totalDamage


for i in range(0,26):
  enemy_ac = i
  d = damageSim(10000, enemy_ac)
  print("Damage at AC " + str(i) + ": " + str(statistics.mean(d)))
