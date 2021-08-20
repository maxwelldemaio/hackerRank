package com.eta;

/*
 * // Test cases
		String test0 = "";
		String test1 = "42"; //42
		String test2 = "  -42"; //-42
		String test3 = "4193 with words"; //4193
		String test4 = "words and 987"; //0
		String test5 = "-91283472332"; //-2147483648
		String test6 = " "; // 0
		
		StrToIntAtoi s = new StrToIntAtoi();
		System.out.println("Return value: " + s.myAtoi(test6));
 */

public class StrToIntAtoi {
	public int myAtoi(String s) {
		if (s.equals("")) {
			return 0;
		}
		int res = 0, i = 0, sign = 1;
		
		// get rid of whitespace
		while (i < s.length() && s.charAt(i) == ' ') {
			i++;
		}
		
		// check for sign
		if (i < s.length() && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
			// change if negative, iterate
			if (s.charAt(i++) == '-') {
				sign = -1;
			}
		}
		
		// now iterate across digits if any
		// should only be in range 0-9
		while (i < s.length() && s.charAt(i) >= '0' && s.charAt(i) <= '9') {
			// check if we will go over the max
			if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && s.charAt(i) - '0' > 7)) {
				if (sign == -1) {
					return Integer.MIN_VALUE;
				}
				return Integer.MAX_VALUE;
			}
			
			// update res
			res = res * 10 + (s.charAt(i++) - '0');
		}
		return sign * res;
	}
}
