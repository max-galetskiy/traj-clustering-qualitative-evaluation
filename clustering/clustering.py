
import similarity

import sklearn.cluster
import kmedoids

# Generic cluster method
#
# trajectories = np.array with points (represented as lists)
# distances    = distance matrix of the supplied trajectories
#
# method = {"k_medoids","dbscan","hdbscan","spectral","agglomorative"} (used clustering algorithm)
#
def cluster(trajectories,distances,method,nr_clusters=-1,dbscan_eps=-1, aggl_eps=-1,spectral_gamma=-1,lcss_used=False):

   if method == "k_medoids":

      if nr_clusters <= 0:
          raise ValueError("No K supplied for K-Medoids clustering")  

      if lcss_used:
         distances = similarity.lcss_to_dist_matrix(distances)

      return kmedoids.KMedoids(nr_clusters,method='fasterpam',random_state=0).fit_predict(distances)

   elif method == "dbscan":
       
      if dbscan_eps <= 0:
         raise ValueError("No epsilon/minpnts supplied for DBSCAN clustering.")
       
      if lcss_used:
         distances = similarity.lcss_to_dist_matrix(distances)

      min_pnts = 2 * len(trajectories[0][0]) + 1
      return sklearn.cluster.DBSCAN(eps=dbscan_eps,min_samples=min_pnts,metric="precomputed").fit_predict(distances)

   elif method == "hdbscan":

      if lcss_used:
         distances = similarity.lcss_to_dist_matrix(distances)

      return sklearn.cluster.HDBSCAN(metric="precomputed").fit_predict(distances)


   elif method == "spectral_knn":

      if nr_clusters <= 0:
         raise ValueError("Number of clusters not supplied to spectral clustering")
      
      return sklearn.cluster.SpectralClustering(n_clusters=nr_clusters,affinity="precomputed_nearest_neighbors",random_state=0).fit_predict(distances)


   elif method == "agglomorative":
      if nr_clusters <= 0 and aggl_eps <= 0:
         raise ValueError("Number of clusters/Eps not supplied to agglomorative clustering")

      if lcss_used:
         distances = similarity.lcss_to_dist_matrix(distances)

      if nr_clusters > 0:
         return sklearn.cluster.AgglomerativeClustering(n_clusters=nr_clusters,metric="precomputed",linkage='complete').fit_predict(distances)

      return sklearn.cluster.AgglomerativeClustering(n_clusters=None,distance_threshold=aggl_eps, metric="precomputed",linkage='complete').fit_predict(distances)

   else:
      raise ValueError(f"Unsupported clustering method: {method}")