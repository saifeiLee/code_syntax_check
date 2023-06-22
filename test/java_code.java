package code_syntax_check.test;

import java.util.Map;

class java_code {
    public static void main(String[] args) {
        System.out.println("Start sleeping...");
        try {
            Thread.sleep(1000 * 5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        Map<String, String> map = Map.of("key", "value");
    }
}
