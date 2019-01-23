def triangles():
	L=[1]
	while True:
		yield L
		L = [1]+[L[i] + L [i+1] for i in range(len(L)-1)] + [1]

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

qq=fib(6)
while True:
	try:
		g=next(qq)
		print(g)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# max depth
class solution(self):
	def maxdepth(self,root):
		if root:
			return 1+max(self.maxdepth(root.left),self.maxdepth(root.right))
		else return 0

# preorder:
class solution(self):
	def preorder(self,root):
		result,q=[root]
		while q:
			node=q.pop()
			if node:
				result.append(node.val)
				q.append(node.right)
				q.append(node.left)
		return result


class solutioni(self):
	def preorder(self,root):
		result,q=[root]
		while q:
			node=q.pop()
			if node:
				result.append(node.val)
				q.append(node.left)
				q.append(node.right)
		return result[::-1]

class inord(self):
	def inorder(self,root):
		result,q=[],[]
		while True:
			while root:
				q.append(root)
				root=root.left
			if len(q)==0:
				return result
			node=q.pop()
			res.append(node.value)
			root=node.right

class levelord(self):
	def levelorder(self,root):
		res,level=[],[root]
		while root and level:
			res.append(node.val for node in level)
			lrchild=[(node.left,node.right) for node in level]
			level=[node for lR in lrchild for node in lR if node ]


class sym(self):
	def symmetric(self,root):
		stack=[root.left,root.right]
		while len(stack>0):
			node=stack.pop(0)
			lc=node[0]
			rc=node[1]
			if lc is None and rc is None:
                continue
            if lc is None or rc is None:
                return False

            if lc.val==rc.val:
				stack.insert(0,[lc.left,rc.right])
				stack.insert(0,[lc.right,rc.left])
			else:
				return False
		return True


class path(self):
	def dfs(self,root,tatget,res):
		if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
        if root.left:
        	dfs(root.left,target-root.val,res)
        if root.right:
        	dfs(root.right,target-root.right,res)
    def pathSumL(self):
    	res=[]
    	self.dfs(root,target,res)
    	return any(res)

