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
        # return tanh_fn(x)
        return sigmoid_fn(x)

    def activation_dfn(self, x):
        # return tanh_dfn(x)
        return sigmoid_dfn(x)

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

            outputs.append(np.expand_dims(input_examples[index], 1))   # inputs
            output_vec = np.expand_dims(output_examples[index], 1)

            print 'outputs[0].shape == ' + str(outputs[0].shape)

            for i in range(0, len(self.layer_sizes) - 1):

                print 'weights[' + str(i) + '] == ' + str(self.weights[i].shape)
                print 'np.dot(weights[' + str(i) + '], outputs[' + str(i) + ']) == ' + str(np.dot(self.weights[i], outputs[i]).shape)
                print 'biases[' + str(i) + '] == ' + str(self.biases[0].shape)
                print 'dot + biases[' + str(i) + '] == ' + str((np.dot(self.weights[i], outputs[i]) + self.biases[i]).shape)

                activations.append(np.dot(self.weights[i], outputs[i]) + self.biases[i])
                outputs.append(self.activation_fn(activations[i + 1]))

                print 'activations[' + str(i + 1) + '].shape == ' + str(activations[i + 1].shape)
                print 'outputs[' + str(i + 1) + '].shape == ' + str(outputs[i + 1].shape)

            deltas.insert(0, self.activation_dfn(activations[-1]) * (outputs[-1] - output_vec))

            print 'deltas[1].shape == ' + str(deltas[0].shape)

            for i in range(len(self.layer_sizes) - 2, 0, -1):
                deltas.insert(0, self.activation_dfn(activations[i]) * np.dot(self.weights[i].T, deltas[0]))

                print 'deltas[0].shape == ' + str(deltas[0].shape)

            for i in range(0, len(self.weights)):
                self.weights[i] -= self.learning_rate * np.dot(deltas[i], outputs[i].T)
                self.biases[i] -= self.learning_rate * deltas[i]

            print 'output_vec.shape == ' + str(output_vec.shape)
            print 'outputs[-1].shape == ' + str(outputs[-1].shape)
            print 'outputs[-1] == ' + str(outputs[-1])

            self.error += np.absolute(output_vec - outputs[-1])

            print str(output_vec) + ' ' + str(outputs[-1])

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
