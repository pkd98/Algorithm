import java.util.Scanner;

public class _10872팩토리얼 {

    public static int fact(int n){
        if (n == 0)
            return 1;
        return n* fact(n-1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println(fact(N));
    }
}
