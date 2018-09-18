import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class RunThread implements Runnable {
   private Thread t;

   public void run() {
	   try {
		   while(true)
		   {
			   DateTimeFormatter date = DateTimeFormatter.ofPattern("HH:mm:ss");  
			    LocalDateTime now = LocalDateTime.now();  
			    System.out.println(date.format(now));  
	            Thread.sleep(1000);
		   }
	      }catch (InterruptedException e) {
	      } 
   }
   
   public void time_gen() {
      if (t == null) {
         t = new Thread (this);
         t.start (); 
      }
   }
}

public class Clock {

   public static void main(String args[]) {
      RunThread R1 = new RunThread();
      R1.time_gen();
   }    
} 

