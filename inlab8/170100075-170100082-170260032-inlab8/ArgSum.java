public class ArgSum
{
    public static void main(String[] args)
    {
        int sum = 0;
        for(int i = 0; i < args.length; i++)
        {
            sum += Integer.valueOf(args[i]);
        }
        System.out.println(args.length+","+sum);
    }
}
