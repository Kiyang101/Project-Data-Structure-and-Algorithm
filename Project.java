
class BST{
    private Integer[] tree;
    private int current;
    private int left;
    private int right;

    public BST(){}
    public BST(Integer[] tree){
        this.tree = tree;
    }

    public void setTree(Integer[] tree){
        this.tree = tree;
    }

    private void goLeft(){
        this.current = this.left;
        this.left = this.current * 2 + 1;
        this.right = this.left + 1;
    }

    private void goRight(){
        this.current = this.right;
        this.left = this.current * 2 + 1;
        this.right = this.left + 1;
    }

    public boolean findValue(int target){
        this.current = 0;
        this.left = 1;
        this.right = 2;
        try {
            while(this.tree[this.current] != null) {
                if (target == this.tree[this.current]) {
                    return true;
                }
                if (target < this.tree[this.current]) {
                    goLeft();
                } else {
                    goRight();
                }
            }
        }catch(IndexOutOfBoundsException e){
            return false;
        }
        return false;
    }

    public int findMin(){
        this.current = 0;
        this.left = 1;
        this.right = 2;
        try {
            while (this.tree[this.current] != null) {
                if(this.tree[this.left] == null){
                    return this.tree[this.current];
                }
                goLeft();
            }
        }catch (IndexOutOfBoundsException e){
            return this.tree[this.current];
        }
        return this.tree[this.current];
    }

    public int findMax(){
        this.current = 0;
        this.left = 1;
        this.right = 2;
        try {
            while (this.tree[this.current] != null) {
                if(this.tree[this.left] == null){
                    return this.tree[this.current];
                }
                goRight();
            }
        }catch (IndexOutOfBoundsException e){
            return this.tree[this.current];
        }
        return this.tree[this.current];
    }
}

public class Project {
    public static void main(String[] args) {
        Integer[] t2 = {56 ,26, 200, 18, 28, 190, 213, 12, 24, 27, null, null, null, null, null};
        BST tree = new BST(t2);
        System.out.println(tree.findValue(27));
        System.out.println(tree.findMin());
        System.out.println(tree.findMax());
    }
}
