def top_n(items, n):
    '''Return top n items from an array in descending order.
    Args:
        items(array): list of array like object
        n (int): number of object to return in an array like object

    Return:
        Array (top n items in discending order)
    
    Eg:
    top_n((9,2,4,2,3), 3)
    Returns:
       (3, 4, 9)
    '''

    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!
                
    # Get last two items
    top_n = items[-n:]
    
    # Return in descending order
    return top_n[::-1]