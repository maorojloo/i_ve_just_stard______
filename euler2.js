
function main(x){
let numbs = [1,2];
let nomNomber=2
let privosNumber=1
for(let i =0; i<= x;i++)
{
console.log("doning")

let newNumber = nomNomber+privosNumber;
numbs.push(newNumber);
privosNumber = nomNomber;
nomNomber = newNumber;
}

return numbs
}

let ss =main(10);
console.log(ss);