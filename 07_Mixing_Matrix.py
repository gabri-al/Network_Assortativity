#print(nx.attribute_mixing_dict(G_fb, 'gender;')) # Display all possible attribute values
mapping_ = {'anonymized feature 77' : 0,
            'anonymized feature 78' : 1,
            None : 2}
M_ = nx.attribute_mixing_matrix(G_fb, 'gender;', mapping = mapping_, normalized = True)
