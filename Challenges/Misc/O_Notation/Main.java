public class Main {

    public static void main(String[] args) {
    }


    private static String fun1(int n) {
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            sum++;
        }
        return "THICTF{";
    }

    private static String fun2(int n) {
        int sum = 0;
        for (int i = 1; i < n; i *= 2) {
            for (int j = 0; j < n; j++) {
                sum++;
            }
        }
        return "da";
    }

    private static String fun3(int n) {
        int sum = 0;
        for (int i = 2; i < n; i *= 2) {
            for (int j = 1; j < i; j *= 2) {
                sum++;
            }
        }
        return "so";
    }

    private static String fun4(int n) {
        int sum = 0;
        for (int i = 0; i < n * n; i++) {
            for (int j = 0; j < i; j++) {
                sum++;
            }
        }
        return "thm";
    }

    private static String fun5(int n) {
        int sum = 0;
        for (int i = 0; i < n * n; i++) {
            sum++;
        }
        for (int j = 0; j < n; j++) {
            sum++;
        }
        return "ori";
    }

    private static String fun6(int n) {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < 1000; j++) {
                for (int k = 1; k * k < n; k++) {
                    sum++;
                }
            }
        }
        return "lg";
    }

    private static String fun7(int n) {
        int sum = 0;
        for (int i = 0; i < n * n * n; i++) {
            for (int j = 0; j < n * n * n; j++) {
                sum++;
            }
        }
        return "}";
    }

    private static String fun8(int n) {
        int sum = 0;
        for (int i = 1; i < n; i *= 2) {
            for (int j = 0; j < i; j++) {
                sum++;
            }
        }
        return "rte";
    }
}
