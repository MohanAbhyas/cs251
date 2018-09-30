import java.net.*;
import java.io.*;

public class EchoServer
{
    public static void main(String[] args)
    {
        try
        {
            ServerSocket srvr = new ServerSocket(3050, 2000);
            Socket temp;
            while(true)
            {
                try
                {
                    temp = srvr.accept();
                    DataInputStream inp = new DataInputStream(temp.getInputStream());
                    String msg = inp.readUTF();
                    System.out.println(msg);
                    DataOutputStream outp = new DataOutputStream(temp.getOutputStream());
                    outp.writeUTF(msg+args[0]);
                    temp.close();
                }
                catch (SocketTimeoutException s) {
                }
            }
        }
        catch (IOException e){
            System.out.println("Sorry Dying");
        }
    }
}
