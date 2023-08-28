import numpy as np

# np.argmax는 리스트에서 인덱스를 반환

# define a sequence of 10 words over a vocab of 5 words
data = [[0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1]]
data = np.array(data)

# Greedy decoder
def greedy_decoder(data):
    # index for largest probability each row
    return [np.argmax(s) for s in data]


result_greedy = greedy_decoder(data)
print(result_greedy)
