object ProblemOne {

  def findSum: Int = {
    def recurs(x: Int, sum: Int): Int = {
      if (x == 1000) sum
      else if (x % 3 == 0 || x % 5 == 0) recurs(x + 1, sum + x)
      else recurs(x + 1, sum)
    }
    recurs(0, 0)
  }
}


object Main {
  def main(args: Array[String]) {
    import ProblemOne._
    println(findSum)
  }
}
