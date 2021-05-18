package codingbat_java;
/*
 * Given an int n, return the absolute difference between n and 21, 
 * except return double the absolute difference if n is over 21.
	diff21(19) 2
	diff21(10) 11
	diff21(21) 0
 */

public class diff21 {
	public static void main(String[] args) {
		// Test cases
		System.out.println(code(19));
		System.out.println(code(10));
		System.out.println(code(21));
	}
	
	public static int code(int n) {
		// Check if n is > 21
		if (n > 21) {
			return (21 - n) * -2;
		}
		return 21 - n;
	}
}
