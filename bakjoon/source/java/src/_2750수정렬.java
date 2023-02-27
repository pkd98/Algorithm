import java.util.Arrays;
import java.util.Scanner;

public class _2750수정렬 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [] nums = new int[N];

        for (int i = 0; i<N; i++){
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);

        for (int i =0; i<N; i++){
            System.out.println(nums[i]);
        }
    }
}
