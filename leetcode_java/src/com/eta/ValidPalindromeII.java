package com.eta;

public class ValidPalindromeII {
	public static boolean isPalindrome(String s, int i, int j) {
		while (i < j) {
			if(s.charAt(i++) != s.charAt(j--)) {
				return false;
			}
		}
		return true;
	}
	
	public static boolean isPalindromeII(String s) {
		// Initialize pointers
		int i = 0;
		int j = s.length() - 1;
		
		while (i < j) {
			// Don't match
			if (s.charAt(i) != s.charAt(j)) {
				return isPalindrome(s, i+1, j) || isPalindrome(s, i, j-1);
			}
			
			i++;
			j--;
		}
		
		return true;
	}
}
