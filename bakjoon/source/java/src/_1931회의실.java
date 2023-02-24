/*
 회의실 배정
  1개의 회의실과 N개 회의에 대해 회의실 사용표 만들기
  각 회의 시작시간 끝나는시간
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class _1931회의실 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        int N = Integer.parseInt(br.readLine());
        int [][] time = new int[N][2];

        StringTokenizer st;

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            time[i][0] = Integer.parseInt(st.nextToken()); // 시작시간
            time[i][1] = Integer.parseInt(st.nextToken()); // 종료시간
        }

        Arrays.sort(time, new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {

                if(o1[1] == o2[1]){ // 종료시간 같다면, 시작시간 빠른순 정렬
                    return o1[0] - o2[0];
                }
                return o1[1] - o2[1]; // 종료시간 빠른 순서대로 정렬
            }
        });

        int cnt = 0, previousEndTime = 0;

        for(int i=0; i<N; i++){

            if(previousEndTime <= time[i][0]) {
                previousEndTime = time[i][1];
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
