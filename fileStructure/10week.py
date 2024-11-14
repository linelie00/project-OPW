class Node:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self):
        self.root = Node(is_leaf=True)
    
    def insert(self, key):
        root = self.root
        # 루트가 가득 찬 경우, 새로운 루트를 생성하고 트리를 분할
        if len(root.keys) == 3:
            new_root = Node()
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            idx = len(node.keys) - 1
            while idx >= 0 and key < node.keys[idx]:
                idx -= 1
            idx += 1
            if len(node.children[idx].keys) == 3:
                self.split_child(node, idx)
                if key > node.keys[idx]:
                    idx += 1
            self._insert_non_full(node.children[idx], key)

    def split_child(self, parent, idx):
        node = parent.children[idx]
        new_node = Node(is_leaf=node.is_leaf)
        # 중간 값을 부모로 올리고 나머지 분할
        parent.keys.insert(idx, node.keys[1])
        parent.children.insert(idx + 1, new_node)
        new_node.keys = node.keys[2:]  # 오른쪽 절반
        node.keys = node.keys[:1]      # 왼쪽 절반
        # 자식 노드의 경우 자식 포인터도 나눔
        if not node.is_leaf:
            new_node.children = node.children[2:]
            node.children = node.children[:2]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# B+ 트리 생성 및 키 삽입
bptree = BPlusTree()
keys = [15, 69, 110, 90, 20, 120, 40, 125]

for key in keys:
    bptree.insert(key)

# 최종 트리 상태 출력
bptree.print_tree()
