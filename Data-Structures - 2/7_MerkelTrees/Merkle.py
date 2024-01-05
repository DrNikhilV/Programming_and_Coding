import hashlib

def build_merkle_tree(leaves):
    if len(leaves) == 0:
        return None
    if len(leaves) == 1:
        return leaves[0]

    new_leaves = []

    for i in range(0, len(leaves), 2):
        data = leaves[i]
        if i + 1 < len(leaves):
            data += leaves[i + 1]
        new_leaves.append(hash_data(data))

    return build_merkle_tree(new_leaves)

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

if __name__ == "__main__":
    data = ["A", "B", "C", "D"]
    merkle_root = build_merkle_tree(data)
    print("Merkle Root:", merkle_root)