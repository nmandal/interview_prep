General Tips
- Clarify any assumptions you made subconsciously. Many questions are under-specified on purpose.
- Always validate input first. Check for invalid/empty/negative/different type input. Never assume you are given valid parameters. Alternatively, clarify with the interviewer whether you can assume valid input (usually yes), which can save you some time from writing code that does input validation.
- Are there any time/space complexity requirements/constraints?
- Check for off-by-one errors.
- In languages where there are no automatic type coercion, check that concatenation of values are of the same type int, str, list.
- After finishing your code, use a few example inputs to test your solution.
- Is the algorithm meant to be run multiple times, for example in a web server? If yes, the input is likely to be preprocessable to improve the efficiency in each call.
- Generally, to improve the speed of a program, we can either (1) choose a more appropriate data structure/algorithm; or (2) use more memory. The latter demonstrates a classic space vs. time tradeoff, but is not necessarily the case that you can achieve better speed at the expense of space. Also, note that there is often a theoretical limit to how fast your program can run (in terms of time complexity). For instance, a question that requires you to find the smallest/largest element in an unsorted array cannot run faster than O(N).
- Data structures are your weapons. Choosing the right weapon for the right battle is the key to victory. Be very familiar about the strengths

Tricks for Data Structures and Algorithms:

Arrays:
- Fast access for element at an index, slow lookups (unless sorted) and insertions. Be comfortable with notions of iteration, resizing, partitioning, merging, etc.
- Often have simple brute-force solutions that use O(n) space, but there are subtler solutions that **use the array itself** to **reduce space** complexity to O(1).
- Filling an array from the front is slow, so see if it's possible to **write values from the back**.
- Instead of deleting an entry (which requires moving all entries to the right), consider **overwriting**.
- When dealing with integers encoded by an array consider **processing the digits from the back** of the array. Alternatively, reverse the array so the **least-significant digit is the first entry.**.
- Be comfortable with writing code that operates on **subarrays**.
- It's incredibly easy to make **off-by-1** errors when operating on arrays - reading past the last element of an array is a common error which has catastrophic consequences.
- Don't worry about preserving the **integrity** of the array (sortedness, keeping equal entries together, etc.) until it's time to return.
- An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a **subset** of {{0,1,...,W-1}}. (When using a Boolean array to represent a subset of {{1,2,3,...,n}}, allocate an array of size n+1 to simplify indexing).
- When operating on 2D arrays, **use parallel logic** for rows and columns.
- Sometimes it's easier to **simulate the specification** than to analytically solve for the result. For example, rather than writing a formula for the i-th entry in the spiral order for an n x n matrix, just compute the output from the beginning.

- Is the array sorted or partially sorted? If it is, some form of binary search should be possible. This also usually means that the interviewer is looking for a solution that is faster than O(n).
- Can you sort the array? Sometimes sorting the array first may significantly simplify the problem. Make sure that the order of array elements do nto beed to be preserved before attempting a sort.
- For questions where summation or multiplication of a subarray is involved, pre-computation using hashing or a prefix/suffix sum/product might be useful.
- If you are given a sequence and the interviewer asks for O(1) space, it might be possible to use the array itself as a hash table. For example, if the array has only values from 1 to N, where N is the length of the array, negate the value at that index (minus one) to indicate presence of that number.

Strings:
- Know how strings are represented in memory. Understand basic operators such as comparison, copying, matching, joining, splitting, etc.
- Similar to arrays, string problems often have simple brute-force solutions that use O(n) space solution, but subtler solutions that use the string itself to **reduce space complexity** to O(1).
- Understand the implications of a string type which is **immutable**, e.g., the need to allocate a new string when concatenating immutable strings. **alternatives** to immutable strings, e.g. a list in Python.
- Updating a mutable string from the front is slow, so see if it's possible to **write values from the back**.

Linked Lists:
- Understand trade-offs with respect to arrays. Be comfortable with iteration, insertion, and deletion within singly and doubly linked lists. Know how to implement a list with dynamic allocation and with arrays.
- List problems often have a simple brute-force solution that uses O(n) space, but a subtler solution that uses the **existing list nodes** to reduce space complexity to O(1).
- Very often, a problem on lists is conceptually simple, and is more about **cleanly coding what is specified**, rather than designing an algorithm.
- Consider using a **dummy head** (sometimes referred to as a sentinel) to avoid having to check for empty lists. This simplifies code, and makes bugs less likely.
- It's easy to forget to **update next** (and previous pointers in doubly linked list) for the head and tail.
- Algorithms operating on singly linked lists often benefit from using **two iterators**,  one ahead of the other, or advancing quicker than the other.

