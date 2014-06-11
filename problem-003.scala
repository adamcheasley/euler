// What is the largest prime factor of the number 600851475143?

object ProblemTwo {

  def isPrime(n: Long): Boolean = n == smallestDivisor(n)

  def smallestDivisor(n: Long): Long = findDivisor(n, 2)

  def findDivisor(n: Long, testDivisor: Long): Long = {
    if (square(testDivisor) > n) n
    else if (divides(testDivisor, n)) testDivisor
    else findDivisor(n, testDivisor + 1)
  }

  def square(n: Long): Long = n * n

  def divides(d: Long, n: Long): Boolean = (n % d) == 0

  def findGreatestPrimeFactor(i: Long): Long = {
    def rec(x: Long, toTest: Long, factor: Long): Long = {
      if (toTest == (i - 1L)) factor
      else if (i % toTest == 0 && isPrime(toTest))
        rec(x, toTest + 1L, toTest)
      else rec(x, toTest + 1L, factor)
     }
    rec(i, 2L, 2L)
  }
}


object Main {
  def main(args: Array[String]) {
    import ProblemTwo._
    println(findGreatestPrimeFactor(600851475143L))
  }
}
//test
