object ProblemTwo {

  def evenFib: Int = {
    def recurs(prevFib: Int, curFib: Int, sum: Int): Int = {
      if (curFib > 4000000) sum
      else if (curFib % 2 == 0) recurs(curFib, curFib + prevFib, sum + curFib)
      else recurs(curFib, curFib + prevFib, sum)
    }
    recurs (1, 1, 0)
  }
}


object Main {
  def main(args: Array[String]) {
    import ProblemTwo._
    println(evenFib)
  }
}
