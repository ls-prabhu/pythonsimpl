package sll;

import java.util.Scanner;

class LinkedList{
    Node head;
    class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
            next = null;
        }
    }
    
    public void insertfirst( int new_data){
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    public void insertAfter(Node preNode,int data){
        if(preNode==null){
            System.out.println("the node can't be null");
            return;
        }

        Node new_node = new Node(data);
        new_node.next = preNode.next;
        preNode.next = new_node;
    }

    public void insertEnd(int data){
        Node new_node = new Node(data);
        if(head==null){
            head = new_node;
            return;
        }
        new_node.next = null;
        Node last =head;

        while (last.next != null) {
            last = last.next;
            last.next = new_node;
            return;
        }
    }

    public void deleteNode(int position){
        if(head== null){
            System.out.println("the list is empty");
        }
        Node temp = head;
        if(position==0){
            head = temp.next;
            return;
        }

        for(int i = 0; temp!= null && i < position-1;i++){
            temp = temp.next;
            if(temp==null||temp.next==null){
                return;
            }
            Node next = temp.next.next;
            temp.next = next;
        }
    }

    boolean search(Node head, int key){
        Node current = head;
        while (current!=null) {
            if(current!=null){
                if(current.data==key){
                    return true;
                }
            }
        }

        return false;
    }

    public void printAll(){
        Node tNode = head;
        while (tNode!=null) {
            System.out.print(" "+tNode.data);
            tNode = tNode.next;
        }
        System.out.print("\n");
        System.out.println(" ^");
        
    }

    public void leavespace(){
        for (int i =0; i<15; i++) {
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList lls = new LinkedList();

        while (true) {
            System.out.println("1. insert in first\n2.insert at end\n3.show all the elements");
            System.out.print("enter your option: ");
            int input = sc.nextInt();
            switch (input) {
                case 1:
                    System.out.print("enter the value: ");
                    int insfv = sc.nextInt();
                    lls.insertfirst(insfv);
                    lls.leavespace();
                    lls.printAll();
                    break;
                
                case 2:
                    System.out.print("enter the value: ");
                    int insev = sc.nextInt();
                    lls.insertEnd(insev);
                    lls.leavespace();
                    lls.printAll();
                    break;
                case 3:
                    lls.leavespace();
                    lls.printAll();
                default:
                    break;
            }
        }
    }
}
