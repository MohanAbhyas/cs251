public class ProducerConsumerFix
{
    int totalStock = 0;
    public synchronized void add(int value){
        totalStock += value;
    }
    public static void main(String[] args)
    {
        ProducerConsumerFix pc = new ProducerConsumerFix();
        Thread producer = new Thread(){
            public void run() {
                for(int i = 0; i < 100000; i++)
                {
                    pc.add(1);
                }
            }
        };
        Thread consumer = new Thread(){
           public void run() {
               for(int i = 0; i < 100000; i++)
               {
                    pc.add(-1);
               }
           }
        };
        producer.start();
        consumer.start();
        try
        {
            producer.join();
        }
        catch(Exception ex)
        {
        }
        try
        {
            consumer.join();
        }
        catch(Exception ex)
        {
        }
        System.out.println(pc.totalStock);
    }
}
