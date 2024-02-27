import argparse

p=argparse.ArgumentParser(description='Adder')

p.add_argument('n1', type=float, help='First number')
p.add_argument('n2', type=float, help='Second number')
p.add_argument('--scale', type=int, default=1, help='Scale result by an integer')

args=p.parse_args()

print((args.n1+args.n2)*args.scale)