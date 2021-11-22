import argparse, json

parser = argparse.ArgumentParser()
parser.add_argument('variables', help='set up variable to build the graph')
# parser.add_argument('properties', help='properties to search link')
parser.add_argument('output_file', help='output file path')

args = parser.parse_args()
args.variables
variables = json.loads(args.variables)

with open('sparql/base.rq') as f:
  query = f.read().format(**variables)

with open(f'{args.output_file}', 'w') as f:
  f.write(query)