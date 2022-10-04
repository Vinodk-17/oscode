import java.rmi.*;
public interface PalindromeInterface extends Remote{
	public boolean isPalindrome(int n) throws RemoteException;
}