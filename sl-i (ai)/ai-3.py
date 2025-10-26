def alphabeta(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -9999
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  
        return best
    else:
        best = 9999
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break 
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

print("Optimal value:", alphabeta(0, 0, True, values, -9999, 9999, 3))