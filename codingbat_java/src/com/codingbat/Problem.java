package com.codingbat;

public class Problem {

	public static void main(String[] args) {
		// Test cases
		int[] intArray1 = {10,20,30,40,50,60,70,80};
		
		System.out.println(firstLast6(intArray1));
	}
	
	public static boolean sleepIn(boolean weekday, boolean vacation) {
		  // Check if weekday or vacation
		  if (vacation) {
		    return true;
		  } 
		  else if (weekday == false) {
		    return true;
		  }
		  else {
		    return false;
		  }
		}
	
	public static int sumDouble(int a, int b) {
		  // Check if a = b
		  if (a == b) {
			  return (a + b) * 2;
		  }
		  return a + b;
	}
	
	public static boolean parrotTrouble(boolean talking, int hour) {
		  if (!talking) {
			  return false;
		  } else if (talking && (hour < 7 || hour > 20)) {
			  return true;
		  } else {
			  return false;
		  }
	}
	
	public static boolean monkeyTrouble(boolean aSmile, boolean bSmile) {
		if ((aSmile && bSmile) || (!aSmile && !bSmile)) {
		    return true;
		  } else {
		    return false;
		  }
	}
	
	public static int diff21(int n) {
		// Check if n is > 21
		if (n > 21) {
			return (21 - n) * -2;
		}
		return 21 - n;
	}
	
	public static boolean makes10(int a, int b) {
		/* 
		 * Given 2 ints, a and b, return true if one if them is 10 
		 * or if their sum is 10.
		 * */
		
		if (a == 10 || b == 10) {
			return true;
		} else if (a + b == 10) {
			return true;
		} else {
			return false;
		}
	}
	
	public static boolean firstLast6(int[] nums) {
		/* 
		 * Given an array of ints, return true if 6 appears as either the 
		 * first or last element in the array. 
		 * The array will be length 1 or more.
		 * */
		if (nums[0] == 6 || nums[nums.length - 1] == 6) {
			return true;
		}
		return false;
	}
	
	public static boolean sameFirstLast(int[] nums) {
		/* 
		 * Given an array of ints, return true if the array is length 1 or more, 
		 * and the first element and the last element are equal.
		 * */
		
	}
}
