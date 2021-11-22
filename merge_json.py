import json, argparse

parser = argparse.ArgumentParser()
parser.add_argument('obograph', help='obograph json file path')
parser.add_argument('subset', help='subset file path')
parser.add_argument('output_file', help='output file path')

args = parser.parse_args()

obograph = json.load(open(args.obograph))
subset = json.load(open(args.subset))

nodes = subset["graphs"][0]["nodes"]
for node_obo in obograph["graphs"][0]["nodes"]:
  if node_obo["type"] == "CLASS":
    for node_s in nodes:
      if node_obo["id"] == node_s["id"]:
        node_obo["meta"] = node_s["meta"]

with open(args.output_file, 'w', encoding='utf-8') as f:
  json.dump(obograph, f, ensure_ascii=False, indent=2)
