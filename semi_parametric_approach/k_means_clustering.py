# We assume that k = 4
from collections import defaultdict

class Clustering:
    def __init__(self, data):
        self.data = data

    def compute_cluster_centers(self):
        self.reference_vectors = [4.5,5,5.5,3.5]
        for epoch in range(50):
            print(epoch)
            labels = self.compute_labels(self.data)
            self.update_component_knowledge(labels)
            print(self.reference_vectors)

    def compute_labels(self, data):
        labels = {}
        for instance in data:
            distances_to_rv = [(instance - rv)**2 for rv in self.reference_vectors]
            nearest_reference_vector = distances_to_rv.index(min(distances_to_rv))
            labels[instance] = nearest_reference_vector
        return labels

    def update_component_knowledge(self, labels):
        grouped_labels = defaultdict(list)
        for key, value in sorted(labels.items()):
            grouped_labels[value].append(key)
        for label,instances in grouped_labels.items():
            self.reference_vectors[label] = sum(instances)/float(len(instances))


