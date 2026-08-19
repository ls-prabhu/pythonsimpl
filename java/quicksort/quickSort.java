package quicksort;

import java.util.Arrays;

class quickSort {
    static int partition(int array[],int low, int high){
        int pivot = array[high];
        int i = low-1;

        for(int j=low; j<high;j++){
            if(array[j]<=pivot){
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        int temp = array[i+1];
        array[i+1] = array[high];
        array[high] = temp;

        return i+1;
    }


    static void QuickSort(int array[], int low, int high){
        if (low<high) {
            int pi = partition(array, low, high);

            QuickSort(array, low, pi-1);

            QuickSort(array, pi+1, high);
        }
    }
}


class Sorting{
    public static void main(String[] args) {
        int[] data = {5,8,2,43,21,35,12};

        System.out.println("the unsorted array is");
        System.out.println(Arrays.toString(data));

        int size = data.length;

        quickSort.QuickSort(data, 0, size-1);

        System.out.println("the sorted array");
        System.out.println(Arrays.toString(data));
    }
}