from semi_parametric_approach import Clustering

if __name__ == '__main__':
    clustering = Clustering([1.2,1.3,1.4,1.5,3.5,3.6,3.7,3.8,3.9,7.5,7.6,7.7,7.8,10.11,10.12,10.13,10.14])
    clustering.compute_cluster_centers()


