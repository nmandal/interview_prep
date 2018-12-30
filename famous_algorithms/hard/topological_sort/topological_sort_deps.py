# O(V+E) time | O(V+E) space
def topological_sort(jobs, deps):
    job_graph = create_job_graph(jobs, deps)
    return get_ordered_jobs(job_graph)

def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)
    # [x, y] x = job, y = dep
    for job, dep in deps:
        # adding edges
        graph.add_dep(job, dep)
    return graph

def get_ordered_jobs(graph):
    ordered_jobs = []
    no_prereqs = list(filter(lambda node: node.num_prereqs == 0, graph.nodes))
    while len(no_prereqs):
        node = no_prereqs.pop()
        ordered_jobs.append(node.job)
        remove_deps(node, no_prereqs)
    graph_has_edges = any(node.num_prereqs for node in graph.nodes)
    return [] if graph_has_edges else ordered_jobs

def remove_deps(node, no_prereqs):
    while len(node.deps):
        dep = node.deps.pop()
        dep.num_prereqs -= 1
        if dep.num_prereqs == 0:
            no_prereqs.append(dep)
        

class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)
            
    def add_dep(self, job, dep):
        job_node = self.get_node(job)
        dep_node = self.get_node(dep)
        job_node.deps.append(dep_node)
        dep_node.num_prereqs += 1
        
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
        self.deps = []
        self.num_prereqs = 0
