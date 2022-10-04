import java.rmi.*;
import java.rmi.server.*;
public class Palindrome extends UnicastRemoteObject implements PalindromeInterface {
	Palindrome() throws RemoteException{
		
	}
	public boolean isPalindrome(int n) throws RemoteException{
		int a=n;
		int rev=0;
		while (a!=0){
			int t=a%10;
			rev=rev*10+t;
			a=a/10;
		}
		if(n==rev)
			return true;
		else
			return false;
		
	}
}