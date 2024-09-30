const tree1 = [33, 9, 53, 8, 21, null, 61, null, null, 11, null, null, null];

const tree2 = [
  56,
  26,
  200,
  18,
  28,
  190,
  213,
  12,
  24,
  27,
  null,
  null,
  null,
  null,
];

const tree3 = [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, null, null];

const tree4 = [
  "dog",
  "bus",
  "pin",
  "box",
  "cat",
  "hat",
  "run",
  "bat",
  null,
  "car",
  null,
  "fun",
  null,
  "red",
  "sun",
];

const BST = (tree, target) => {
  if (
    tree === null ||
    target === null ||
    tree === undefined ||
    target === undefined
  ) {
    return false;
  }
  const root = 0;
  let current = root;
  let left = current + 1;
  let right = current + 2;
  let found = false;

  console.log("target =", target);
  console.log("current =", tree[current]);
  console.log("left =", tree[left]);
  console.log("right =", tree[right]);
  console.log("\n");

  if (target === tree[root]) {
    found = true;
  }

  while (!found) {
    if (target < tree[current]) {
      current = left;
      left = current * 2 + 1;
      right = left + 1;

      console.log("left");
      console.log("current =", tree[current]);
      console.log("left =", tree[left]);
      console.log("right =", tree[right]);
      console.log("\n");

      if (tree[current] === target) {
        found = true;
      }
      if (tree[current] === null || tree[current] === undefined) {
        break;
      }
      continue;
    }

    if (target > tree[current]) {
      current = right;
      left = current * 2 + 1;
      right = left + 1;

      console.log("right");
      console.log("current =", tree[current]);
      console.log("left =", tree[left]);
      console.log("right =", tree[right]);
      console.log("\n");

      if (tree[current] === target) {
        found = true;
      }
      if (tree[current] === null || tree[current] === undefined) {
        break;
      }
      continue;
    }
  }

  return found;
};

const treeFindMin = (tree) => {
  const root = 0;
  let current = root;
  let left = 1;
  let right = 2;

  if (!tree) {
    return null;
  }

  console.log("current =", tree[current]);
  console.log("left =", tree[left]);
  console.log("right =", tree[right]);
  console.log("\n");

  while (tree[left] !== null || tree[left] !== undefined) {
    if (tree[left] < tree[current]) {
      current = left;
      left = left * 2 + 1;
      right = left + 1;

      console.log("left");
      console.log("current =", tree[current]);
      console.log("left =", tree[left]);
      console.log("right =", tree[right]);
      console.log("\n");

      if (tree[left] === null || tree[left] === undefined) {
        break;
      } else {
        continue;
      }
    }
  }

  return tree[current];
};

const treeFindMax = (tree) => {
  const root = 0;
  let current = root;
  let left = 1;
  let right = 2;

  if (!tree) {
    return null;
  }

  console.log("current =", tree[current]);
  console.log("left =", tree[left]);
  console.log("right =", tree[right]);
  console.log("\n");

  while (tree[right] !== null || tree[right] !== undefined) {
    if (tree[right] > tree[current]) {
      current = right;
      left = right * 2 + 1;
      right = left + 1;

      console.log("right");
      console.log("current =", tree[current]);
      console.log("left =", tree[left]);
      console.log("right =", tree[right]);
      console.log("\n");

      if (tree[right] === null || tree[right] === undefined) {
        break;
      } else {
        continue;
      }
    }
  }

  return tree[current];
};

const target = "hat";

if (BST(tree4, target)) {
  console.log("--- found ---");
} else {
  console.log("--- not found ---");
}

// console.log("min =", treeFindMin(tree4));
// console.log("max =", treeFindMax(tree4));
