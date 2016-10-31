tr, va, te = mnist.load()

import mlp_chino
reload(mlp_chino)
mlp = mlp_chino.Mlp([784,1000,10])
mlp.train(tr[0], tr[1])



outputs[0].shape == (784,)
outputs[1].shape == (1000, 1)
outputs[2].shape == (1, 1)

activations[1].shape == (1000, 1)
activations[2].shape == (1, 1)

deltas[0].shape == (1000, 1)
deltas[1].shape == (1, 1)

mlp.weights[0].shape == (1000, 784)
mlp.weights[1].shape == (1, 1000)

mlp.biases[0].shape == (1000, 1)
mlp.biases[1].shape == (1, 1)
