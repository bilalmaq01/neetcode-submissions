class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int o = nums2.length;
        int p = nums1.length;
        if (nums1.length == 0) {
            if (nums2.length % 2 != 0) {
            // Odd number of elements, median is the middle element
            return nums2[nums2.length / 2];
            } else {
            // Even number of elements, median is the )average of the two middle elements
                int middle1 = nums2[o / 2 - 1];
                int middle2 = nums2[o / 2];
                return (double) (middle1 + middle2) / 2.0; // Use 2.0 for floating-point division
            }
        }
        if (nums2.length == 0) {
            if (nums1.length % 2 != 0) {
            // Odd number of elements, median is the middle element
            return nums1[nums1.length / 2];
            } else {
            // Even number of elements, median is the average of the two middle elements
                int middle1 = nums1[p / 2 - 1];
                int middle2 = nums1[p / 2];
                return (double) (middle1 + middle2) / 2.0; // Use 2.0 for floating-point division
            }
        }



        int m  = nums1.length; //0 ->
        int n  = nums2.length; //1 -> 1

        int half = (m+n+1)/2; //1.5 -> 1

        int low = 0;
        int high = m;        //1

        double median = defineBorders(high,low,half, nums1, nums2, m, n);
        return median;

    }

    public static double defineBorders(int high, int low,int half, int[] nums1, int[] nums2, int m,int  n){

        int i = (low+high) / 2; //1
        int j = half - i;       //0

        int LA = (i <= 0) ? Integer.MIN_VALUE : nums1[i-1]; //2
        int RA = (i >= m) ? Integer.MAX_VALUE : nums1[i];  //999
        int LB = (j <= 0) ? Integer.MIN_VALUE : nums2[j-1]; //-999
        int RB = (j >= n) ? Integer.MAX_VALUE : nums2[j];   //999

        if (LA > RB){
            return defineBorders(i - 1, low,half,nums1, nums2, m, n);
        } else if (LB > RA) {
            return defineBorders(high, i + 1,half,nums1, nums2, m, n);
        } else {
            double leftMax = Math.max(LA,LB);
            double rightMin = Math.min(RA, RB);
            return (n + m) % 2 == 0 ? 
            (rightMin + leftMax) / 2.0 :
            leftMax;
        }
    }
}
