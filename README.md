# satsolver
A simple SAT Solver.

**Question 2**

**SIMPLE SAT SOLVER**

## Specifications:

- Implemented in python 2.7
- Used lex library for tokenization
- Used Look Ahead Left – Right approach for parsing

## How to Run:

- On terminal run the following command in the project folder:

python run.py

- Type the wff using logical connectives as following:

| or | | |
| --- | --- |
| and | &amp; |
| not | ! |
| implication | -&gt; |
| iff | &lt;-&gt; |
| equivalence | &lt;=&gt; |
| parenthesis | () as required |

## Example Runs:

Note: The implementation converts the well-formed-formulas to CNF before evaluating them.

1. Contradictions:

        &gt; (p -&gt; q) &amp; (q -&gt; p) &lt;=&gt; p &lt;-&gt; !q

 CONTRADICTION!

        &gt; (p|q) &amp; (!p &amp; !q)

 CONTRADICTION!

1. Tautology:

&gt; ((p &amp; q) -&gt; r) &lt;=&gt; (p -&gt; (q -&gt; r))

=  True

        &gt; ((p &amp; q) -&gt; r) &lt;=&gt; (p -&gt; (q -&gt; r))

=  True

        &gt; p -&gt; p &lt;=&gt; 1

=  True

1. Satisfiability:

&gt; ((p | q) &amp; (p -&gt; r) &amp; (q -&gt; r)) -&gt; r

=   p,  r

=   p, !r

=   q, !p,  r

=   q, !p, !r

=  !q, !p

        &gt; !(p &amp; q) &amp; !r

        =  !q,  p, !r

=  !p, !r

&gt; (!p | !q | r) &amp; (p | !q | !r) &amp; (p | !q | r) &amp; (p | q | !r)

        =   q,  p,  r

        =  !q,  p

=  !q, !p, !r

        &gt; p -&gt; q

        =   q,  p

=  !p

        &gt; p &lt;-&gt; q

        =   q,  p

=  !q, !p
