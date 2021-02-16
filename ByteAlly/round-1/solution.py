paths = []
def possiblePaths(graph, s, d):
  global paths
  paths = []
  DFS(s, d, graph, [s])

  return calculateDistance(paths, graph)

# calculateDistance method gives us the total distance between each path from start node to destination node
def calculateDistance(paths, graph):
  ans = []
  for path in paths:
    distance = 0
    for index in range(len(path)-1):
      s = path[index]
      e = path[index+1]
      distance += graph[s][e] 
    
    ans.append((path, distance))

  return ans

# DFS method gives us all possible paths between start node to distination node
def DFS(s, d, graph, path):
  for node, _ in graph[s].items(): # checking childrens of 's' node
    if node == d: # if node is a distination node we found a path so we appending to paths list (globally declared)
      paths.append(path+[node])
    elif node not in path: # if node not present in the path we are checking if there any possible node to reach destination
      DFS(node, d, graph, path+[node])

if __name__ == '__main__':
  try:
    totCity = int(input())
    cities = {}
    for _ in range(totCity):
      city = input()
      cities[city] = {}

    roads = int(input())
    for _ in range(roads):
      path = input().split()
      cities[path[0]][path[1]] = int(path[2])
      cities[path[1]][path[0]] = int(path[2])

    s, d = input().split()
    if not cities.get(s) or not cities.get(d):
      raise KeyError

  except KeyError:
    print("Please pass valid city name of source and destination")
  except ValueError:
    print("Please pass the valid input")
  except TypeError:
    print("Please pass the valid distance between two cities")
  except:
    print("Something went wrong")
  else:
    result = possiblePaths(cities, s, d)
    print("\n-------------- paths -----------------")
    for r in result:
      print(r[0], r[1])
