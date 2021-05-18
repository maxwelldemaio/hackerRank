package codingbat_java;
/*
	 Given two int values, return their sum. 
	 Unless the two values are the same, then return double their sum.
	
	sumDouble(1, 2) -> 3
	sumDouble(3, 2) -> 5
	sumDouble(2, 2) -> 8
 */

public class sum_double {
	public static void main(String[] args) {
		// Test cases
		System.out.println(code(1, 1));
		System.out.println(code(3, 3));
		System.out.println(code(2, 2));
	}
	
	public static int code(int a, int b) {
	  // Check if a = b
	  if (a == b) {
		  return (a + b) * 2;
	  }
	  return a + b;
	}
}
