package com.eta;

public class StrToIntAtoi {
	public int myAtoi(String s) {
		// Initialize sum, sign, and iter variables
		int res = 0, sign = 1, i = 0;
		
		// Go through whitespace
		while (s.charAt(i) == ' ') {
			i++;
		}
		
		// Check for sign (and increment to keep going)
		if (s.charAt(i) == '-' || s.charAt(i) == '+') {
			if (s.charAt(i++) == '-') {
				sign = -1;
			}
		}
		
        // Iterate through all digits of input
		// Only iterate while there is valid input
		// Make sure the res does not overflow the Integer max/min value
		while(i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
			
            res = res * 10 + Character.getNumericValue(s.charAt(i));
		}
		
        return sign * res;
	}
}
