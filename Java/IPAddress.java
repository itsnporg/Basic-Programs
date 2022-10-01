import java.net.InetAddress;
import java.net.UnknownHostException;

public class IPAddress {
    public static void main(String[] args) {
        // get IP address of localhost
        try {
            InetAddress ip = InetAddress.getLocalHost();
            System.out.println("IP address of localhost is: " + ip.getHostAddress());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }

    }
}
