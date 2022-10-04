import java.rmi.*;
import java.util.*;
public class PalindromeClient{
	public static void main (String[] args){
		try{
			PalindromeInterface remoteObj = (PalindromeInterface)Naming.lookup("Palindrome");
			System.out.println(remoteObj.isPalindrome((new Scanner(System.in)).nextInt()));
		}
		catch(Exception e){
			System.out.println(e);
		}
	}
}