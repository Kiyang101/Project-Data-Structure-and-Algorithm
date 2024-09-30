class BST {
  #tree;
  #current;
  #left;
  #right;

  constructor(tree) {
    this.tree = tree;
  }

  setTree(tree) {
    this.tree = tree;
  }

  #goLeft() {
    this.current = this.left;
    this.left = this.current * 2 + 1;
    this.right = this.left + 1;
  }

  #goRight() {
    this.current = this.right;
    this.left = this.current * 2 + 1;
    this.right = this.left + 1;
  }

  findValue(target) {
    if (!target) {
      return false;
    }

    this.current = 0;
    this.left = 1;
    this.right = 2;

    console.log("current = ", this.tree[this.current]);
    console.log("left = ", this.tree[this.left]);
    console.log("right = ", this.tree[this.right]);
    console.log("\n");

    try {
      while (this.tree[this.current]) {
        if (target.toLowerCase() === this.tree[this.current].toLowerCase()) {
          console.log("found: ", this.tree[this.current]);
          return true;
        }
        if (target.toLowerCase() < this.tree[this.current].toLowerCase()) {
          this.#goLeft();
        } else {
          this.#goRight();
        }
        console.log("current = ", this.tree[this.current]);
        console.log("left = ", this.tree[this.left]);
        console.log("right = ", this.tree[this.right]);
        console.log("\n");
      }
    } catch {
      return false;
    }
  }

  findMin() {
    this.current = 0;
    this.left = 1;
    try {
      while (this.tree[this.current]) {
        if (!this.tree[this.left]) {
          return this.tree[this.current];
        } else {
          this.#goLeft();
        }
      }
    } catch {
      return false;
    }
  }

  findMax() {
    this.current = 0;
    this.right = 2;
    try {
      while (this.tree[this.current]) {
        if (!this.tree[this.right]) {
          return this.tree[this.current];
        } else {
          this.#goRight();
        }
      }
    } catch {
      return false;
    }
  }
}

const t5 = [
  "Harmony",
  "Dream",
  "Peace",
  "Butterfly",
  "Energy",
  "Journey",
  "Rainbow",
  "Apple",
  "Courage",
  null,
  "Garden",
  null,
  "Nature",
  "Quest",
  "Treasure",
];

const tree = new BST(t5);
// tree.setTree(t5);
console.log(tree.findValue("gaRdeN"));
console.log("\nmin = ", tree.findMin());
console.log("max = ", tree.findMax());
