# There are 3 types of cars and we have access to people income information
import math


def _get_class_priors(labels):
    total_instances = float(len(labels))
    p_class_1 = labels.count(1) / total_instances
    p_class_2 = labels.count(2) / total_instances
    p_class_3 = labels.count(3) / total_instances
    return [p_class_1, p_class_2, p_class_3]


def _get_sufficient_statistics(income_data, labels):
    class_1_instances = []
    class_2_instances = []
    class_3_instances = []
    for income, label in zip(income_data, labels):
        if (label == 1):
            class_1_instances.append(income)
        elif (label == 2):
            class_2_instances.append(income)
        elif (label == 3):
            class_3_instances.append(income)
    mean1 = sum(class_1_instances) / float(len(class_1_instances))
    x1_sub_mean1 = [(x1 - mean1) ** 2 for x1 in class_1_instances]
    variance1 = sum(x1_sub_mean1) / float(len(class_1_instances))

    mean2 = sum(class_2_instances) / float(len(class_2_instances))
    x2_sub_mean2 = [(x2 - mean2) ** 2 for x2 in class_2_instances]
    variance2 = sum(x2_sub_mean2) / float(len(class_2_instances))

    mean3 = sum(class_3_instances) / float(len(class_3_instances))
    x3_sub_mean3 = [(x3 - mean3) ** 2 for x3 in class_3_instances]
    variance3 = sum(x3_sub_mean3) / float(len(class_1_instances))

    return [[mean1, variance1], [mean2, variance2], [mean3, variance3]]


class Classifier:
    def __init__(self, income_data, labels):
        self.class_priors = _get_class_priors(labels)
        self.distribution_statistics = _get_sufficient_statistics(income_data, labels)

    def predict_class(self, income):
        g_x = []
        for i in range(3):
            g_x.append(self.class_likelihood(income, i) * self.class_priors[i])
        return g_x.index(max(g_x)) + 1

    def class_likelihood(self, income, class_label):
        class_distribution_info = self.distribution_statistics[class_label]
        variance = class_distribution_info[1]
        mean = class_distribution_info[0]
        sd = math.sqrt(variance)
        return math.exp(-(((income - mean) ** 2)/ (2 * variance)))/(math.sqrt(2 * math.pi) * sd)
