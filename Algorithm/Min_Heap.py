heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)
heappush(heap, 500)

# printing the value of minimum element
print("Head value of heap : "+str(heap[0]))


# printing the elements of the heap
print("The heap elements : ")
for i in heap:
	print(i, end = ' ')

print("\n")

print("Sorted min heap : ")
list_heap = []
for i in list(heap):
    element = heappop(heap)
    list_heap.append(element)

print(list_heap)


# printing the elements of the heap
#print("The heap elements : ")
#for i in heap:
#	print(i, end = ' ')
