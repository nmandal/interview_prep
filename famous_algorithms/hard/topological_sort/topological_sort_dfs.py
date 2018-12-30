# O(V+E) time | O(V+E) space
def topological_sort(jobs, deps):
    job_graph = create_job_graph(jobs, deps)
    return get_ordered_jobs(job_graph)

def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)
    # [x, y] x = prereq, y = job
    for prereq, job in deps:
        # adding edges
        graph.add_prereq(job, prereq)
    return graph

def get_ordered_jobs(graph):
    ordered_jobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        has_cycle = depth_first_traverse(node, ordered_jobs)
        if has_cycle:
            return []
    return ordered_jobs

def depth_first_traverse(node, ordered_jobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereq_node in node.prereqs:
        has_cycle = depth_first_traverse(prereq_node, ordered_jobs)
        if has_cycle:
            return True
    node.visited = True
    node.visiting = False
    ordered_jobs.append(node.job)
    return False
        
class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)
            
    def add_prereq(self, job, prereq):
        job_node = self.get_node(job)
        prereq_node = self.get_node(prereq)
        job_node.prereqs.append(prereq_node)
        
    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])
        
    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]
        
class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False
