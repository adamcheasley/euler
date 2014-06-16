object ProblemFortyFive {

  def hexTest(x: Int): Double = (Math.sqrt((8*x)+1) + 1) / 4

  def isHexNum(x: Int): Boolean = hexTest(x).toInt == hexTest(x)

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
