class TreeObj:
    def __init__(self, indx, value = None):
        self.index = indx
        self.value = value
        self.left = self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj

class DecisionTree:
    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj = None, left = True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root: TreeObj, x: list):
        obj = root
        while obj.left or obj.right:
            if x[obj.index]:
                obj = obj.left
            else:
                obj = obj.right
        return obj.value

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, 'Будет программистом'), v_11)
DecisionTree.add_obj(TreeObj(-1, 'Будет кодером'), v_11, False)
DecisionTree.add_obj(TreeObj(-1, 'Не все потеряно'), v_12)
DecisionTree.add_obj(TreeObj(-1, 'Безнадежен'), v_12, False)
x = [0, 0, 1]
res = DecisionTree.predict(root, x)
print(res)
