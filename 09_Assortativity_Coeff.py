# NX computation
print(nx.attribute_assortativity_coefficient(G_fb, 'gender;'))

# Manual computation of the attribute assortativity coeff
tr_ = np.trace(M_)
Msq_ = np.sum(np.matmul(M_, M_))

coeff_ = (tr_-Msq_)/(1-Msq_)
