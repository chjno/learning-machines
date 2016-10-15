import numpy as np

and_weights = None
and_bias = None
or_weights = None
or_bias = None

def ptron(mode, input1, input2, expected=None):
    global and_weights, and_bias
    global or_weights, or_bias

    inputs = np.array([input1, input2])

    if mode == 'and':
        
        if and_weights is None:
            and_weights = np.random.random(2)
            and_bias = np.random.random()

        total = np.dot(inputs, and_weights) + and_bias

        if total > 0:
            output = 1
        else:
            output = -1

    elif mode == 'or':

        if or_weights is None:
            or_weights = np.random.random(2)
            or_bias = np.random.random()

        total = np.dot(inputs, or_weights) + or_bias

        if total >= 0:
            output = 1
        else:
            output = -1

    print 'output: ' + str(output)

    if expected is not None and output != expected:
        print ''
        print 'adjusting and_weights...'
        print ''
        error = expected - output
        learning_constant = 0.01


        if mode == 'and':
            d_and_weights = error * inputs * learning_constant
            d_and_bias = error * learning_constant

            # print 'old and_weights: ' + str(and_weights)
            # print 'old and_bias: ' + str(and_bias)

            and_weights = and_weights + d_and_weights
            and_bias = and_bias + d_and_bias

            # print 'new and_weights: ' + str(and_weights)
            # print 'new and_bias: ' + str(and_bias)

        elif mode == 'or':
            d_or_weights = error * inputs * learning_constant
            d_or_bias = error * learning_constant

            # print 'old or_weights: ' + str(or_weights)
            # print 'old or_bias: ' + str(or_bias)

            or_weights = or_weights + d_or_weights
            or_bias = or_bias + d_or_bias

            # print 'new or_weights: ' + str(or_weights)
            # print 'new or_bias: ' + str(or_bias)
