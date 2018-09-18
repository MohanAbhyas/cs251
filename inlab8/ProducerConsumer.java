public class ProducerConsumer
{
    int totalStock = 0;
    public static void main(String[] args)
    {
        ProducerConsumer pc = new ProducerConsumer();
        Thread producer = new Thread(){
            public void run() {
                for(int i = 0; i < 100000; i++)
                {
                    pc.totalStock++;
                }
            }
        };
        Thread consumer = new Thread(){
           public void run() {
               for(int i = 0; i < 100000; i++)
               {
                    pc.totalStock--;
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
