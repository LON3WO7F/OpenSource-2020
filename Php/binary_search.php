<?php

function binarySearch($sortedArray, $target)
{
    $leftPoint = 0;
    $rightPoint = (count($sortedArray) -1 );

    while ($leftPoint <= $rightPoint)
    {
        $middlePoint = round(($leftPoint + $rightPoint) / 2);
        if ($sortedArray[$middlePoint] === $target) {
            return $sortedArray[$middlePoint];
        } elseif ($target < $sortedArray[$middlePoint]) {
            $rightPoint = $middlePoint - 1;
        } else {
            $leftPoint = $middlePoint + 1;
        }
    }
    return false;
}



$arr1 = [-2, 3, 4, 7, 8, 9, 11, 13];
var_dump(binarySearch($arr1, 1));

?>
