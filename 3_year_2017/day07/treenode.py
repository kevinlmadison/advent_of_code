class TreeNode:

    def __init__(self, name=None, weight=None, total_weight=None):
        self.name = name
        self.weight = weight
        self.total_weight = total_weight
        self.children = []

    def set_total(self):
        self.total_weight =  self.weight + sum(child.get_total() for child in self.children)

    def get_total(self):
        if not self.total_weight:
            self.set_total()
        return self.total_weight

    def get_weight(self):
        return self.weight
    
    def __repr__(self):
        return "{} : {} : {}".format(self.name, str(self.weight), \
                [repr(x) for x in self.children if len(self.children) > 0])
