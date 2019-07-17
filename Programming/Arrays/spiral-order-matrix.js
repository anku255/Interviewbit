module.exports = {
  //param A : array of array of integers
  //return a array of integers
  spiralOrder: function(A) {
    var m = A.length; //
    var n = A[0].length;

    var top = 0;
    var bottom = m - 1; // row - 1
    var left = 0;
    var right = n - 1; // col - 1

    var dir = 0;

    var spiral = [];
    while (top <= bottom && left <= right) {
      if (dir == 0) {
        for (var i = left; i <= right; i++) spiral.push(A[top][i]);
        dir = 1;
        top += 1;
      } else if (dir == 1) {
        for (var i = top; i <= bottom; i++) spiral.push(A[i][right]);
        right -= 1;
        dir = 2;
      } else if (dir == 2) {
        for (var i = right; i >= left; i--) spiral.push(A[bottom][i]);
        bottom -= 1;
        dir = 3;
      } else if (dir == 3) {
        for (var i = bottom; i >= top; i--) spiral.push(A[i][left]);
        left += 1;
        dir = 0;
      }
    }
    return spiral;
  }
};
