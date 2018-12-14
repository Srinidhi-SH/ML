# Here there are 3 classes C1, C2 and C3
# We calculate the posterior and the discriminant is based on the posterior

def _class_likelihood(x, class_label):
    # class likelihood is gaussian and is not considered here
    return x * class_label

def predict_class(x):
    class_priors = [0.4,0.3,0.3]
    g_x = []
    for i in range(3):
        prob_x_given_c = _class_likelihood(x, i+1)
        g_x.append(prob_x_given_c * class_priors[i])
    return g_x.index(max(g_x))

