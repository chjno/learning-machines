import numpy as np

input_vecs = []
output_vecs = []

for i in range(300):
    dog = np.random.uniform( 0.0, np.pi * 2.0, ( 1, 1 ) )
    input_vecs.append(dog)
    output_vecs.append(np.sin(dog))

import mlp_chino
mlp = mlp_chino.Mlp([1,5,1])
mlp.train(input_vecs, output_vecs)




dog = np.random.uniform( 0.0, np.pi * 2.0, ( 1, 1 ) )
mlp.predict(dog)
np.sin(dog)






import numpy as np

input_vecs = []
output_vecs = []

for i in range(300):
    dog = np.random.uniform( 0.0, np.pi * 2.0)
    cat = np.random.uniform( 0.0, np.pi * 2.0)
    input_vecs.append(np.array([dog, cat]))
    output_vecs.append(np.array([np.sin(dog), np.cos(cat)]))

import mlp_chino
mlp = mlp_chino.Mlp([2,5,2])
mlp.train(input_vecs, output_vecs)