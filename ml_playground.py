from parametric_approach import Regressor

if __name__ == '__main__':
    regressor = Regressor([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9])
    print(regressor.predict_y(12))
    print(regressor.predict_y(230))
    print(regressor.predict_y(490))
