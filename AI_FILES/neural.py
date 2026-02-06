import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# --------------------
# Input Layer
# --------------------
inputs = [0.6, 0.9]
print("Input Layer:", inputs)

# --------------------
# Hidden Layer
# --------------------
weights_hidden = [
    
    [0.2, 0.4],   # weights for hidden neuron 1
    [0.7, 0.3]    # weights for hidden neuron 2
]

bias_hidden = [0.1, 0.1]
hidden_outputs = []

for i in range(2):
    weighted_sum = (
        inputs[0] * weights_hidden[i][0] +
        inputs[1] * weights_hidden[i][1] +
        bias_hidden[i]
    )
    activated_output = sigmoid(weighted_sum)
    hidden_outputs.append(activated_output)

print("Hidden Layer Output:", hidden_outputs)

# --------------------
# Output Layer
# --------------------
weights_output = [0.6, 0.9]
bias_output = 0.2

output_sum = (
    hidden_outputs[0] * weights_output[0] +
    hidden_outputs[1] * weights_output[1] +
    bias_output
)

final_output = sigmoid(output_sum)

print("Final Output:", final_output)
