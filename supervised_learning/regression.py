# We assume a linear model y = w.x + w0
# When we take derivative of MSE loss wrt w and w0, we get equations w.r.t w and w0
# Testing it over a small data set

class Regressor:
    def __init__(self, x, r):
        N = len(x)
        x_avg = sum(x)/float(N)
        r_avg = sum(r)/float(N)
        sum_x_square = sum([xt ** 2 for xt in x])
        sum_r_mul_x = sum([xt*rt for xt,rt in zip(x,r)])

        self.w = (sum_r_mul_x - (x_avg * r_avg * N))/(sum_x_square - (N * (x_avg ** 2)))
        self.w0 = r_avg - (self.w * x_avg)

    def predict_y(self, x):
        y = self.w * x + self.w0
        return y
