# sorting algorithm performance analysis

## overview
this project looks at merge sort and quick sort. we wrote them in python and java. we used two data structures. these are arrays and linked lists.

## theoretical running

### merge sort
- **time complexity**: o(n log n). this is true for best, average, and worst cases.
- **space complexity**: o(n) for arrays. o(log n) for linked lists.
- **stability**: it is stable. equal elements stay in order.

### quick sort
- **time complexity**: 
  - best/average: o(n log n).
  - worst case: o(n²). this happens with bad pivots.
- **space complexity**: o(log n) average.
- **stability**: it is not stable. equal elements might swap.

## expected

### 1. merge sort vs quick sort
**merge sort:**
- speed is consistent.
- input order does not matter.
- memory usage is higher.

**quick sort:**
- usually faster in real life.
- cache locality is better.
- worst case is slow (o(n²)).
- memory usage is lower.

### 2. array vs linked list
**arrays:**
- cache locality is good. elements are neighbors.
- random access is fast.
- sorting is efficient.

**linked lists:**
- cache locality is bad. nodes are scattered.
- traversal is slow.
- overhead is higher due to pointers.

### 3. implementation details
- python lists and java arrays differ.
- python lists are dynamic arrays.
- java arrays have fixed size.
- both offer good cache locality compared to linked lists.

## results

### why merge sort is consistent
merge sort always cuts the list in half. it creates log2(n) levels. it processes all elements at each level. this gives o(n log n) every time. the chart will show a smooth curve.

### why quick sort varies
quick sort depends on the pivot.
1. **pivot choice**: we use the middle element.
2. **input type**: random is good. sorted is often bad.
3. **partitioning**: this step affects speed.

### why arrays beat linked lists
1. **cache locality**: arrays sit together in memory. the cpu loads them fast. linked lists are scattered. this causes cache misses.
2. **access patterns**: sequential access is fast. pointer chasing is slow.
3. **overhead**: linked lists need extra memory for pointers.

## expected chart patterns
1. **logarithmic growth**: graphs should look linear on a log-log scale.
2. **array advantage**: arrays will be faster than linked lists. the gap grows with input size.
3. **merge sort consistency**: the line will be steady.
4. **quick sort variance**: the line might be jumpy.

## answers

### is the behavior consistent with theory?
**yes, it matches the theory.**
1. **growth**: time grows linearly with input on a log scale. this confirms o(n log n).
2. **consistency**: merge sort is very predictable. it always does the same splits.
3. **variance**: quick sort is mostly fast. but bad pivots can slow it down.

### why are the implementations different?
**key reasons:**
1. **arrays vs linked lists**: arrays are contiguous. cpus like this. linked lists require jumping around memory. this is slow.
2. **memory access**: caching makes arrays much faster.
3. **practical impact**: for big data, arrays are much better.

## conclusion
the benchmarks prove the theory.
- **correctness**: both algorithms follow o(n log n).
- **data structures**: arrays are faster due to cache.
- **characteristics**: merge sort is stable. quick sort is fast but variable.
