
import java.util.Scanner;
import java.util.Stack;

public class _10773제로 {

    public static void main(String[] args) {

        Stack<Integer> st = new Stack<Integer>();
        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();
        int num;
        int answer = 0;

        for(int i=0; i<K; i++){
            num = sc.nextInt();
            st.push(num);
            if (num == 0){
                st.pop();
                st.pop();
            }
        }
        for(Integer i: st){
            answer += (int)i;
        }
        System.out.println(answer);
    }
}
