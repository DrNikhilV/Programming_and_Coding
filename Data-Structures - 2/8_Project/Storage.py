import hashlib

class MerkleTree:
    def __init__(self):
        self.leaves = []
        self.nodes = []
        self.root = None

    def add_sequence(self, dna_sequence):
        leaf = hashlib.sha256(dna_sequence.encode()).hexdigest()
        self.leaves.append(leaf)
        self._update_tree()

    def _update_tree(self):
        while len(self.leaves) > 1:
            parent_nodes = []

            for i in range(0, len(self.leaves), 2):
                left_child = self.leaves[i]
                right_child = self.leaves[i + 1] if i + 1 < len(self.leaves) else None

                parent_hash = hashlib.sha256((left_child + right_child).encode()).hexdigest()

                parent_nodes.append(parent_hash)

            self.leaves = parent_nodes

        self.root = self.leaves[0]

    def get_root_hash(self):
        return self.root

    def get_hash_keys(self):
        return self.leaves

def main():
    # Read the DNA sequence from the text file
    with open("Salivary_Amylase_Sequence.txt", "r") as f:
        dna_sequence = f.read()

    # Create a Merkle tree
    merkle_tree = MerkleTree()

    # Store the DNA sequence in the Merkle tree
    merkle_tree.add_sequence(dna_sequence)

    # Get the root hash of the Merkle tree
    root_hash = merkle_tree.get_root_hash()

    # Get the hash keys stored in the Merkle tree
    hash_keys = merkle_tree.get_hash_keys()

    print("DNA sequence stored in the Merkle tree.")
    print("Root Hash:", root_hash)
    print("Hash Keys:")
    for hash_key in hash_keys:
        print(hash_key)

if __name__ == "__main__":
    main()
