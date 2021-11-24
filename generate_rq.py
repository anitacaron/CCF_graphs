import argparse, json

level_2 = """
  UNION
  {{
    SELECT DISTINCT ?s
    WHERE {{
      GRAPH <http://reasoner.renci.org/nonredundant> {{
        ?s ?p1 ?o1 .
        ?o1 ?p2 node: .
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p1_p {{ {properties} rdfs:subClassOf }}
              ?p1 rdfs:subPropertyOf* ?p1_p .
            }}
        }}
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p2_p {{ {properties} rdfs:subClassOf }}
              ?p2 rdfs:subPropertyOf* ?p2_p .
            }}
        }}
      }}
    }}
  }}
"""

level_3 = """
  UNION
  {{
    SELECT DISTINCT ?s
    WHERE {{
      GRAPH <http://reasoner.renci.org/nonredundant> {{
        ?s ?p1 ?o1 .
        ?o1 ?p2 ?o2 .
        ?o2 ?p3 node: .
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p1_p {{ {properties} rdfs:subClassOf }}
              ?p1 rdfs:subPropertyOf* ?p1_p .
            }}
        }}
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p2_p {{ {properties} rdfs:subClassOf }}
              ?p2 rdfs:subPropertyOf* ?p2_p .
            }}
        }}
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p3_p {{ {properties} rdfs:subClassOf }}
              ?p3 rdfs:subPropertyOf* ?p3_p .
            }}
        }}
      }}
    }}
  }}
"""

level_4 = """
  UNION
  {{
    SELECT DISTINCT ?s
    WHERE {{
      GRAPH <http://reasoner.renci.org/nonredundant> {{
        ?s ?p1 ?o1 .
        ?o1 ?p2 ?o2 .
        ?o2 ?p3 ?o3 .
        ?o3 ?p4 node: .
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p1_p {{ {properties} rdfs:subClassOf }}
              ?p1 rdfs:subPropertyOf* ?p1_p .
            }}
        }}
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p2_p {{ {properties} rdfs:subClassOf }}
              ?p2 rdfs:subPropertyOf* ?p2_p .
            }}
        }}
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p3_p {{ {properties} rdfs:subClassOf }}
              ?p3 rdfs:subPropertyOf* ?p3_p .
            }}
        }}
        FILTER EXISTS {{
          GRAPH <http://reasoner.renci.org/ontology> {{
              VALUES ?p4_p {{ {properties} rdfs:subClassOf }}
              ?p1 rdfs:subPropertyOf* ?p4_p .
            }}
        }}
      }}
    }}
  }}
"""

parser = argparse.ArgumentParser()
parser.add_argument('variables', help='set up variables to build the graph')
# parser.add_argument('properties', help='properties to search link')
parser.add_argument('output_file', help='output file path')

args = parser.parse_args()
variables = json.loads(args.variables)

if variables["depth"] == 2:
  variables["depths"] = level_2.format(**variables)
elif variables["depth"] == 3:
  variables["depths"] = (level_2 + level_3).format(**variables)
elif variables["depth"] == 4:
  variables["depths"] = (level_2 + level_3 + level_4).format(**variables)
else:
  variables["depths"] = ""

with open('sparql/base.rq') as f:
  query = f.read().format(**variables)

with open(f'{args.output_file}', 'w') as f:
  f.write(query)