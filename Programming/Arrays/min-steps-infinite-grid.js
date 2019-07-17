module.exports = {
  //param A : array of integers
  //param B : array of integers
  //return an integer
  coverPoints: function(A, B) {
    const noOfPoints = A.length;

    let minDist = 0;

    for (let i = 0; i < noOfPoints - 1; i++) {
      let pointOneX = A[i];
      let pointOneY = B[i];

      let pointTwoX = A[i + 1];
      let pointTwoY = B[i + 1];

      x_dist = Math.abs(pointOneX - pointTwoX);
      y_dist = Math.abs(pointOneY - pointTwoY);

      minDist += Math.max(x_dist, y_dist);
    }
    return minDist;
  }
};
