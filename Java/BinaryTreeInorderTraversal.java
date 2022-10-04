import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class InorderTraversal {
    TreeNode root;
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> st=new Stack<TreeNode>();
        List<Integer> li=new ArrayList<>();
        if(root==null)
            return li;
        while(true){
            if(root!=null){
                st.push(root);
                root=root.left;
            }else{
                if(st.isEmpty())
                    break;
                root=st.pop();
                li.add(root.val);
                root=root.right;
            }
        }
        return li;
    }

    public static void main(String[] args) {
        InorderTraversal in=new InorderTraversal();
        in.root = new TreeNode(37);
        in.root.left = new TreeNode(27);
        in.root.right = new TreeNode(47);
        in.root.left.left = new TreeNode(22);
        in.root.left.right = new TreeNode(32);
        in.root.left.left.left = new TreeNode(12);
        in.root.left.left.right = new TreeNode(25);
        in.root.right.left = new TreeNode(42);
        in.root.right.right = new TreeNode(57);
        in.root.right.right.left = new TreeNode(52);
        in.root.right.right.right = new TreeNode(67);

        System.out.println(in.inorderTraversal(in.root));
    }
}

// OUTPUT: [12, 22, 25, 27, 32, 37, 42, 47, 52, 57, 67]
