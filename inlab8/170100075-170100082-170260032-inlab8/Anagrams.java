import java.util.Scanner;
public class Anagrams {
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		String s1=sc.next();
		String s2=sc.next();
		int a[]=new int[26];
		for(int i=0;i<26;i++)
			a[i]=0;
		if(s1.length()!=s2.length())
		{
			System.out.println("Not Anagrams");
		}
		else
		{
			for(int i=0;i<s1.length();i++)
			{
				if(s1.charAt(i)>=65&&s1.charAt(i)<=90)
					a[s1.charAt(i)-65]++;
				if(s1.charAt(i)>=97&&s1.charAt(i)<=123)
					a[s1.charAt(i)-97]++;
			}
			for(int i=0;i<s2.length();i++)
			{
				if(s2.charAt(i)>=65&&s2.charAt(i)<=90)
					a[s2.charAt(i)-65]--;
				if(s2.charAt(i)>=97&&s2.charAt(i)<=123)
					a[s2.charAt(i)-97]--;
			}
			int flag=1;
			for(int i=0;i<26;i++)
			{
				if(a[i]!=0)
					flag=0;
			}
			if(flag==1)
				System.out.println("Anagrams");
			else
				System.out.println("Not Anagrams");
		}
	}

}

