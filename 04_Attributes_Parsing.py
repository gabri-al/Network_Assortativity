main_path = r'Downloads/facebook/'
node_feats = {}

filenames_id = ['0','107','348','414','686','698','1684','1912','3437','3980']
for n_ in filenames_id:
    #Import .feat file
    feat_ = np.genfromtxt(main_path+n_+'.feat', delimiter=' ')
    
    #Import .featnames file
    featnames_ = {}
    featnames_file = open(main_path+n_+'.featnames', 'r') # Parse line by line (no delimiters)
    for line in featnames_file:  # example line: '0 birthday;anonymized feature 376' --> split it at first space
        spl = line.split(" ", 1)
        k = spl[0].replace('\'','')
        v = spl[1].replace('\'','').replace('\n','')
        v_ = v.split("anonymized ", 1) # Split the feature into feature name (e.g. birthday) and feature value (e.g. anonymized feature 376)
        v_name = v_[0].replace('\'','')
        v_value = v_[1].replace('\'','')
        v_value = "anonymized "+v_value
        featnames_[k] = [v_name, v_value] # Build a dict of lists where list[0] is attribute key, list[1] is attribute value
    featnames_file.close()

    # Fill in a dict with nodes as key and their features (i.e. feat == 1)
    for r in np.arange(0, feat_.shape[0], 1): # For each node in feat file
        feat_row_ = feat_[r]
        node_ = int(feat_row_[0])
        # Check if node has already some features assigned
        if node_ not in node_feats.keys():
            feat_assigned_ = {}
        else:
            feat_assigned_ = node_feats[node_]
        # Assign features to node_
        for fc in np.arange(1, feat_.shape[1], 1): # For each column in feat file
            if int(feat_row_[fc]) >= 1:
                dic_k = str(fc-1)
                if featnames_[dic_k][0] not in feat_assigned_.keys():
                    feat_assigned_[featnames_[dic_k][0]] = featnames_[dic_k][1]
        node_feats[node_] = feat_assigned_
