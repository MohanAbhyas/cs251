import java.util.Scanner;
class Summation extends Thread {

    private long[] arr;

    private int low, high;long partial;

    public Summation(long[] arr, int low, int high)
    {
        this.arr = arr;
        this.low = low;
        this.high = Math.min(high, arr.length);
    }


    public void run()
    {
        sum(arr, low, high);
    }

    public static void sum(long[] arr, int low, int high)
    {
        long sum=0;
        for (int i = low; i < high; i++) {
            sum+=arr[i];

        }
        //return sum;
        arr[low/(high-low)]=sum;
    }


    public static void parallelSum(long[] arr,int threads,int size)
    {
        //System.out.println("paralleSum called");
        if (threads>=1)
        {
        Summation[] sums = new Summation[threads];

        for (int i = 0; i < threads; i++) {
            sums[i] = new Summation(arr, i * size, (i + 1) * size);
            sums[i].start();
        }

        try {
            for (Summation sum : sums) {
                sum.join();
            }
        } catch (InterruptedException e) { }

        long total = 0;
        Summation.parallelSum(arr,threads/size,size);
        /*for (Summation sum : sums) {
            total += sum.getPartialSum();
        }

        return total;*/
    }
    else
        return ;
    }


}


    /*class mythread extends Thread{
        private Thread t;
        public void run(){
            try{

            }
            catch(Exception e){

            }
        }
    }*/

public class PSum{

    public static void main(String args[])
    {
        long[] A;

        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int p=sc.nextInt();
        int tot=(int)Math.pow(p,n);
        A= new long[tot] ;
        for (int i = 0; i < tot; i++) {
            A[i]=sc.nextInt();
        }
        long[] B=A;
        //System.out.println(Summation.parallelSum(B,(int)Math.pow(p,n-1),p));
        Summation.parallelSum(B,(int)Math.pow(p,n-1),p);
        System.out.println(B[0]);

        //System.out.println("Parallel: " + (System.currentTimeMillis() - start)); // Parallel: 25
    }
}