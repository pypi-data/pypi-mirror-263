import numpy as np
import pickle
import pymatgen.core as mg

with open('composition_vectorizer/orderings/1d_orderings.pkl','rb') as fid:
    orders_dict = pickle.load(fid)


def pymatgen_comp(comp_input):
    # Check if the input is a string (single composition)
    if isinstance(comp_input, str):
        return [mg.Composition(comp_input)]
    # Check if the input is a list or array
    elif isinstance(comp_input, (list, tuple)):
        return [mg.Composition(x) for x in comp_input]
    else:
        raise TypeError("Input must be a string or a list/tuple of strings.")



def featurizer_1d(comps, order, el_list = []):
        if order not in ['alphabet','periodic','pettifor','m-pettifor']:
           raise ValueError("order must be one of ['alphabet','periodic','pettifor','m-pettifor']")
        
        comps = pymatgen_comp(comps)
        if len(el_list) == 0:
            all_eles = []
            for c in comps:
                all_eles += list(c.get_el_amt_dict().keys())
            eles = np.array(sorted(all_eles,key = lambda x : orders_dict[order].index(x)))
        else:
            eles = np.array(sorted(el_list,key = lambda x : orders_dict[order].index(x)))
          
        
        all_vecs = np.zeros([len(comps), len(eles)])
        for i, c in enumerate(comps):
            for k, v in c.get_el_amt_dict().items(): 
                j = np.argwhere(eles == k)
                all_vecs[i, j] = v

        all_vecs = all_vecs / np.sum(all_vecs, axis=1).reshape(-1, 1)
        all_vecs = np.array(all_vecs, dtype=np.float32)

        return (all_vecs,eles)