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

public class PreorderTraversal {
     TreeNode root;
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> st=new Stack<TreeNode>();
        List<Integer> li=new ArrayList<Integer>();
        if(root==null)
            return li;
        st.push(root);
        while(!st.isEmpty()){
            root=st.pop();
            if(root.right!=null)
                st.push(root.right);
            if(root.left!=null)
                st.push(root.left);
            li.add(root.val);
        }
        return li;
    }

    public static void main(String[] args) {
        PreorderTraversal pt=new PreorderTraversal();
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

        System.out.println(pt.preorderTraversal(pt.root));
    }
}

// OUTPUT: [37, 27, 22, 12, 25, 32, 47, 42, 57, 52, 67]
