import numpy as np


def sigmoid_fn(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_dfn(x):
    y = sigmoid_fn(x)
    return y * (1.0 - y)


def tanh_fn(x):
    return np.sinh(x) / np.cosh(x)


def tanh_dfn(x):
    return 1.0 - np.power(tanh_fn(x), 2.0)


class Mlp:

    def activation_fn(self, x):
        return tanh_fn(x)

    def activation_dfn(self, x):
        return tanh_dfn(x)

    epoch = 0
    report_freq = 1000
    n_epochs = 1e6

    learning_rate = 0.01

    error = None

    weights = []
    biases = []

    def __init__(self, layer_sizes):

        self.layer_sizes = layer_sizes

        self.error = np.zeros((layer_sizes[0], 1))

        for i in range(0, len(self.layer_sizes) - 1):
            self.weights.append(np.random.rand(self.layer_sizes[i + 1], self.layer_sizes[i]))
            self.biases.append(np.random.rand(self.layer_sizes[i + 1], 1))

    def train(self, input_examples, output_examples):

        index = 0

        while self.epoch <= self.n_epochs:

            activations = [None]
            outputs = []
            deltas = []

            if index >= len(input_examples):
                index = 0

            outputs.append(input_examples[index])   # inputs
            output_vec = output_examples[index]

            for i in range(0, len(self.layer_sizes) - 1):
                activations.append(np.dot(self.weights[i], outputs[i]) + self.biases[i])
                outputs.append(self.activation_fn(activations[i + 1]))

            deltas.insert(0, self.activation_dfn(activations[-1]) * (outputs[-1] - output_vec))

            for i in range(len(self.layer_sizes) - 2, 0, -1):
                deltas.insert(0, self.activation_dfn(activations[i]) * np.dot(self.weights[i].T, deltas[0]))

            for i in range(0, len(self.weights)):
                # print self.weights[i]
                print np.expand_dims(outputs[i].T, 1).shape
                self.weights[i] -= self.learning_rate * np.dot(deltas[i], outputs[i].T)
                self.biases[i] -= self.learning_rate * deltas[i]
                # print self.weights[i]

            self.error += np.absolute(output_vec - outputs[-1])

            if self.epoch % self.report_freq == 0:
                print("Epoch: %d\nError: %f" % (self.epoch, np.sum(self.error) / float(self.layer_sizes[0]) / float(self.report_freq)))
                self.error = np.zeros((self.layer_sizes[0], 1))

            self.epoch += 1
            index += 1

    def predict(self, input_example):

        activations = [None]
        outputs = []

        outputs.append(input_example)   # inputs
        # output_vec = output_examples[index]

        for i in range(0, len(self.layer_sizes) - 1):
            activations.append(np.dot(self.weights[i], outputs[i]) + self.biases[i])
            outputs.append(self.activation_fn(activations[i + 1]))

        return outputs[-1]
