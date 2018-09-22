import java.util.*;

class Summation extends Thread {

    private int[] arr;

    private int low, high, partial;

    public Summation(int[] arr, int low, int high)
    {
        this.arr = arr;
        this.low = low;
        this.high = Math.min(high, arr.length);
    }

    public int getPartialSum()
    {
        return partial;
    }

    public void run()
    {
        partial = sum(arr, low, high);
    }
    public static int sum(int[] arr, int low, int high)
    {
        int total = 0;

        for (int i = low; i < high; i++) {
            total += arr[i];
        }
        return total;
    }
    public static void parallelSum(int[] arr, int threads, int p)
    {
        int size = arr.length/threads;
        while(threads>0)
        {
        Summation[] sums = new Summation[threads];

        for (int i = 0; i < threads; i++) {
            sums[i] = new Summation(arr, i * size, (i + 1) * size);
            sums[i].start();
        }
        for (int i = 0; i < threads; i++)
         try {
            for (Summation sum : sums) {
                sum.join();
            }
        } 
        catch (InterruptedException e) { }

        int total = 0;
        int big[]=new int[threads];
        int k=0;
        for (Summation sum : sums) {
            big[k]=sum.getPartialSum();
            ++k;
        }
        arr=big;
        threads/=p;
        }
      System.out.println(arr[0]);
    }

}

public class PSum
{
 public static void main(String[] args)
  {
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int p=sc.nextInt();/*int n=10;int p=2;*/
    int arr[]=new int[(int)Math.pow(p,n)];
    for (int i = 0; i < arr.length; i++)
        arr[i] = sc.nextInt(); //arr[i]=i+1;    
    Summation.parallelSum(arr,(int)Math.pow(p,n-1),p);
  }
}
