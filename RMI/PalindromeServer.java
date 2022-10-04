import java.rmi.*;
import java.rmi.server.*;

public class PalindromeServer{
	public static void main(String[] args){
		try{
			Palindrome palindrome = new Palindrome();
			Naming.rebind("Palindrome", palindrome);
			System.out.println("Server Started");
		}
		catch (Exception e){
			System.out.println(e);
		}
	}
}
