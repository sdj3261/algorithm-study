import java.util.Scanner;

public class task1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();

        //32481 81 + 32
        Long ret = Long.MIN_VALUE;
        Long[] data = new Long[n.length()-1];
        for (int i = 0; i < n.length()-1; i++) {
            data[i] = Long.parseLong(n.substring(i,i+2));
        }

        Long overLappingValue = data[0];
        //간격중에 큰 값을 max값으로 선택한다.
        Long[] sub_ret = new Long[data.length];
        for (int i = 0; i < data.length-1; i++) {
            //만약 ret보다 data[i]가크면 업데이트
            if(overLappingValue < data[i]) {
                overLappingValue = data[i];
            }
            sub_ret[i] = overLappingValue;
        }

        for (int i = 0; i < data.length; i++) {
            System.out.println(data[i]);
        }

        long ret2 = Long.MIN_VALUE;
        for(int i=2; i<sub_ret.length; i++) {
            long left = sub_ret[i-2];
            long right = data[i];

            ret2 = Math.max(ret2, left+right);
        }

        System.out.println(ret2);


    }
}