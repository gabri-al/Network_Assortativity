# Build a list of all possible attribute names
attrs_ = []
for n in node_feats.keys(): # Nodes id
    for attr in node_feats[n].keys():
        if attr not in attrs_:
            attrs_.append(attr)

# Measure coefficients for all attributes
assort_coeff = {}

for attr in attrs_:
    coeff_ = nx.attribute_assortativity_coefficient(G_fb, attr)
    assort_coeff[attr] = coeff_

display(dict(sorted(assort_coeff.items(), key=lambda item: item[1], reverse=True)))
