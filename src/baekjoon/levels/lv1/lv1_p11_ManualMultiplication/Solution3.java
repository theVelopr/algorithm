package baekjoon.levels.lv1.lv1_p11_ManualMultiplication;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * toCharArray
 * 문자열 길이가 가변적으로 입력받으며 문자를 하나씩 참조해야할 때 사용하면 매우 유용함.
 *
 * BufferedReader
 * Scanner 로 입력 받는것보다 성능적으로 더 좋음음
*/

public class Solution3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int A = Integer.parseInt(br.readLine());
        String B = br.readLine();

        char[] b = B.toCharArray();

        System.out.println(A * (b[2] - '0'));
        System.out.println(A * (b[1] - '0'));
        System.out.println(A * (b[0] - '0'));
        System.out.println(A * Integer.parseInt(B));
    }
}
