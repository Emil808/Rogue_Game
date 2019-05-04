from collections import defaultdict 

# Emil's dfs_bfs
class GraphDBfs:
	def __init__(self): 
		self.graph = defaultdict(list)
		self.marked = {}
		self.edgeto = {}

	def addEdge(self, u, v):
		self.graph[u].append(v)   # u, is connected to v
		self.graph[v].append(u)

	def dfs(self, v):		# finds vertices connected to v through dfs

		for x in self.graph: 	# initialize marked properties as False
			self.marked[x] = False
			self.edgeto[x] = None
		self.rdfs(v)

	def rdfs(self, v):		# recursive dfs
		self.marked[v] = True
		for x in self.graph[v]:
			if not self.marked[x]:
				self.rdfs(x)
				self.edgeto[x] = v


	def bfs(self, v):
		queue = []
		distTo = {}
		for x in self.graph: 	# initialize marked properties as False
			self.marked[x] = False
			self.edgeto[x] = None
		queue.append(v)
		self.marked[v] = True
		distTo[v] = 0

		while len(queue) != 0:
			t = queue.pop(0)

			for x in self.graph[t]:
				if not self.marked[x]:
					queue.append(x)
					self.marked[x] = True
					self.edgeto[x] = t
					distTo[x] = distTo[t] + 1

