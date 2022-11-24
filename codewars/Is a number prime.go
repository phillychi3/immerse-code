package kata
import "math"
func IsPrime(n int) bool {
  if(n == 0){
    return false
  }
  if(n<2){
    return false
  }
  if(n%2 == 0 && n!= 2){
    return false
  }
  if(n%3 == 0 && n!= 3){
    return false
  }
  for i:=3;i<int(math.Sqrt(float64(n)));i=i+2 {
    if(n%i == 0 ){
      return false
    }
  }
  return true
}