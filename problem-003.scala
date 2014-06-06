// What is the largest prime factor of the number 600851475143 ?

object ProblemTwo {

  def isPrime(i: Int): Boolean = {
    if (i <= 1) false
    else if (i == 2) true
    else !(2 to (i-1)).exists(x => i % x == 0)
  }

  def findFactors(i: Int): List[Int] = {
    def rec(x: Int, toTest: List[Int], factors: List[Int]): List[Int] = {
      if (toTest.isEmpty) factors
      else if (i % toTest.head == 0) rec(x, toTest.tail, factors :+ toTest.head)
      else rec(x, toTest.tail, factors)
     }
    rec(i, List.range(2, (i-1)), List())
  }

  // def findPrimeFactors(x: Int): List[Int] = {
  //   def rec(n: Int, toTest: List[Int], primeFactors: List[Int]): List[Int] = {
  //     //if (n == (x/2)) primeFactors
  //     //else
  //   }
  // }
}


object Main {
  def main(args: Array[String]) {
    import ProblemTwo._
    println(findFactors(20))
  }
}
