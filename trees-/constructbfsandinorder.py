from treeutils import *
def constructtree(inorder,bfs):
    if inorder and bfs:
        ind=None
        for i in range(len(bfs)):
            try:
                ind=inorder.index(bfs[i])
                break
            except ValueError:
                pass
                #Nonthing to be done

        root=TreeNode(bfs[i])
        root.left=constructtree(inorder[:ind],bfs[i+1:])
        root.right=constructtree(inorder[ind+1:],bfs[i+1:])
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

def main():
    inorder=[2,1,3,4]
    bfs=[1,2,3,4]
    root=constructtree(inorder,bfs)
    print "_______inorder________\n"
    inordertraversal(root)
    print '\n'
    print '___________preorder___________\n'
    preordertraversal(root)

if __name__=='__main__':
    main()