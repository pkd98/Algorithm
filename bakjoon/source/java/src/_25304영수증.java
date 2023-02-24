import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _25304영수증 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int X = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int [][] costs = new int[N][2];
        int total = 0;
        StringTokenizer st;

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            costs[i][0] = Integer.parseInt(st.nextToken()); // 물건 가격
            costs[i][1] = Integer.parseInt(st.nextToken()); // 개수
            total += costs[i][0] * costs[i][1];
        }
        if(X == total){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
