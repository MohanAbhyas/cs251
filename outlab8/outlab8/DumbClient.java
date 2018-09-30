import java.net.*;
import java.io.*;

public class DumbClient
{
    public static void main(String[] args)
    {
        try
        {
            Socket clnt = new Socket("localhost", 3050);
            System.out.println(args[0]);
            DataInputStream inp = new DataInputStream(clnt.getInputStream());
            DataOutputStream outp = new DataOutputStream(clnt.getOutputStream());
            outp.writeUTF(args[0]);
            String msg = inp.readUTF();
            System.out.println(msg);
            clnt.close();
        }
        catch (IOException e)
        {
            System.out.println("Dying");
        }
    }
}
