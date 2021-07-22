package baekjoon.levels.lv1.lv1_p11_ManualMultiplication;

import java.util.Scanner;

/**
 * 이 문제는 하나로 입력된 문자(숫자)를 분리하여 연산을 할 수 있는지를 확인하는 문제다.
 *
 * 풀이
 * 1. 문자열로 입력받아 charAt() 으로 하나씩 꺼내 쓰는 방법
 * 2. 나머지와 나눗셈 연산을 통해 각 자릿수를 구하여 쓰는 방법
 * 3. 문자열을 character 배열로 한 자리씩 넣어주어 이용하는 방법
 *
 * 여기서 1번과 3번의 방법은 문자열로 입력받기 때문에 가장 마지막 출력(6) 에서는 연산하기 위해서 int형으로 변환해주어야 한다.
 */

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        String b = sc.next();

        sc.close();

        System.out.println("Solution 1");
        System.out.println(a * (b.charAt(2) - '0'));
        System.out.println(a * (b.charAt(1) - '0'));
        System.out.println(a * (b.charAt(0) - '0'));
        System.out.println(a * Integer.parseInt(b));
        System.out.println("---------------------");
    }
}
