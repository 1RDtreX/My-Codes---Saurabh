class Solution {
    public int maxOperations(int[] nums, int k) {
        int sum=0;
        
        for(int i=0;i<nums.lenght;i++)
        {
                for(int j=i;j<nums.lenght;j++)
                {
                        if(nums[i]+nums[j]==k)
                        {
                            sum++;
                        }

                }


        }
        return sum;

    }

    public static void main(String []args)
    {
        Solution obj=new Soulution();
        int []nums={1,2,3,4,5};
        int x=obj.maxOperations(nums,5);
        System.out.println(x);
    }
}