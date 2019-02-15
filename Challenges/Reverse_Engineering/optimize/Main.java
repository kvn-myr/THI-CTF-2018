import java.util.Arrays;

public class Main {

    public static int sieveOfEratosthenes(int n, int max) {
        boolean prime[] = new boolean[n+1];
        Arrays.fill(prime, true);
        for(int p = 2; p*p <= n; p++){
            if(prime[p]){
                for(int i = p*2; i<=n; i+=p){
                    prime[i] = false;
                }
            }
        }

        int sum = 0;
        for(int i = 2; i <=n; i++){
            if(prime[i]){
                sum+=i;
                if(sum>= max){
                    return sum;
                }
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(sieveOfEratosthenes(160000, 1000000000));
    }
}
