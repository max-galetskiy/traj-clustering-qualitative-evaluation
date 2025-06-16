# A Qualitative Evaluation of Distance Measures in Trajectory Data Clustering
This GitHub project comprises the entire source code for the paper "A Qualitative Evaluation of Distance Measures in Trajectory Data Clustering" by Max Galetskiy, Johann Bornholdt, Theodoros Chondrogiannis and Michael Grossniklaus.

# Setup
The entire source code is written in Python (either in `.py` files or within Jupyter Notebooks). In the following, we give instructions to recreate our experimental results. 

## What's included?
Additionally to the source code itself, this repository contains the following data:
- Parameters/metadata for the five datasets used in the paper (`data/datasets/metadata.csv`)
- Computed cluster labels for all of these datasets (`data/clustering_data/`)
- Computed evaluation metrics for these datasets including ground-truth based scores, correlation scores, the hopkins statistic and the runtimes (`data/score_data/`)

## Dependencies
The code depends on the following other projects:
- [Traj-Dist](https://github.com/bguillouet/traj-dist) (Note that some minor adjustments to this code are needed to update it to newer Python/Cython versions. The Git Issues should provide enough information on those adjustments)
- [K-Medoids](https://pypi.org/project/kmedoids/)

Refer to the provided links for installation instructions. Furthermore, the code largely depends on standard data science libraries such as:
- [scikit-learn](https://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)

## Datasets
For storage and legal purposes, we do not include the original datasets in this project. However, a small sample file (`data/datasets/sample.csv`) gives insight into the expected format: Trajectories should be given as a csv file (with a "`;`" seperator!) with one trajectory per line. Trajectories are expected to be formatted as a nested list containing either 2-dimensional or 3-dimensional points. The trajectory column is expected to be called "`trajectory`". Furthermore, a column with ground-truth labels is also required to be given, but its name is arbitrary. Other columns may be included, but will not be used in the source code.

We used the following five datasets (all of which can easily be transformed into the wanted format via pandas):
- [Australian Sign Language (ASL)](https://archive.ics.uci.edu/dataset/115/australian+sign+language+signs+high+quality)
- [CROSS](https://figshare.com/articles/dataset/CVRR_dataset_for_trajectory_clustering/25826839?file=46339321)
- [Labomni](https://figshare.com/articles/dataset/CVRR_dataset_for_trajectory_clustering/25826839?file=46339321)
- [Fish Trajectories (FT)](https://homepages.inf.ed.ac.uk/rbf/Fish4Knowledge/GROUNDTRUTH/BEHAVIOR/)
- [DigiLeTs](https://github.com/CognitiveModeling/DigiLeTs)

If you wish to use these datasets in your work, please refer to the citation guidelines provided by these datasets.

## Distance Matrices
Our clustering code excepts distance matrices to already be precomputed and stored in `.json` files (located in `data/similarities/`). To compute these distance matrices yourself, follow these steps:
1. Put the transformed `.csv` files of the datasets into `data/datasets/`
2. Comment out line 26 in `experiments/sim_matrix_computation.py` (Or adjust `data/datasets/metadata.csv` to your liking)
3. Run `experiments/sim_matrix_computation.py`

# Project Structure
The project is partitioned into the following directories:
- `clustering` contains the source code to compute cluster labels given a distance matrix and the according parameters
- `data` contains datasets, clustering labels (`clustering_data`), evaluation metrics (`score_data`) and distance matrices (`similarities`). Additionally, a jupyter notebook with code to visualize the datasets (`visualization.ipynb`) is included as well
- `experiments` contains the code to generate cluster labels and evaluation scores (`experiments.ipynb`), code to visualize experimental results (`figures.ipynb`) and the aforementioned distance matrix computation code (`sim_matrix_computation.py`)
- `sim_measures` contains the source code to compute trajectory distances