Stacks and Queues:
- Recognize where LIFO (stack) and FIFO (queue) semantics are applicable. Know array and linked list implementations.
- Stacks:
    - Learn to recognize when the stack LIFO property is **applicable**. For example, **parsing and reversing** typically benefit from a stack.
    - Consider augmenting the basic stack and queue data structure to support additional operations such as finding the maximum element.
- Queues:
    - Learn to recognize when the queue FIFO property is applicable. For example, queues are ideal when order needs to be preserved.

Binary Trees:
- Use for representing hierarchical data. Know about depth, height, leaves, search path, traversal sequences, successor/predecessor operations.
- **Recursive algorithms** are well-suited to problems on trees. Remember to include space implicitly allocated on the **function call stack** when doing space complexity analysis.
- Some tree problems have simple brute-force solutions that use O(n) space solution, but subtler solutions that uses the **existing tree nodes** to reduce space complexity to O(1).
- Consider **left- and right-skewed trees** when doing complexity analysis. Note that O(h) complexity, where h is the tree height, translates into O(log n) complexity for balanced trees, but O(n) complexity on skewed trees.
- If each node has a **parent field**, use it to make your code simpler, and to reduce time and space complexity.
- It's easy to make the **mistake** of treating a node that has a **single child** as a leaf.

Heaps:
- Key benefit: O(1) lookup find-max, O(log n) insertion, and O(log n) deletion of max. Node and array representations. Min-heap variant.
- Use a heap when **all you care about** is the **largest** or **smallest** elements, and you **do not need** to support fast lookup, delete, or search operations for arbitrary elements.
A heap is a good choice when you need to compute the k **largest** or k **smallest** elements in a collection. For the former, use a min-heap, for the latter, use a max-heap/

Searching:
- **Binary search** is an effective search tool. It is applicable to more than use searching in **sorted arrays**, e.g., it can be used to search an **interval of real numbers or integers**.
- If your solution uses sorting, and the computation performed after sorting is faster than sorting, e.g., O(n) or O(log n), **look for solutions that do not perform a complete sort**.
- Consider **time/space tradeoffs**, such as making multiple passes through the data.

Hash Tables:
- Key benefit: O(1) insertions, deletions, and lookups. Key disadvantages: not suitable for order-related queries; need for resizing; poor worst-case performance. Understand implementation using array of buckets and collision chains. Know hash functions for integers, strings, and objects.
- Hash tables have the **best theoretical and real-world performance** for lookup, insert, and delete. Each of these operations has O(1) time complexity. The O(1) time complexity for insertion is for the average case -a single insert can take O(n) if the hash table has to be resized.
- Consider using a hash code as a **signature** to enhance performance, e.g., to filter out candidates.
- Consider using a precomputed lookup `table` instead of boilerplate if-then code for mappings, e.g., from character to value, or character to character.
- When defining your own type that will be put in a hash table, be sure you understand the relationship between **logical equality** and the fields the hash function must inspect. Specifically, anytime equality is implemented, it is imperative that the correct hash function is also implemented, otherwise when objects are placed in hash tables, logically equivalent objects may appear in different buckets, leading to lookups returning false, even when the searched item is present.
- Sometimes, you'll need a `multimap` i.e., a map that contains multiple values for a single key, or a bi-directional map. If the language's standard libraries do not provide the functionality you need, learn how to implement a multimap using a list of values, or find a **third party library** that has a multimap. 
Sorting:
- Undercover some structure by sorting the input.
- Sorting problems come in two flavors: (1.) **use sorting to make subsequent steps in an algorithm simpler**, and (2.) design a **custom sorting routine**. For the former, it's fine to use a library sort function, possibly with a custom comparator. For the latter, use a data structure like a BST, heap, or array indexed by values.
- Certain problems become easier to understand, as well as solve, when the input is sorted. The most natural reason to sort is if the inputs have a **natural ordering**, and sorting can be used as a preprocessing step to **speed up searching**.
- For **specialized input**, e.g., a very small range of values, or a small number of values, it's possible to sort in O(n) time rather than O(n log n) time.
- It's often the case that sorting can be implemented in **less space** than required by a brute force approach.
- Sometimes it is not obvious what to sort on, e.g., should a collection of intervals be sorted on starting points or endpoints.

