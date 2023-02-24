/*
ATM에 N명 줄서있음.
i번 사람이 인출하는데 걸리는 시간 Pi
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class _11399ATM {

    public static void main(String[] args) {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> Pi = new ArrayList<>();

        for(int i=0; i<N; i++){
            Pi.add(sc.nextInt());
        }
        Collections.sort(Pi);

        for(int i=0; i<N; i++){
            for (int j=0; j<N-i; j++){
                answer += Pi.get(j);
            }
        }
        System.out.println(answer);
    }
}
