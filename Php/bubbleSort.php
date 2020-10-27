<?php
   function bubbleSort($arr){
      // Initialize 2 loops to have indexes of array, the sizeof() function returns the number of elements in an array.
       for($i = 0; $i < sizeof($arr) - 1; $i++){
           for($j = 0; $j < sizeof($arr) - 1 - $i; $j++){
               $k = $j+1; // add + 1 to new variable to initialize next one index after $j
               if($arr[$k] < $arr[$j]){ // check if $j index in array is bigger than next one $k
                   $temp = $arr[$k]; // initialize new variable to have temporary value of the next one index that is smaller than previous
                   $arr[$k] = $arr[$j]; // now reassign to the one index that was smaller than previous to be $i index (that was bigger)
                   $arr[$j] = $temp; // and reassign to the one index that was bigger that next one $k index (that was smaller)
               }
           }
       }
       return $arr; // after all is swaped return sorted array
   }

   // print sorted array to screen (Array ( [0] => 1 [1] => 2 [2] => 3 [3] => 4 [4] => 5 ))
   print_r(bubbleSort(array(5,3,2,4,1)));
?>
