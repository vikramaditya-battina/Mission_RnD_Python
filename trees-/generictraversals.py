from treeutils import *
class Count(object):
    count=0
    def __init__(self):
        Count.count+=1

def inorder(root,visit):
    if root==None:
        return
    else:
        visit(root)
        inorder(root.left,visit)
        inorder(root.right,visit)

def postorder(root,visit):
    if root==None:
        return
    else:
        postorder(root.left,visit)
        postorder(root.right,visit)
        visit(root)


def preorder(root,visit):
    if root==None:
        return
    else:

        preorder(root.left,visit)
        preorder(root.right,visit)

def visit(root):
    return 1

if __name__=='__main__':
    print 'vikram'
    root=create_tree((1,(5,(2,7,8),6),3))
    inorder(root,visit)

