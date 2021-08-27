package com.eta;

import java.util.HashMap;
import java.util.Map;

public class LinkedListCycle {
	public boolean hasCycle(ListNode head) {
		// Create new hashmap to store hashCodes and indexes
//		int i = 0;
//		Map<Integer, Integer> code_map = new HashMap<>();
//		
//		// loop
//		while(head != null) {
//			System.out.println("Value: " + head.val);
//			if (code_map.containsKey(head.hashCode())) {
//				return true;
//			}
//			
//			// add hashcode to map
//			code_map.put(head.hashCode(), i);
//			
//			// continue
//			head = head.next;
//			i++;
//		}
//        return false;
		
		ListNode slow_p = head, fast_p = head;
		
        int flag = 0;
        while (slow_p != null && fast_p != null
               && fast_p.next != null) {
            slow_p = slow_p.next;
            fast_p = fast_p.next.next;
            if (slow_p == fast_p) {
                flag = 1;
                break;
            }
        }
        if (flag == 1) {
        	System.out.println("Loop found");
            return true;
        }
        System.out.println("Loop not found");
    	return false;
    }
}
