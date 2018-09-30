import java.io.*;
import java.util.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FrequencyCollection
{
    public static void main(String[] args)
    {
        String content = new String();
        try
        {
        content = new String(Files.readAllBytes(Paths.get(args[0])));}
        catch(Exception e){};
        String a = new String();
        StringTokenizer st1 = new StringTokenizer(content);
        SortedMap<String, Integer> sm = new TreeMap<String, Integer>();
        ArrayList<String> al = new ArrayList<String>(Arrays.asList("and", "the", "is", "in", "at", "of", "his", "her", "him"));
        ArrayList<String> words = new ArrayList<String>();
        while(st1.hasMoreTokens())
        {
            a = st1.nextToken();
            if(!al.contains(a.toLowerCase()))
            {
                words.add(a.toLowerCase());
            }
        }
        Collections.sort(words);
        String prev = new String("");
        for(String temp : words)
        {
            if(!temp.equals(prev))
            {
                System.out.print(temp+" ");
                System.out.println(Collections.frequency(words, temp));
                prev = temp;
            }
        }
    }
}
