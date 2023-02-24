import java.util.Scanner;
/*
    K원 동전 최소 개수 출력
*/
public class _11047동전0 {

    public static int minCoins(int K, int[] coins){
        int n, cnt = 0;
        int k = K;
        for(int i = coins.length-1; i >= 0; i--){
            if(k >= coins[i]) {
                n = k / coins[i];
                k -= n * coins[i];
                cnt += n;
                // System.out.println(K);
            }
            if(k == 0){
                break;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N, K, i;
        N = sc.nextInt();
        K = sc.nextInt();
        int [] coins = new int[N];

        for(i = 0; i < N; i++){
            coins[i] = sc.nextInt();
        }

        int answer = minCoins(K, coins);
        System.out.println(answer);
    }
}