import argparse
import numpy as np

p=argparse.ArgumentParser(description='Array')

p.add_argument('input', type=str, help='Input filepath')
p.add_argument('output', type=str, help='Output filepath')
p.add_argument('--transformation', type=str, default='std', help='Type of array transformation to apply')
# p.add_argument('transformation', choices=['norm', 'std'], help='Type of array transformation to apply')

args=p.parse_args()


# Load the input and normalize it
input_array = np.load(args.input)

if args.transformation=='std':
    print('Standardizing...')
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)
elif args.transformation=='norm':
    print('Normalizing...')
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)
else :
    raise

# Save the normalized array
np.save(args.output, output_array)