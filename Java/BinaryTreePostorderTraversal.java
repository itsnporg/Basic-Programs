import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

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
public class PostorderTraversal {
    TreeNode root;
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> li=new ArrayList<>();
        if(root==null)
            return li;
        Stack<TreeNode> st1=new Stack<>();
        Stack<TreeNode> st2=new Stack<>();
        st1.push(root);
        while(!st1.isEmpty()){
            root=st1.pop();
            st2.push(root);
            if(root.left!=null)
                st1.push(root.left);
            if(root.right!=null)
                st1.push(root.right);
        }
        while(!st2.isEmpty()){
            root=st2.pop();
            li.add(root.val);
        }
        return li;
    }

    public static void main(String[] args) {
        PostorderTraversal pt=new PostorderTraversal();
        pt.root = new TreeNode(37);
        pt.root.left = new TreeNode(27);
        pt.root.right = new TreeNode(47);
        pt.root.left.left = new TreeNode(22);
        pt.root.left.right = new TreeNode(32);
        pt.root.left.left.left = new TreeNode(12);
        pt.root.left.left.right = new TreeNode(25);
        pt.root.right.left = new TreeNode(42);
        pt.root.right.right = new TreeNode(57);
        pt.root.right.right.left = new TreeNode(52);
        pt.root.right.right.right = new TreeNode(67);

        System.out.println(pt.postorderTraversal(pt.root));
    }
}
