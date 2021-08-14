package com.eta;

public class ReverseLinkedList {
	public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }
        
        ListNode curr = head;
        ListNode prev = null;
        ListNode next = null;
        
        while(curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
        return head;
    }
}
