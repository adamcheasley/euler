// What is the largest prime factor of the number 600851475143 ?

object ProblemTwo {

  def isPrime(i: Long): Boolean = {
    if (i <= 1L) false
    else if (i == 2L) true
    else !(2L to ((i/2)-1L)).exists(x => i % x == 0L)
  }

  def findGreatesPrimeFactor(i: Long): Long = {
    def rec(x: Long, toTest: Long, factor: Long): Long = {
      if (toTest == (i/2)) factor
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
    println(findGreatesPrimeFactor(600851475143L))
  }
}
