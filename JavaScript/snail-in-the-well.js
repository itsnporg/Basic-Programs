/*The snail climbs up 7 feet each day and slips back 2 feet each night. 
How many days will it take the snail to get out of a well with the given depth? */

function main() {
    var depth = parseInt(readLine(), 10);
    //your code goes here
    var sum = 0;
    var count = 0;
    for (i=0;i<depth;i++)
    {
        sum+=7;
        count++;
        if (sum>=depth)
        {
            break;
        }
      else{
      sum -= 2;
    }
    }

    console.log(count);
}
