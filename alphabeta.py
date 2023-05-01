MAX, MIN = 1000, -1000
 
# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
  
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = MIN
 
        # Recur for left and right children
        for i in range(0, 2):
             
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            print("depth",depth)
            print("alpha",alpha)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = MAX
 
        # Recur for left and
        # right children
        for i in range(0, 2):
          
            val = minimax(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            print("depth",depth)
            print("beta",beta)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
      
# Driver Code
if __name__ == "__main__":
  
    values = [2, 3, 5, 9, 0, 1, 7, 5] 
    print("The optimal value is :", minimax(0, 0, True, values,MIN,MAX))

    
    #2nd code--------------------------------------------------------------------------------------
    MAX, MIN = 1000, -1000
dict = {'00':'A','10':'B','20':'D','21':'E','11':'C','22':'F','23':'G'} 
def minimax(depth, nodeIndex, maximizingPlayer,values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha,beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        print("Alpha value at ", dict.get(str(depth) + str(nodeIndex)),": ", alpha)
        return best

    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha,beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        print("Beta value at ", dict.get(str(depth) + str(nodeIndex)),": ",beta)
        return best
       

if __name__ == "__main__":
    values = [2, 3, 5, 9, 0, 1, 7, 5]
    print("The optimal value is :", minimax(0, 0, True, values,MIN,MAX))

