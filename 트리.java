import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] child;
    static int N, root, del, answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        child = new ArrayList[N];
        for (int i = 0; i < N; i++) child[i] = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        root = -1;
        for (int i = 0; i < N; i++) {
            int p = Integer.parseInt(st.nextToken());
            if (p == -1) root = i;
            else child[p].add(i);
        }

        del = Integer.parseInt(br.readLine());

        // 루트가 삭제되면 리프 없음
        if (del == root) {
            System.out.println(0);
            return;
        }

        answer = 0;
        dfs(root);
        System.out.println(answer);
    }

    static void dfs(int u) {
        if (u == del) return; // 삭제 서브트리는 통째로 무시

        boolean isLeaf = true;
        for (int v : child[u]) {
            if (v == del) continue; // 삭제된 자식은 없는 셈
            isLeaf = false;         // 유효한 자식이 하나라도 있으면 리프 아님
            dfs(v);
        }
        if (isLeaf) answer++;
    }
}
