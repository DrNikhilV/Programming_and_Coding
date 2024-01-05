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

    def retrieve_sequence(self, leaf_hash):
        if leaf_hash in self.leaves:
            leaf_index = self.leaves.index(leaf_hash)
            leaf, proof = self._collect_proof(leaf_index)
            return leaf, proof
        else:
            return None, None

    def _collect_proof(self, leaf_index):
        leaf = self.leaves[leaf_index]
        proof = []

        while leaf_index > 0:
            parent_index = (leaf_index - 1) // 2

            if leaf_index % 2 == 0:
                sibling_index = leaf_index - 1
                sibling = self.leaves[sibling_index]
                proof.append(sibling)
            else:
                sibling_index = leaf_index + 1
                sibling = self.leaves[sibling_index]
                proof.append(sibling)

            leaf = self.leaves[parent_index]
            leaf_index = parent_index

        return leaf, proof

    def verify_proof(self, proof, retrieved_leaf, target_hash):
        current_hash = hashlib.sha256(retrieved_leaf.encode()).hexdigest()

        for node in proof:
            if leaf_index % 2 == 0:
                current_hash = hashlib.sha256((current_hash + node).encode()).hexdigest()
            else:
                current_hash = hashlib.sha256((node + current_hash).encode()).hexdigest()

        return current_hash == target_hash


def main():
    # Create a Merkle tree
    merkle_tree = MerkleTree()

    # Read the DNA sequence from the text file and add it to the Merkle tree
    with open("Salivary_Amylase_Sequence.txt", "r") as f:
        dna_sequence = f.read()
        merkle_tree.add_sequence(dna_sequence)

    # Prompt the user to enter a hash key
    target_hash = input("Enter the hash key you want to retrieve (or the root hash key for verification): ")

    if target_hash == merkle_tree.get_root_hash():
        print("Root hash key matches. The entire Merkle tree is verified.")
    else:
        # Retrieve the DNA sequence from the Merkle tree
        retrieved_sequence, proof = merkle_tree.retrieve_sequence(target_hash)

        if retrieved_sequence is not None:
            print("Retrieved DNA sequence:", retrieved_sequence)

            # Verify the proof
            if merkle_tree.verify_proof(proof, retrieved_sequence, target_hash):
                print("The DNA sequence was successfully retrieved from the Merkle tree and verified.")
            else:
                print("The DNA sequence could not be verified.")
        else:
            print("Hash key not found in the Merkle tree.")

if __name__ == "__main__":
    main()