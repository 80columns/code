import java.util.*;

class HeapSort
{
    public static ArrayList<Integer> MaxHeapify(ArrayList<Integer> NumberList)
    {
        /* Start sifting up the largest number from the first index in
         * NumberList such that the index has children in the array/heap
         * representation:
         * http://en.wikipedia.org/wiki/Binary_heap#Heap_implementation */
        for(int I = (NumberList.size() / 2) - 1; I >= 0; I--)
        {
            /* Compare the value of the node against its left
             * child's value */
            if(NumberList.get((I*2) + 1) > NumberList.get(I))
            {
                /* Swap the value of the node with the value of
                 * its left child so that the highest value is
                 * placed into the node */
                Integer Temp = NumberList.get(I);
                NumberList.set(I, NumberList.get((I*2) + 1));
                NumberList.set((I*2) + 1, Temp);
            }

            /* First ensure that the node has a right child in the
             * array before comparing the node's value against its
             * right child's value */
            if((I*2) + 2 < NumberList.size())
            {
                /* Compare the value of the node against its right
                 * child's value */
                if(NumberList.get((I*2) + 2) > NumberList.get(I))
                {
                    /* Swap the value of the node with the value of7
                     * its right child so that the highest value is
                     * placed into the node */
                    Integer Temp = NumberList.get(I);
                    NumberList.set(I, NumberList.get((I*2) + 2));
                    NumberList.set((I*2) + 2, Temp);
                }
            }
        }

        return NumberList;
    }

    public static void HeapSort(ArrayList<Integer> NumberList)
    {
        ArrayList<Integer> SortedNumberList = new ArrayList<Integer>();

        /* Turn the array/heap into a max-heap */
        NumberList = MaxHeapify(NumberList);

        /* Remove the head node from the heap, place it in the sorted
         * array, and re-max-heapify NumberList */
        int NumberListSize = NumberList.size();
        for(int I = 0; I < NumberListSize; I++)
        {
            SortedNumberList.add(0, NumberList.remove(0));
            NumberList = MaxHeapify(NumberList);
        }

        System.out.println("The sorted numbers: " + SortedNumberList);
    }

    public static void main(String[] args)
    {
        /* Check the number of command-line arguments */
        if(args.length < 1)
        {
            System.out.println("Error: Supply at least two numbers as " +
                               "arguments");
            System.out.println("E.g.: java HeapSort 1 5 2 8 3 0 9");
        }

        /* Create an array list that will hold the numbers */
        ArrayList<Integer> NumberList = new ArrayList<Integer>();

        /* Place the command-line arguments into the number list */
        for(int I = 0; I < args.length; I++)
        {
            NumberList.add(Integer.parseInt(args[I]));
        }

        /* Sort the numbers */
        HeapSort(NumberList);

        /* Return from main */
        return;
    }
}
