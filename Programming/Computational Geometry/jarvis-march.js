// Javis March Algorithm
// Input - Array of points  [[x1, x2]...]
// Output - Convex Hull ->  [[x1, x2]...]

/**
 *
 * @param {Array} a first point
 * @param {Array} b second point
 * @param {Array} c third point
 *
 * @returns orientation of c with respect to the vector p1->p2
 */
function getCrossProduct(a, b, c) {
  const y1 = b[1] - a[1];
  const y2 = c[1] - a[1];
  const x1 = b[0] - a[0];
  const x2 = c[0] - a[0];

  const val = y2 * x1 - y1 * x2;
  return val;
}

function findConvexHull(arr) {
  if (arr.length < 3) return [];

  // Find the point with smallest x value
  let smallestIndex = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i][0] < arr[smallestIndex[0]]) smallestIndex = i;
  }

  let hull = [];
  let currentPointIndex = smallestIndex;
  let nextPointIndex;
  do {
    hull.push(arr[currentPointIndex]);

    nextPointIndex = (currentPointIndex + 1) % arr.length;

    // loop through all the points

    for (let i = 0; i < arr.length; i++) {
      // positive value of cross product means point i is in the left of
      // vector currentPoint->nextPoint
      if (
        getCrossProduct(arr[currentPointIndex], arr[nextPointIndex], arr[i]) > 0
      ) {
        nextPointIndex = i;
      }
    }

    currentPointIndex = nextPointIndex;
  } while (currentPointIndex !== smallestIndex);

  return hull;
}

const inputPoints = [
  [0, 3],
  [1, 1],
  [2, 2],
  [4, 4],
  [0, 0],
  [1, 2],
  [3, 1],
  [3, 3],
  [3, 0]
];

console.log("convex hull -> ", findConvexHull(inputPoints));
