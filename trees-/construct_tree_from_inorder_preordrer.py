from treeutils import *
#construction of the tree from preorder and inorder traversal
#done two methods using 1...slicing the given pre and in order list
#2...passing indexs also to the functions that index may be boundary index
def constructtree(inorder,preorder):   #using slicing of the
    if inorder:
        root=TreeNode(preorder[0])
        x=inorder.index(preorder[0])
        root.left=constructtree(inorder[0:x],preorder[1:x+1])
        root.right=constructtree(inorder[x+1:],preorder[x+1:])
        return root
def inordertraversal(root):
    if root:
        inordertraversal(root.left)
        print root.value,
        inordertraversal(root.right)

def preordertraversal(root):
    if root:
        print root.value,
        preordertraversal(root.left)
        preordertraversal(root.right)
def construct_tree_using_indexing(inorder,i1,i2,preorder,p1,p2) :#where p1,p2 are preorder boundary  # indexs and i1,i2 are inorderindexs
    if i1<=i2:
        root=TreeNode(preorder[p1])
        ind=inorder.index(preorder[p1])
        root.left = construct_tree_using_indexing(inorder,i1,ind-1,preorder,p1+1,p1+(ind-i1))
        root.right=construct_tree_using_indexing(inorder,ind+1,i2,preorder,p1+(ind-i1)+1,p2)
        return root


def main():
    preorder=[10,20,30,40,50,60,70]
    inorder=[20,40,30,50,10,60,70]
    root=construct_tree_using_indexing(inorder,0,6,preorder,0,6)

    preordertraversal(root)
    print '\n'
    inordertraversal(root)

if __name__ =='__main__':
    main()