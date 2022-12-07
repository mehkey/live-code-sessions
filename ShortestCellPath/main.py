from collections import deque

def shortestCellPath(grid, sr, sc, tr, tc):
  """
  @param grid: int[][]
  @param sr: int
  @param sc: int
  @param tr: int
  @param tc: int
  @return: int
  """

  M = len(grid)
  N = len(grid[0])

  q = deque()

  q.append([sr,sc])

  dirs = [[1,0],[0,1],[-1,0],[0,-1]]
  grid[sr][sc] = 0

  dist = 0

  while q:

    for _ in range(len(q)):

      x,y = q.popleft()

      if x == tr and y == tc:
        return dist

      for dir in dirs:
        x_new = x + dir[0]
        y_new = y + dir[1]

        if 0 <= x_new < M and 0 <= y_new < N and grid[x_new][y_new] == 1:
          grid[x_new][y_new] = 0
          q.append([x_new,y_new])
    dist += 1

  return -1


#No I can't hear you

#No I can't hear you
# I cant hear you also

#are you talking??

#yes I can't hear you
# I've turned off my microphone so I think the issue might be on your end because I still cant hear you

#I don't think so

#

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
print(shortestCellPath(grid,0,  0,  2,  0))



#No I can't hear you

#No I can't hear you
# I cant hear you also

#are you talking??

#yes I can't hear you
# I've turned off my microphone so I think the issue might be on your end because I still cant hear you

#I don't think so
# if you cant find the issue we can just end early if thats ok
# maybe I can try to refresh the page but idk if it will end the sesson, because I also
# can see your camera (assuming it still on)

# haha I never had this issue before 30 pramp, first time
# I doubt it's on my end

# when you said you only have a loud lounge

