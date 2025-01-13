<h2>Algorithm is set of finite steps which if followed gives the solution in finite time</h2>

pillars-
inputs (single data / data set like 'n' / problem set like data structure) -most important
output (result or proper response) -most important
finiteness (fixed step/time)
effectiveness (each step should either solve the problem or get us closer to the solution)
definiteness (each step should clearly define its use and need) 

<p>Analysis is done to predict time and space complexity so as to select a particular algorithm</p>

types:
priori- done befor implementation, using pen paper
posteriori- done after implementation , using software by professionals (testors)

for efficient analysis, both best and worst case is used, but it requires time to analyze
for quick analysis, worst case is used, but it less efficient

<p><b>Asymptotic Notations</b> are units to record complexity using maths <br> eg: Big-Oh- for only worst case -simple,fast but less efficient, Theta- best+worst -avg is taken, very efficient but slow, Omega- best case only, generally not used </p>

f(n): input rate, amount of input
g(n): optpur rate, amount of steps to get output

for(i=0;i<=n;i++)
 print(i)

for n=4,
i=0 : 1
i<=n : 0,1,2,3,4,5    n+2
i++ : 1,2,3,4,5       n+1
print() : 0,1,2,3,4   n+1

total : 1 + n+2 + n+1 + n+1 = 3n+5

Big-Oh :
constants have no value
in addition use max(worst) only [n n square n cube   n cube is considered]
in nesting, mutliply and then addition rule


<p> <strong>first sorting then searching so that searching is efficient</strong> </p>

<h2>pseudo code:</h2>
read-input
write-output

<h2>.sorted()</h2> uses bubble sort


types of algorithm:
1. divide and conquer (merge ans quick sort)
2. greedy algorithm (about optimisation | optimisation is minimisation of cost if given/buy, optimisation is maximization  profit when taken/sell) eg.:Dijsktra shortest path algorithm (we know everything from start to end)
3. Dynamic Programming (Solve problem as it comes, have optimisation) eg.: Floyd warshal's (we don't know everything about the whole problem)
4. Backtracking (only solutions needed, may or may not have optimisation) eg.: N-queens problem (arrange N queens on NxN chessboard such that no queens attacks each other) .... always asked ..... minimum size can be 4x4 
5. Branch n Bound (state space search, decision tree, calculate all possible solutions) eg.: Travelling Salesman Problem 

technical interviews:
1. syntax should be ready and remembered
2. should khow many languages or ready to work on many languages
3. for cracking interview, prepare only in single language

online - MCQ( apti + technical)
online - coding on platform
online/offline round 2 - coding
final interview- HR + Tech 