# Need on PATH
# og2dot: https://github.com/cmungall/obographviz
# dot: https://graphviz.org
# jq: https://stedolan.github.io/jq/
# curl

UBERGRAPH="https://stars-app.renci.org/ubergraph/sparql"

all: two-hop-neighborhood.pdf

%.result.json: sparql/%.rq
	 curl -X POST --data-binary @$< --header "Content-Type:application/sparql-query" --header "Accept:application/json" $(UBERGRAPH) >$@

%.obograph.json: %.result.json
	jq '.results | {graphs: [{ id: "result", nodes: .bindings | map({id: .s.value, lbl: .slabel.value, type: "CLASS"}, {id: .p.value, lbl: .plabel.value, type: "PROPERTY"}, {id: .o.value, lbl: .olabel.value, type: "CLASS"}) | unique , edges: .bindings | map(. | { sub: .s.value, pred: .p.value, obj: .o.value }) } ]}' $< >$@

%.dot: %.obograph.json style/ubergraph-style.json
	og2dot.js -s style/ubergraph-style.json $< >$@

%.pdf: %.dot
	dot $< -Tpdf -Grankdir=BT >$@
