import java.lang.Math;
import java.util.*;

public class PSum
{
    int n,p,arr[],arr2[];
    int coun;
    int adding(int start, int end)
    {
        int sum = 0;
        for(int i = start; i < end; i++)
        {
            sum += arr[i];
        }
        return sum;
    }
    public static void main(String[] args)
    {
        PSum ps = new PSum();
        Scanner sc = new Scanner(System.in);
        ps.n = sc.nextInt();
        ps.p = sc.nextInt();
        ps.arr = new int[(int) Math.pow(ps.p,ps.n)];
        for(int i = 0; i < (int) Math.pow(ps.p,ps.n); i++)
        {
            ps.arr[i] = sc.nextInt();
        }
        for(int i = ps.n; i > 0; i--)
        {
            ps.arr2 = new int[(int) Math.pow(ps.p,i-1)];
            Vector<Thread> v = new Vector<Thread>();
            ps.coun = 0;
            for(int j = 0; j < (int) Math.pow(ps.p,i-1); j++)
            {
                v.add(new Thread(){
                            public void run(){
                                ps.arr2[ps.coun] = ps.adding(ps.coun*ps.p, (ps.coun+1)*(ps.p));
                                ps.coun++;
                            }
                        });
                v.get(j).start();
            }
            for(int j = 0; j < (int) Math.pow(ps.p, i-1); j++)
            {
                try
                {
                    v.get(j).join();
                }
                catch(Exception ex){}
            }
            ps.arr = ps.arr2;
        }
        System.out.println(ps.arr[0]);
    }
}
