package dll;

import java.util.Scanner;

public class doublyll {

    Node head;
    
    class Node{
        int data;
        Node prev;
        Node next;

        Node(int d){
            this.data = d;
        }
    }

    public void insertFront(int data){
        Node newNode = new Node(data);

        newNode.next = head;

        newNode.prev = null;

        head = newNode;

        if(head!=null){
            head.prev = newNode;
            head = newNode;
        }
    }


    public void insertEnd(int data){
        Node newNode = new Node(data);

        Node temp = head;

        newNode.next = null;

        if(head==null){
            newNode.prev = null;
            head = newNode;
            return;
        }
        while(temp.next!=null){
            temp=temp.next;
        }
        temp.next = newNode;
        newNode.prev = temp;
    }

    public void insertAfter(int target, int data){
        Node current = head;
        while (current!=null&&current.data!=target) {
            current = current.next;
        }

        Node newNode = new Node(data);

        newNode.next = current.next;
        current.next = newNode;

        newNode.prev = current;

        if(newNode.next!= null){
            newNode.next.prev = newNode;
        }
    }


    void deleteNode(Node delNode){
        if(head==null||delNode==null){
            return;
        }
        if(head==delNode){
            head = delNode.next;
        }
        if(delNode.next!=null){
            delNode.next.prev = delNode.prev;
        }

        if(delNode.prev!=null){
            delNode.prev.next = delNode.next;
        }
    }

    void printAll(){
        Node tNode = head;
        leavespace();
        System.out.println("doubly linked list");
        if(head==null){
            System.out.println("this is empty");
            return;
        }
        while (tNode!=null) {
            if (tNode.prev!=null&&tNode!=head) {
                System.out.print("<");
            }else{
                System.out.print(":");
            }
            System.out.print(tNode.data);
            if(tNode.next!=null){
                System.out.print(">");
            }else{
                System.out.print(":");
            }
            tNode = tNode.next;
        }
        System.out.println();
    }

    void leavespace(){
        int i = 0;
        while (i<=15) {
            System.out.println("\n");
            i++;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        doublyll dll = new doublyll();

        while (true) {
            System.out.println("1. insert in first\n2.insert at end\n3.Insert after specific node\n4.show all the elements");
            System.out.print("enter your option: ");
            int input = sc.nextInt();
            switch (input) {
                case 1:
                    System.out.print("enter the value: ");
                    int insfv = sc.nextInt();
                    dll.insertFront(insfv);
                    dll.leavespace();
                    dll.printAll();
                    break;
                
                case 2:
                    System.out.print("enter the value : ");
                    int insev = sc.nextInt();
                    dll.insertEnd(insev);
                    dll.leavespace();
                    dll.printAll();
                    break;
                case 3:
                    dll.leavespace();
                    dll.printAll();
                    System.out.print("insert after which node? :");
                    int insnxtnode= sc.nextInt();
                    System.out.print("enter the data:");
                    int insval = sc.nextInt();
                    dll.insertAfter(insnxtnode, insval);
                    dll.printAll();

                case 4:
                    dll.leavespace();
                    dll.printAll();
                default:
                    break;
            }
        }
    }
}