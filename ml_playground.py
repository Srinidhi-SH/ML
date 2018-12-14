from supervised_learning import Regressor, isFamilyCar

if __name__ == '__main__':
    print(isFamilyCar(150,14000))
    regressor = Regressor([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]);
    print(regressor.predict_y(10))
    print(regressor.predict_y(11))
    print(regressor.predict_y(12))