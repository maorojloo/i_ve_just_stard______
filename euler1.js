console.log('its working');


function main(x)
{
    let nums=[];
    
for(let i=1 ;i<x;i++)
{   
    if (i%5==0||i%3==0){nums=nums+i}
    

}


let sum = 0;
sum=0;
for (num of nums)
{
sum += parseInt(num);

}


return sum
}


console.log(main(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000));