package codingbat_java;

public class sleepIn {

	public static void main(String[] args) {
		// Test cases
		System.out.println(code(false, false));
		System.out.println(code(true, false));
		System.out.println(code(true, true));
	}
	
	public static boolean code(boolean weekday, boolean vacation) {
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
}
