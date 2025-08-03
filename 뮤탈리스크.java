package algorithm;

import java.util.*;

public class MutaliskBFS {
    static int[][][] visited = new int[61][61][61];
    static int[][] attacks = {
            {9, 3, 1}, {9, 1, 3},
            {3, 9, 1}, {3, 1, 9},
            {1, 9, 3}, {1, 3, 9}
    };
    static int ret = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] scv = new int[3];
        //scv 개수
        for (int i = 0; i < scv.length; i++) {
            scv[i] = scanner.nextInt();
        }

        System.out.println(bfs(scv));
    }
    public static int bfs(int[] scv) {
        visited[scv[0]][scv[1]][scv[2]] = 1;
        Queue<int[]> q = new LinkedList<>();
        q.add(scv);

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int scvHealth1 = cur[0];
            int scvHealth2 = cur[1];
            int scvHealth3 = cur[2];

            if(scvHealth1 == 0 && scvHealth2 == 0 && scvHealth3 == 0)
                break;

            for(int[] attack : attacks) {

                int ret1 = Math.max(0, scvHealth1- attack[0]);
                int ret2 = Math.max(0, scvHealth2 - attack[1]);
                int ret3 = Math.max(0, scvHealth3 - attack[2]);

                if (visited[ret1][ret2][ret3] == 0) {  // 아직 방문 안 한 상태만 큐에 추가
                    visited[ret1][ret2][ret3] = visited[scvHealth1][scvHealth2][scvHealth3] + 1;
                    q.add(new int[]{ret1, ret2, ret3});
                }
            }
        }
        if(visited[0][0][0] == 0) {
            return -1;
        } else
            return visited[0][0][0] -1;
    }
}
