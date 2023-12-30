
def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
        
    n= len(balls)

    print(n)
    bptr =n-1
    
    # loop for bptr
    for i in range(n-1,-1,-1):
         #print(f"i {i} balls{balls[i]}")
         if balls[i] == 'B':
             balls[bptr], balls[i] = balls[i], balls[bptr]
             bptr -= 1
    
    
    rptr = 0
    for i in range(0, bptr+1):
        if balls[i] == 'R':
            balls[rptr], balls[i] = balls[i], balls[rptr]
            rptr += 1
    
    return balls
          