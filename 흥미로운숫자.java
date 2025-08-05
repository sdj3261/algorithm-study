import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String start = sc.next();
        String end = sc.next();
        int startSec = toSeconds(start);
        int endSec = toSeconds(end);

        int count = 0;
        for (int sec = startSec; sec <= endSec; sec++) {
            int h = sec / 3600;
            int m = (sec % 3600) / 60;
            int s = sec % 60;

            String time = String.format("%02d%02d%02d", h, m, s);
            if (isInteresting(time)) count++;
        }
        System.out.println(count);
    }

    private static int toSeconds(String time) {
        String[] parts = time.split(":");
        return Integer.parseInt(parts[0]) * 3600
                + Integer.parseInt(parts[1]) * 60
                + Integer.parseInt(parts[2]);
    }

    private static boolean isInteresting(String time) {
        boolean[] used = new boolean[10];
        int uniqueCount = 0;
        for (char c : time.toCharArray()) {
            int digit = c - '0';
            if (!used[digit]) {
                used[digit] = true;
                uniqueCount++;
                if (uniqueCount > 2) return false;
            }
        }
        return true;
    }
}
