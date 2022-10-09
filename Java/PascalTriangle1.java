//Lists the Pascal's Triangle

import java.util.*;

public class PascalTriangle1 {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> tri=new ArrayList<>();
        for(int i=0;i<numRows;i++){
            List<Integer> list=new ArrayList<>();
            if(i==0){
                // System.out.println("Hello1");
                list.add(1);
            }else if(i==1){
                // System.out.println("Hello2");
                list.add(1);
                list.add(1);
            }else{
                list.add(tri.get(i-1).get(0));
                // System.out.println("Hello3");
                for(int j=0;j<tri.get(i-1).size()-1;j++){
                    // System.out.println("Hello4");
                    list.add(tri.get(i-1).get(j)+tri.get(i-1).get(j+1));
                }
                list.add(tri.get(i-1).get(0));
            }
            // System.out.println(list);
            tri.add(list);
        }
        return tri;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int i=sc.nextInt();
        System.out.println(generate(i));
    }
}

// Input: 5
// Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
