import java.util.Scanner;

public class linearSum{
	public static void main(String args[]){
		long[] A;

        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int p=sc.nextInt();
        int tot=(int)Math.pow(p,n);
        A= new long[tot] ;
        for (int i = 0; i < tot; i++) {
            A[i]=sc.nextInt();
        }
        long sum=0;
        for (int i = 0; i < tot; i++) {
            sum+=A[i];
        } 
        System.out.println(sum);
	}
}