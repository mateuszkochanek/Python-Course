# Input z samymi jedynkami to tak zwany bias unit. Gdybysmy ich nie mieli to wykres wynikowy musialby przechodzic
# przez punkt 0,0. Dodatkowo model staje się dzięki temu bardziej elastyczny.
#
# Generalnie sieć neuronowa używająca tylko funkcji sigmoid daje wyniki bliskie do prawdziwych.
# Obie modyfikacje relu niestety czasem daja same 0 albo 0,5. Ale np dla np.random.seed(4) i eta 0.01 dostalem w obu
# sieciach dla XORA, używajacych relu output = [[0.][1.][1.][0.]], wiec można wysnuć przypuszczenie, że jest to
# bardziej dokładne. Dla AND przy tych ustawieniach wyniki również były podobne. Natomiast dla OR sieci mające
# relu dawały: [[0.25][0.75][0.75][1.25]].
#
import numpy as np

class NeuralNetwork_sigmoid:

    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(4,self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.5

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1.T))
        self.output = sigmoid(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * sigmoid_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = sigmoid_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2

class NeuralNetwork_relu:

    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(4,self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.01

    def feedforward(self):
        self.layer1 = rectified_laf(np.dot(self.input, self.weights1.T))
        self.output = rectified_laf(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * rectified_laf_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = rectified_laf_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2

class NeuralNetwork_sigmoid_relu:

    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(4,self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = 0.01

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1.T))
        self.output = rectified_laf(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * rectified_laf_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = sigmoid_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2

def sigmoid(x):
    return 1.0/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

def rectified_laf(x):
    return x * (x > 0)

def rectified_laf_derivative(x): # jeśli x<0 to 0 inaczej 1
    return 1. * (x > 0)


def test_XOR():
    X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
    y = np.array([[0],[1],[1],[0]])
    network1 = NeuralNetwork_sigmoid(X,y)
    network2 = NeuralNetwork_relu(X, y)
    network3 = NeuralNetwork_sigmoid_relu(X, y)
    for i in range(5000):
        network1.feedforward()
        network1.backprop()
        network2.feedforward()
        network2.backprop()
        network3.feedforward()
        network3.backprop()
    np.set_printoptions(precision=3, suppress=True)
    print("XOR: Wyniki dla sieci używającej tylko funkcji sigmoid:")
    print(network1.output)
    print("XOR: Wyniki dla sieci używającej tylko funkcji relu:")
    print(network2.output)
    print("XOR: Wyniki dla sieci używającej funkcji sigmoid dla outputu i relu dla wewnętrznej warstwy:")
    print(network2.output)

    def test_XOR():
        X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
        y = np.array([[0], [1], [1], [0]])
        network1 = NeuralNetwork_sigmoid(X, y)
        network2 = NeuralNetwork_relu(X, y)
        network3 = NeuralNetwork_sigmoid_relu(X, y)
        for i in range(5000):
            network1.feedforward()
            network1.backprop()
            network2.feedforward()
            network2.backprop()
            network3.feedforward()
            network3.backprop()
        np.set_printoptions(precision=3, suppress=True)
        print("XOR: Wyniki dla sieci używającej tylko funkcji sigmoid:")
        print(network1.output)
        print("XOR: Wyniki dla sieci używającej tylko funkcji relu:")
        print(network2.output)
        print("XOR: Wyniki dla sieci używającej funkcji sigmoid dla outputu i relu dla wewnętrznej warstwy:")
        print(network2.output)

def test_AND():
    X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
    y = np.array([[0],[0],[0],[1]])
    network1 = NeuralNetwork_sigmoid(X,y)
    network2 = NeuralNetwork_relu(X, y)
    network3 = NeuralNetwork_sigmoid_relu(X, y)
    for i in range(5000):
        network1.feedforward()
        network1.backprop()
        network2.feedforward()
        network2.backprop()
        network3.feedforward()
        network3.backprop()
    np.set_printoptions(precision=3, suppress=True)
    print("AND: Wyniki dla sieci używającej tylko funkcji sigmoid:")
    print(network1.output)
    print("AND: Wyniki dla sieci używającej tylko funkcji relu:")
    print(network2.output)
    print("AND: Wyniki dla sieci używającej funkcji sigmoid dla outputu i relu dla wewnętrznej warstwy:")
    print(network2.output)

def test_OR():
    X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
    y = np.array([[0],[1],[1],[1]])
    network1 = NeuralNetwork_sigmoid(X,y)
    network2 = NeuralNetwork_relu(X, y)
    network3 = NeuralNetwork_sigmoid_relu(X, y)
    for i in range(5000):
        network1.feedforward()
        network1.backprop()
        network2.feedforward()
        network2.backprop()
        network3.feedforward()
        network3.backprop()
    np.set_printoptions(precision=3, suppress=True)
    print("OR: Wyniki dla sieci używającej tylko funkcji sigmoid:")
    print(network1.output)
    print("OR: Wyniki dla sieci używającej tylko funkcji relu:")
    print(network2.output)
    print("OR: Wyniki dla sieci używającej funkcji relu dla outputu i sigmoid dla wewnętrznej warstwy:")
    print(network2.output)



#np.random.seed(4)
test_XOR()
test_AND()
test_OR()