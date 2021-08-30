using System;

namespace ReverseSinglyLinkedList {
    class Node {
        public int Value;
        public Node Next;

        public Node(int _Value) {
            this.Value = _Value;
            this.Next = null;
        }

        public Node Reverse() {
            if (this.Next == null) {
                return this;
            } else {
                var ReversedListHead = this.Next.Reverse();

                this.Next.Next = this;
                this.Next = null;

                return ReversedListHead;
            }
        }

        public void Print() {
            Console.Write($"{this.Value}");

            if (this.Next != null) {
                Console.Write(", ");

                this.Next.Print();
            } else {
                Console.WriteLine();
            }
        }
    }

    class Program {
        static void Main() {
            var Head = new Node(1);
            var TempNode = Head;

            for (var i = 0; i < 10; i++) {
                TempNode.Next = new Node(i + 2);
                TempNode = TempNode.Next;
            }

            Head.Print();
            Head = Head.Reverse();
            Head.Print();
        }
    }
}