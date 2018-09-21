import java.io.*; 
import java.util.*; 
public class FrequencyCollection
{ 
  public static void main(String[] args) throws IOException
  { 
  File file = new File(args[0]); 
  BufferedReader br = new BufferedReader(new FileReader(file)); 
  String str; 
  ArrayList<String> duplicate = new ArrayList<String>();
  Set<String> lexico_unique = new TreeSet<String>(); 
  while ((str = br.readLine()) != null)
  {
   StringTokenizer st = new StringTokenizer(str);  
   while (st.hasMoreTokens()) 
   {  
    String temp=st.nextToken().toLowerCase();
    if(temp.compareTo("and")!=0 && temp.compareTo("the")!=0 && temp.compareTo("is")!=0 && temp.compareTo("in")!=0 &&
    temp.compareTo("at")!=0 && temp.compareTo("of")!=0 && temp.compareTo("his")!=0 && temp.compareTo("her")!=0 && temp.compareTo("him")!=0)
    {
        duplicate.add(temp); 
        lexico_unique.add(temp); 
    }
   }   
  } 
  for (String word: lexico_unique) 
  {
   System.out.println(word + "," + Collections.frequency(duplicate, word));
  } 
 } 
}
