
/**

BFS

queue has row, col, pathLengthSoFar
visited has row, col info

traverse through valid neighbors

when you reach target row , col return pathLengthSoFar

if we exit the search, return -1, no path found



*/

const TRAVERSABLE_CELL = 1;

const NO_PATH_FOUND = -1

const getCellStr = (row: number, col: number): string  => `${row}, ${col}`;

const isInBounds = (row, col, grid) => {
  const numRows = grid.length;
  const numCols = grid[0].length;
  
  const rowInBounds = row >= 0 && row < numRows;
  const colInBounds = col >= 0 && col < numCols;
  
  return rowInBounds && colInBounds;
}

const Directions = {
  DOWN : [0, 1],
  UP : [1, 0],
  LEFT : [-1,0],
  RIGHT : [0,-1]
}

const directions = [[0, 1], [1, 0], [-1, 0], [0, -1]];

const getNeighbors = (row, col, grid) => {
  const neighbors = [];
  
  for (const direction of Object.values(Directions))  {
    const [rowChange, colChange] = Directions[direction];
    
    const newRow = row + rowChange;
    const newCol = col + colChange;
    
    const newCellValue = grid[row][col];
    
    if (!isInBounds(newRow, newCol, grid) || newCellValue !== TRAVERSABLE_CELL) continue;
    
    neighbors.push([newRow, newCol]);
  }
  
  return neighbors;
}

const getCellStr = (row: number, col: number): string  => `${row}, ${col}`;


class GridCell {
  constructor(row, col, lengthSoFar) {
    this.row = row;
    this.col = col;
    this.lengthSoFar= lengthSoFar;
  }
}

const shortestCellPath = (grid, startRow, startCol, targetRow, targetCol) => {
	/**
	@param grid: integer[][]
	@param sr: integer
	@param sc: integer
	@param tr: integer
	@param tc: integer
	@return: integer
	*/
  
  
  const queue = [];
  const visited = new Set();
  
  const startCellStr = getCellStr(startRow, startCol);
  
  const startCell = new GridCell(startRow, startCol, 0)
  
  visited.add(startCellStr);
  queue.push(startCell);
  
  var pathLengthSoFar2 = 0
  
  while (queue.length > 0) {
    const len = queue.length;
    for ( let _ =0; _< len; _++){
      const { row, col, pathLengthSoFar } = queue.shift();
      //console.log(pathLengthSoFar2)
      if (row === targetRow && col === targetCol) return pathLengthSoFar2;

      const neighbors = getNeighbors(row, col, grid);

      for (const neighbor of neighbors) {
        const [neighborRow, neighborCol] = neighbor;

        const neighborStr = getCellStr(neighborRow, neighborCol);

        if (visited.has(neighborStr)) continue;

        visited.add(neighborStr);
        queue.push({
          row: neighborRow,
          col: neighborCol,
          pathLengthSoFar: pathLengthSoFar + 1,
        });
      }
    }
    pathLengthSoFar2++;
  }
  
  return NO_PATH_FOUND;
}

