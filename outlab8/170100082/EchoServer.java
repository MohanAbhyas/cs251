import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
 
public class EchoServer
{
 
    private static Socket socket;
 
    public static void main(String[] args)
    {
        try
        {
 	    int port = 8075;
            ServerSocket serverSocket = new ServerSocket(port);
	    String server_quote="";
	    for(int i=0;i<args.length-1;i++)
   	    {
             server_quote+=args[i]+" ";
            }
	    server_quote+=args[args.length-1];
            while(true)
            {
                socket = serverSocket.accept();
                InputStream is = socket.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);
                String client_message = br.readLine();
                System.out.println(client_message);
                String returnMessage;
                returnMessage = client_message + server_quote + "\n";

                OutputStream os = socket.getOutputStream();
                OutputStreamWriter osw = new OutputStreamWriter(os);
                BufferedWriter bw = new BufferedWriter(osw);
                bw.write(returnMessage);
                bw.flush();
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                socket.close();
            }
            catch(Exception e){}
        }
    }
}
