import argparse
import os

parser = argparse.ArgumentParser(description='Работаем c опциями')
parser.add_argument('-N', type=int, action='store')
parser.add_argument('-S', type=str, action='store')
args = parser.parse_args()
print(args.N)
count = 0
while count < args.N:
    print(args.S)
    count += 1