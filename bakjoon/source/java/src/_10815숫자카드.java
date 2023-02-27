import java.util.Arrays;
import java.util.Scanner;

public class _10815숫자카드 {
    static int[] numCard;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        numCard = new int[N];

        for(int i=0; i<N; i++){
            numCard[i] = sc.nextInt();
        }

        Arrays.sort(numCard);

        int M = sc.nextInt();
        StringBuilder result = new StringBuilder();

        for(int i=0; i<M; i++){
            int isFind = binSearch(sc.nextInt());
            result.append(isFind+" ");
        }
        System.out.println(result);
    }

    static int binSearch(int target){
        int start = 0;
        int end = numCard.length - 1;
        while(start <= end){
            int i = (start + end) / 2;
            if(numCard[i] > target) {
                end = i - 1;
            }
            else if(numCard[i] < target) {
                start = i + 1;
            }
            else {
                return 1;
            }
        }
        return 0;
    }
}
