let factors=[]
//target=600851475143
target=500
for(let i=0;i<=target;i++)
{
if(target%i==0){factors.push(i)}


}
console.log(factors)

let primeFactors=[];
for(fac of factors)
{
let factt=0;
for(let i =0; i<=fac;i++)
{
if(fac%i==0){factt++;}




}

if (factt<=2){primeFactors.push(factt)}




}

console.log(primeFactors);