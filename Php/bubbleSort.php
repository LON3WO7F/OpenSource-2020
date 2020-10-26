<?php
   function bubbleSort($arr){
        for($i = 0; $i < sizeof($arr) - 1; $i++){
            for($j = 0; $j < sizeof($arr) - 1 - $i; $j++){
                $k = $j+1;
                if($arr[$k] < $arr[$j]){
                    $temp = $arr[$k];
                    $arr[$k] = $arr[$j];
                    $arr[$j] = $temp;
                }
            }
        }
        return $arr;
    }

    bubbleSort(array(5,3,2,4,1));
?>
