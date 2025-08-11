package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import static java.lang.Boolean.TRUE;

public class 팰린드롬수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String word = br.readLine();

            //0이면 종료
            if(word.equals("0")) break;

            //Early Return
            if(word.length() == 1) {
                System.out.println("yes");
                continue;
            }

            int left = 0;
            int right = word.length() - 1;
            boolean palinDrom = true;

            while(left<right) {
                if(word.charAt(left) == word.charAt(right)) {
                    left++;
                    right--;
                } else {
                    palinDrom = false;
                    break;
                }
            }

            if(palinDrom) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }

    }
}
