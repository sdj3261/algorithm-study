package algorithm;

import java.util.Arrays;
import java.util.Scanner;

import static java.lang.Math.abs;

public class 두용액 {
    public static class Pair {
        int a;
        int b;
        public Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[] arr = Arrays.stream((sc.nextLine().split(" ")))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();
        int left = 0, right = n - 1;
        long minSum = Long.MAX_VALUE;
        long ans1 = 0, ans2 = 0;

        while (left < right) {
            int sum = arr[left] + arr[right];
            int a = Math.abs(sum);
            if (a < minSum) {
                minSum = sum;
                ans1 = arr[left];
                ans2 = arr[right];
            }
            if(sum > 0) {
                right--;
            } else {
                left++;
            }
        }
        System.out.println(ans1 + " " + ans2);
    }
}
