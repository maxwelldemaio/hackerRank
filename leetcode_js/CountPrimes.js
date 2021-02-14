/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    // Create isPrime array
    let isPrime = [];
    for (let i = 0; i < n; i++) {
        isPrime[i] = true;
    } 

    // Loop's ending condition is i * i < n instead of i < sqrt(n)
   // to avoid repeatedly calling an expensive function sqrt().
   for (let i = 2; (i * i < n); i++) {
       // Check if number has already been eliminated
       if (!isPrime[i]) {
           continue;
       }
       for (j = (i * i); j < n; j+= i) {
           isPrime[j] = false;
       }
   }

   // Count primes
   let count = 0;
   for (let i = 2; i < n; i++) {
      if (isPrime[i]) count++;
   }
   return count;
};

// Tests
console.log(countPrimes(10));