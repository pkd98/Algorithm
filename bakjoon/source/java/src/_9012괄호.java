import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class _9012괄호 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i=0; i<N; i++){
            Stack stack = new Stack();
            String str = sc.next();
            char [] chars = str.toCharArray();
            boolean check = true;

            for (char c : chars){
                if (c == '(')
                    stack.push(c);

                else if (c == ')') {
                    if (stack.isEmpty()) {
                        check = false;
                        break;
                    }
                    else
                        stack.pop();
                }
            }
            if(stack.isEmpty() && check == true)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}