def findDepth(tree,n,index):
    print(f"Currently at: {tree[index]}")
    if (index >= n or tree[index]=='l'):
        return 0
    index +=1
    
    left = findDepth(tree,n,index)
    index +=1
    right = findDepth(tree,n,index)
    ht = 1 + max(left,right)
    return ht

if __name__=='__main__':
    tree = 'nlnll'
    n = len(tree)
    index = 0
    ht = findDepth(tree,n,index)
    print(ht)