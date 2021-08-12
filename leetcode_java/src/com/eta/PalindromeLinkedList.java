package com.eta;

import java.util.ArrayList;
import java.util.List;

// test cases:

// Definition for singly-linked list.
class ListNode1 {
     int val;
     ListNode1 next;
     
     // constructors
     ListNode1() {}
     ListNode1(int val) { this.val = val; }
     ListNode1(int val, ListNode1 next) { this.val = val; this.next = next; }
 }

public class PalindromeLinkedList {
	public static boolean isPalindrome(ListNode1 head) {
		// make list
		List<Integer> myList = new ArrayList<>();
		
		// iterate over the linked list
		while (head != null) {
            System.out.println("ListNode value: " + head.val);
            // add to list 
            myList.add(head.val);
            head = head.next;
        }
		
		// Check if the array is a palindrome
		System.out.println(myList);
		int front = 0;
		int back = myList.size() - 1;
		
        return false;
    }
}
