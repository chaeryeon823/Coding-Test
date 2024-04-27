# 카드게임
# S3

import sys

def all_different_num(num):
  return len(set(num)) == len(num)

def continuous_num(num):
  for i in range(5):
    if num.find(num[i] - 1) > -1 or num.find(num[i] + 1) > -1:
      return False
    return True

def same_color(col):
  return len(set(col)) == 1

color = []
number = []

for i in range(5):
  tmp = sys.stdin.readline().split()
  color.append(tmp[0])
  number.append(int(tmp[1]))

  if all_different_num(number):
    if 
