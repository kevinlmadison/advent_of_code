from treenode import TreeNode

def part1(lines):
    children = set()
    parents = set()
    for x in lines:
        x = x.split()
        x = [y.strip(',') for y in x]
        parents.update([x[0]])
        if len(x) > 2:
            children.update(x[3:])
    print([p for p in parents if p not in children])

def part2(lines):

    def fill_tree(node_name):
        x = TreeNode(node_name, weights[node_name])
        for i in tree[x.name]:
            x.children.append(fill_tree(i))
        return x

    def check_weights(tree_node):
        curr_weights = set()
        for child in tree_node.children:
            curr_weights.add(child.get_total())

        if len(curr_weights) > 1:
            print(curr_weights)
            for child in tree_node.children:
                print("{} : {} : {}".format(child.name, str(child.get_weight()), str(child.get_total())))

        for child in tree_node.children:
            check_weights(child)

    '''Here we're converting our input to a more usable adjacency list 
       and corresponding weight table.'''

    tree = dict()
    weights = dict()
    for x in lines:
        x = x.split()
        x = [y.strip(',()') for y in x]
        tree[x[0]] = set()
        weights[x[0]] = int(x[1])
        if len(x) > 2:
            tree[x[0]].update(x[3:])

    '''For this section we need to balance the weights of each subtree.
       Our root node for this input was 'eqgvf'.'''

    oop_tree = fill_tree('eqgvf')
    oop_tree.set_total()
    check_weights(oop_tree)

def main():
    f = open('input.txt').readlines()
    print("PART 1: ")
    part1(f)
    f = open('input.txt').readlines()
    print("PART 2: ")
    part2(f)

if __name__ == '__main__':
    main()
