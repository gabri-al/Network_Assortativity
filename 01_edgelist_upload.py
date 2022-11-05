_path = r'Downloads/facebook_combined.txt'
G_fb = nx.read_edgelist(_path, create_using = nx.Graph(), nodetype=int)
