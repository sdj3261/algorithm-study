package algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Server {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int addedServerCount = 0;
        int currentServerCount = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < players.length; i++) {
            //반납
            if(map.get(i) != null) {
                System.out.println(i + " " + currentServerCount + " " + addedServerCount);
                currentServerCount = currentServerCount - map.get(i);
                addedServerCount = addedServerCount - map.get(i);
            }
           //증설 조건
            //1. 어느 시간대의 이용자에 따라 최소 n대 필요
            int needServer = players[i] / m;
            int tempTime = 0;
            //2. 필요만큼 반복
            while(currentServerCount < needServer) {
                addedServerCount++;
                answer++;
                currentServerCount++;
                tempTime++;
            }
            //반납 시간 등록
            if(tempTime > 0) {
                map.put(i + k, tempTime);
            }
        }
        return answer;
    }


    public static void main(String[] args) {
        Server solution = new Server();
        int[] arr = {0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5};
        System.out.println(solution.solution(arr, 3, 5));

    }
}
