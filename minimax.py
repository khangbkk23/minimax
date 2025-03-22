import math

def minimax(currentDepth, nodeIndex, maxTurn, score, targetDepth):
    if (currentDepth == targetDepth):
        return score[nodeIndex]

    # Check maximizer case
    if (maxTurn):
        return max(minimax(currentDepth + 1, nodeIndex * 2, False, score, targetDepth), 
                   minimax(currentDepth + 1, nodeIndex * 2 + 1, False, score, targetDepth))

    # Check minimizer case
    else:
        return min(minimax(currentDepth + 1, nodeIndex * 2, True, score, targetDepth),
                   minimax(currentDepth + 1, nodeIndex * 2 + 1, True, score, targetDepth))

# Sample usage
score = [3, 5, 2, 9, 12, 5, 23, 23]
depth = int(math.log(len(score), 2))  # Ensure depth is an integer
print("The optimal value is:", end=" ")
print(minimax(0, 0, True, score, depth))
