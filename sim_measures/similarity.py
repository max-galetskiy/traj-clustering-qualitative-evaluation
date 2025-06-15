import os
import sys

# Build an absolute path from this notebook's parent directory
ext_module_path = os.path.abspath(os.path.join('..', '..', 'external', 'external'))
sys.path.append(ext_module_path)

import traj_dist.distance as tdist
import numpy as np

# returns a distance matrix for a given array of trajectories
#
#   measure = {"discrete_frechet","hausdorff","dtw","lcss","edr","erp","sspd"}
#
#
def distance_matrix(trajectories,measure, edit_distance_eps=-1,erp_refpoint=None):

    if measure in ["discrete_frechet","hausdorff","dtw","sspd"]:

        if measure == "discrete_frechet":
            measure = "discret_frechet"   # couldnt live with the library's convention, I'm sorry

        return tdist.cdist(trajectories, trajectories, metric=measure)
    
    elif measure in ["lcss","edr"]:

        if(edit_distance_eps <= 0):
            raise ValueError("No epsilon-parameter provided for edit-distance based measures")

        return tdist.cdist(trajectories,trajectories,metric=measure,eps=edit_distance_eps)
    
    elif measure == "erp":

        if(erp_refpoint is None):
            raise ValueError("No reference point provided for ERP")
        
        return tdist.cdist(trajectories,trajectories,metric=measure,g=erp_refpoint)
    
    else:
        raise ValueError(f"Unsupported distance measure: {measure}")
    


# transforms a distance matrix to a similarity matrix via a Gaussian kernel
# sim = exp(-d^2 / 2*gamma^2) 
#
# (computation is done rather inefficiently for simplicity's sake)
def dist_to_sim_matrix(distances, edr_used = False, gamma = -1):

    if edr_used:
        return [[1.0 - d for d in row] for row in distances]

    #gamma = 1/dims
    return [[np.exp(-d**2 / (2 * gamma ** 2)) for d in row] for row in distances]

def lcss_to_dist_matrix(similarities):

    return [[1.0 - d for d in row] for row in similarities]