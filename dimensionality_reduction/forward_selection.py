# We are using nearest mean classifier
# We have 3 classes and four attributes

class ForwardSelection:
    def __init__(self, accuracies):
        self.accuracies = accuracies

    def find_best_subset(self):
        subset_of_attributes = ""
        subset_found = False
        while(not subset_found):
            subset_found = True
        return subset_of_attributes