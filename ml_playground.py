from multivariate_normal import MultiVariate

if __name__ == '__main__':
    mv = MultiVariate([[1,4,7],[2,5,8],[3,6,9]])
    print(mv.get_mean_vector())
