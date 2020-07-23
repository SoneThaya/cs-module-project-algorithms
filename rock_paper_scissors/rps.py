#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  options = ['rock', 'paper', 'scissors']
  all_possibilities = []
  
  if n == 0:
    return [[]]
  if n == 1:
    return options
  
  def round_choice(round, round_number):
    
    for i in options:
      round.append(options[i])
      if round_number == n:
        all_possibilities.append(round.slice())
      else:
        round_choice(round, round_number +1)
  
  return all_possibilities


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')