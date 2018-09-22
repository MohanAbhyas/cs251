import java.io.FileWriter; 
import java.util.Scanner;
public class writetestcase{
	public static void main(String args[])
	{ 
		Scanner sc= new Scanner(System.in);
		System.out.println("n");
		int n=sc.nextInt();
        
		System.out.println("p");
        int p=sc.nextInt();

		System.out.println("testcasefilenumber");
        int f=sc.nextInt();

		try{    
		   FileWriter fw=new FileWriter("testcase"+f+".txt");
		   fw.write(n+" "+p+"\n");
		   //fw.newLine();
		   for (int i=1 ;i<Math.pow(p,n)+1 ; ++i) {
			fw.write(i+" ");
		}    
		   fw.close();    
		  }
		  catch(Exception e){System.out.println(e);}    
          System.out.println("Success...");    
     }    
	}