Binary Search Trees:
- Key benefit: O(log n) insertions, deletions, lookups, find-min, find-max, successor, predecessor when tree is height-balanced. Understand node fields, pointer implementation. Be familiar with the notion of balance, and operations maintaining balance.
- With a BST you can **iterate** through elements in **sorted order** in time O(n) (regardless of whether it is balanced).
- Some problems need a **combination of a BST and a hash table**. For example, if you insert student objects in a BST and entries are ordered by GPA, and then a student's GPA needs to be updated and all we have is the student's name and new GPA, we cannot find the student by name without full traversal. However, with an additional hash table, we can directly go to the corresponding entry in the tree.
- Sometimes, it's necessary to **augment** a BST to make it possible to manipulate more complicated data, e.g., intervals, and efficiently support more complex queries, e.g., the number of elements in a range.
- The BST property is a **global property** - a binary tree may have the property that each node's key is greater than the key at its left child and smaller than the key at its right child, but it may not be a BST.

Recursion:
- If the structure of the input is defined in a recursive manner, design a recursive algorithm that follows the input definition.
- Recursion is especially suitable when the **input is expressed using recursive rules** such as compute grammar.
- Recursion is a good choice for **search, enumeration, and divide-and-conquer**.
- Use recursion as **alternative to deeply nested iteration** loops. For example, recursion is much better when you have an undefined number of levels, such as the IP address problem generalized to k substrings.
- If you are asked to **remove recursion** from a program, consider mimicking call stack with the **stack data structure**.
- Recursion can be easily removed from a **tail-recursive** program by using a while loop - no stack is needed. (Optimizing compilers do this.)
- If a recursive function may end up being called with the **same arguments** more than once, **cache** the results - this is the idea behind Dynamic Programming.

Dynamic Programming:
- Compute the solutions for smaller instances of a given problem and use these solutions to construct a solution to the problem. Cache for performance.
- Consider using DP whenever you have to **make choices** to arrive at the solution. Specifically, DP is applicable when you can construct a solution to the given instance from solutions to subinstances of smaller problems of the same kind.
- In addition to optimization problems, DP is also **applicable** to **counting and decision problems** - any problem where you can express a solution recursively in terms of the same computation on smaller instances.
- Although conceptually DP involves recursion, often for efficiency the cache is **built "bottom-up**, i.e., iteratively.
- When DP is implemented recursively the cache is typically a dynamic data structure such as a hash table or a BST; when it is implemented iteratively the cache is usually a one- or multi-dimensional array.
- To save space, **cache space** may be **recycled** once it is known that a set of entries will not be looked up again.
- Sometimes **recursion may out-perform a bottom-up DP** solution, e.g., when the solution is found early or subproblems can be **pruned** through bounding.
- A common **mistake** in solving DP problems is trying to think of the recursive case by splitting the problem into **two equal halves**, a la quicksort, i.e. solve the subproblems for subarrays and combine the result. However, in most cases, these two subproblems are not sufficient to solve the original problem.
- DP is based on **combining solutions** to subproblems to **yield a solution** to the original problem. However, for some problems, DP will not work. For example, if you need to compute the longest path from City 1 to City 2 without repeating an intermediate city, and this longest path passes through City 3, then the subpaths from City 1 to City 3 and City 3 to City 2 may not be individually longest paths without repeated cities.

Greedy Algorithms and Invariants:
- Greedy: Compute a solution in stages, making choices that are locally optimum at step; these choices are never undone.
- Invariants: Identify an invariant and use it to rule out potential solutions that are suboptimal/dominated by other solutions.
- A greedy algorithm is often the right choice for an **optimization problem** where there's a natural set of **choices to select from**.
- It's often easier to conceptualize a greedy algorithm recursively, and then **implement** it using iteration for higher performance.
- Even if the greedy approach does not yield an optimum solution, it can give insights into the optimum algorithm, or serve as a heuristic.
- Sometimes the greedy algorithm is **not obvious**.

Graphs:
- Describe an algorithm using a graph and solve it using an existing graph algorithm.
- It's natural to use a graph when the problem involves **spatially connected** objects, e.g., road segments between cities.
- **More generally**, consider using a graph when you need to analyze **any binary relationship**, between objects, such as interlinked webpages, followers in a social graph, etc. In such cases, quite often the problem can be reduced to a well-known graph problem.
- Some graph problems entail **analyzing structure** e.g., looking for cycles or connected components. **DFS** works particularly well for these applications.
- Some graph problems are related to **optimization**, e.g., find the shortest path from one vertex to another. **BFS, Dijkstra's shortest path algorithm, and minimum spanning tree** are examples of graph algorithms appropriate for optimization problems.

