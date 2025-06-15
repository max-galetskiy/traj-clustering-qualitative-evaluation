import os
import sys
import json

# Build an absolute path from this notebook's parent directory
sim_module_path = os.path.abspath(os.path.join('..', 'sim_measures'))
cl_module_path  = os.path.abspath(os.path.join('..', 'clustering'))
oth_module_path  = os.path.abspath(os.path.join('..', '..', 'external'))
sys.path.append(sim_module_path)
sys.path.append(cl_module_path)
sys.path.append(oth_module_path)

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

import similarity
import clustering
import kmedoids


datasets = pd.read_csv("../data/datasets/metadata.csv",sep=";")

# Comment this out if you have all the datasets contained in the metadata.csv
datasets = datasets[datasets["dataset"] == "Sample"]

for _,d in datasets.iterrows():

    print(d["dataset"])
    
    traj_col = "trajectory"
    
    df = pd.read_csv("../data/datasets/" + d["file"],sep=";")
    trajectories = df[traj_col].apply(lambda x: np.array(json.loads(x)))

    for measure in ["hausdorff","dtw","edr","erp","sspd","discrete_frechet"]:

        if os.path.isfile("../data/similarities/" + d["file"][:-4] + "_" + measure + ".json"):
            continue


        print(measure)

        if measure == "lcss":
            eps = d["lcss_eps"]
        else:
            eps = d["edr_eps"]

        sims = similarity.distance_matrix(trajectories,measure,eps,np.array(json.loads(d["erp"]),np.float64))

        with open("../data/similarities/" + d["file"][:-4] + "_" + measure + ".json",'w') as f:
            json.dump(sims.tolist(),f)