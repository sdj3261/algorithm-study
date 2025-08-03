package algorithm;

import java.util.*;

public class GwalhoAdded {
    static int n;
    static String sik;
    static List<Character> op = new ArrayList<>();
    static List<Integer> nums = new ArrayList<>();
    static int maxVal = Integer.MIN_VALUE;

    // 연산 수행
    public static int calc(int a, int b, char op) {
        if (op == '+') return a + b;
        if (op == '-') return a - b;
        return a * b; // *
    }

    public static void go(int idx, int sum) {
        // 마지막 숫자까지 도달
        if (idx == nums.size() - 1) {
            maxVal = Math.max(maxVal, sum);
            return;
        }

        // 1. 괄호 없이 진행
        int nextSum = calc(sum, nums.get(idx + 1), op.get(idx));
        go(idx + 1, nextSum);

        // 2. 괄호로 다음 연산 묶기 (idx+1과 idx+2)
        if (idx + 1 < op.size()) {
            int bracket = calc(nums.get(idx + 1), nums.get(idx + 2), op.get(idx + 1));
            int nextSum2 = calc(sum, bracket, op.get(idx));
            go(idx + 2, nextSum2);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sik = sc.next();

        for (int i = 0; i < sik.length(); i++) {
            if (Character.isDigit(sik.charAt(i))) {
                nums.add(sik.charAt(i) - '0');
            } else {
                op.add(sik.charAt(i));
            }
        }

        go(0, nums.get(0)); // 첫 숫자부터 시작
        System.out.println(maxVal);
    }
}
