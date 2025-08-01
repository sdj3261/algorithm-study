package algorithm;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class privacy {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int[] calender = IntStream.range(1, 29).map(i ->i).toArray();
        //파기해야할 개인정보 return 오름차순 1차원 정수 번호
        int[] answer = {};
        List<Integer> ret = new ArrayList<>();

        //모든 달은 28일까지
        Map<String, String> mapTerms = Arrays.stream(terms).collect(Collectors.toMap(term -> term.split(" ")[0], term -> term.split(" ")[1]));
        Map<String, List<String>> mapPrivacies =  new HashMap<>();

        for (int i = 0; i < privacies.length; i++) {
            String[] split = privacies[i].split(" ");
            String date = split[0];
            String type = split[1];
            int idx = i + 1;

            mapPrivacies.computeIfAbsent(type, k -> new ArrayList<>())
                    .add(date + " " + idx);
        }

        for(Map.Entry<String, List<String>> entry : mapPrivacies.entrySet()) {
            List<String> privacys = mapPrivacies.get(entry.getKey());
            for(String privacy : privacys) {
                String[] validateNums = privacy.split(" ");
                int id = Integer.parseInt(validateNums[1]);
                boolean checkPagi = checkPagi(today,plusValidateTime(validateNums[0], Integer.parseInt(mapTerms.get(entry.getKey()))));

                System.out.println(checkPagi + " " + id + " " + today +  plusValidateTime(validateNums[0], Integer.parseInt(mapTerms.get(entry.getKey()))));
                if(checkPagi) {
                    ret.add(id);
                }
            }

        }
        return ret.stream().sorted().mapToInt(i -> i).toArray();
    }
    //이 기간 이후로는 개인정보 파기 대상 메소드 선언 입니다.
    public String plusValidateTime(String today, int validateTime) {
        String[] todaysDate = today.split("\\.");
        int year = Integer.parseInt(todaysDate[0]);
        int month = Integer.parseInt(todaysDate[1]);
        int day = Integer.parseInt(todaysDate[2]);

        int newMonth = month + validateTime;
        if(newMonth > 12) {
            if(newMonth % 12 != 0) {
                year += newMonth / 12;
                month = newMonth % 12;
            } else {
                year += (newMonth / 12) - 1;
                month = 12;
            }
        } else {
            month += validateTime;
        }
        System.out.println(String.valueOf(year) + "." + String.valueOf(month) + "." + String.valueOf(day));
        return String.valueOf(year) + "." + String.valueOf(month) + "." + String.valueOf(day);

    }
    public boolean checkPagi(String today, String validateTime) {
        String[] todaysDate = today.split("\\.");
        String[] validateDate = validateTime.split("\\.");

        //vd 보다 오늘날짜가 크거나 같은 경우 파기
        //vd는 파기 시작일
        for(int i=0; i<todaysDate.length; i++) {
            int td = Integer.parseInt(todaysDate[i]);
            int vd = Integer.parseInt(validateDate[i]);

            if(td > vd || (i ==2 && td == vd)) {
                return true;
            } else if(vd > td) {
                return false;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        privacy privacy = new privacy();
        String today = "2022.05.19";
        String[] terms = 	{"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};
        Arrays.stream(privacy.solution(today, terms, privacies)).forEach(System.out::println);

    }
}
