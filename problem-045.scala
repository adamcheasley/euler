object ProblemFortyFive {

  def hexTest(x: Int): Double = (Math.sqrt((8*x)+1) + 1) / 4

  def isHexNum(n: Int): Boolean = hexTest(n).toInt == hexTest(n)

  def pentTest(x: Int): Double = (Math.sqrt(24 * x + 1) + 1) / 6

  def isPentNum(n: Int): Boolean = pentTest(n).toInt == pentTest(n)

  def computeTriangeNumbers(computeTo: Int): List[Int] = {

    def f(n: Int): Int = {
      n * ((n+1)) / 2
    }

    def recurs(next: Int, tri: List[Int]): List[Int] = {
      if (next == computeTo) tri
      else recurs(next + 1, tri :+ f(next))
    }

    recurs(1, List())
  }
}


object Main {
  def main(args: Array[String]) {
    import ProblemFortyFive._
    println(computeTriangeNumbers(100))
  }
}
