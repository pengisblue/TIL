package operator;

public class Operator2 {

    public static void main(String[] args) {

        // 문자열과 문자열 더하기 1
        String result1 = "hello" + "world";
        System.out.println(result1);    // helloworld

        // 문자열과 문자열 더하기 2
        String s1 = "string1";
        String s2 = "string2";
        String result2 = s1 + s2;
        System.out.println(result2);    // string1string2

        // 문자열과 숫자 더하기 1
        String result3 = "a + b = " + 10;   // 숫자를 문자열로 변경
        System.out.println(result3);    // a + b = 10

        // 문자열과 숫자 더하기 2
        int num = 20;
        String str = "a + b = ";
        String result4 = str + num;     // 숫자를 문자열로 변경
        System.out.println(result4);    // a + b = 20
    }
}
