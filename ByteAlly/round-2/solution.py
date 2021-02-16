paths = []
def possiblePaths(graph, s, d, availablePumps, totCapacity):
  global paths
  paths = []
  DFS(s, d, graph, [s])

  return validPaths(paths, graph, totCapacity, availablePumps)

def validPaths(paths, graph, totCapacity, availablePumps):
  ans = []
  for path in paths:
    distance = 0
    temp = totCapacity
    for index in range(len(path)-1):
      s = path[index]
      e = path[index+1]
      distance += graph[s][e]
      temp += (totCapacity*availablePumps[s]) - graph[s][e]
    
    if temp>=0:
      ans.append((path, distance))

  return ans

def DFS(s, d, graph, path):
  for node, _ in graph[s].items():
    if node == d:
      paths.append(path+[node])
    elif node not in path:
      DFS(node, d, graph, path+[node])

if __name__ == '__main__':
  try:
    totCity = int(input())
    cities = {}
    availablePumps = {}
    for _ in range(totCity):
      city, pumps = input().split()
      pumps = int(pumps)
      cities[city] = {}
      availablePumps[city] = pumps

    roads = int(input())
    for _ in range(roads):
      path = input().split()
      cities[path[0]][path[1]] = int(path[2])
      cities[path[1]][path[0]] = int(path[2])

    s, d = input().split()
    if not cities.get(s) or not cities.get(d):
      raise KeyError
    totCapacity = int(input())

  except KeyError:
    print("Please pass valid city name for source and destination")
  except ValueError:
    print("Please pass the valid input")
  except TypeError:
    print("Please pass the valid distance between two cities")
  except:
    print("Something went wrong")
  else:
    result = possiblePaths(cities, s, d, availablePumps, totCapacity)
    print("\n-------------- paths -----------------")
    for r in result:
      print(r[0], r[1])
