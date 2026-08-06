"""
list (Python Lists) - Revision Script
Run: python3 list_revision.py

Covers list methods:
- append
- extend
- insert
- remove
- pop
- clear
- index
- count
- sort
- reverse
- copy

Also covers common list operations (not methods):
- len, in, del
- slicing, slice assignment
- sorted (returns new list)
- min/max/sum (numbers)

Tip: Lists are mutable (methods often modify the same list in-place).
"""

from typing import Any, List


def title(text: str) -> None:
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)


def show(lst: List[Any], label: str = "list") -> None:
    """Helper: print list nicely with id (to see in-place changes)."""
    print(f"{label}: {lst}  (id={id(lst)})")


def demo_append():
    title("1) append(x) -> add ONE item at the end (in-place)")
    lst = ["apple", "banana"]
    show(lst, "before")
    lst.append("cherry")
    show(lst, "after ")


def demo_extend():
    title("2) extend(iterable) -> add MANY items at the end (in-place)")
    lst = ["apple", "banana"]
    show(lst, "before")
    lst.extend(["cherry", "mango"])
    show(lst, "after ")
    # extend works with any iterable:
    lst.extend("XY")
    show(lst, "after extend('XY')")


def demo_insert():
    title("3) insert(index, x) -> insert at a specific position (in-place)")
    lst = ["apple", "cherry"]
    show(lst, "before")
    lst.insert(1, "banana")
    show(lst, "after ")


def demo_remove():
    title("4) remove(x) -> remove FIRST occurrence of value (in-place)")
    lst = ["apple", "banana", "banana", "cherry"]
    show(lst, "before")
    lst.remove("banana")
    show(lst, "after ")
    # If value not found -> ValueError (so often check with 'in')
    # if "orange" in lst:
    #     lst.remove("orange")


def demo_pop():
    title("5) pop([i]) -> remove and RETURN item (in-place)")
    lst = ["apple", "banana", "cherry"]
    show(lst, "before")

    last = lst.pop()
    print("popped (default last):", last)
    show(lst, "after pop()")

    first = lst.pop(0)
    print("popped index 0:", first)
    show(lst, "after pop(0)")


def demo_clear():
    title("6) clear() -> remove ALL items (in-place)")
    lst = ["apple", "banana"]
    show(lst, "before")
    lst.clear()
    show(lst, "after ")


def demo_index():
    title("7) index(x[, start[, end]]) -> find position of value")
    lst = ["apple", "banana", "cherry", "banana"]
    show(lst)

    print("index('banana'):", lst.index("banana"))
    print("index('banana', 2):", lst.index("banana", 2))  # start searching from index 2


def demo_count():
    title("8) count(x) -> count how many times value appears")
    lst = ["apple", "banana", "banana", "cherry"]
    show(lst)
    print("count('banana'):", lst.count("banana"))
    print("count('orange'):", lst.count("orange"))


def demo_sort():
    title("9) sort(key=None, reverse=False) -> sort IN PLACE")
    nums = [3, 1, 10, 2]
    show(nums, "before nums")
    nums.sort()
    show(nums, "after  nums.sort()")

    words = ["Banana", "apple", "cherry"]
    show(words, "before words")
    words.sort()
    show(words, "after  words.sort() (case-sensitive)")

    words2 = ["Banana", "apple", "cherry"]
    show(words2, "before words2")
    words2.sort(key=str.lower)
    show(words2, "after  words2.sort(key=str.lower)")

    nums2 = [3, 1, 10, 2]
    show(nums2, "before nums2")
    nums2.sort(reverse=True)
    show(nums2, "after  nums2.sort(reverse=True)")


def demo_reverse():
    title("10) reverse() -> reverse list IN PLACE")
    lst = [1, 2, 3, 4]
    show(lst, "before")
    lst.reverse()
    show(lst, "after ")


def demo_copy():
    title("11) copy() -> shallow copy (new list object)")
    lst = [["a"], ["b"]]
    c = lst.copy()
    show(lst, "original")
    show(c, "copy    ")

    print("Same object?", lst is c)
    print("Inner object same?", lst[0] is c[0], "(shallow copy shares inner lists!)")

    # Modify inner list affects both
    lst[0].append("X")
    show(lst, "original after inner change")
    show(c, "copy after inner change")


def demo_len_in():
    title("12) Common operations: len(), 'in', iteration")
    lst = ["apple", "banana", "cherry"]
    show(lst)

    print("len(lst):", len(lst))
    print("'banana' in lst:", "banana" in lst)

    print("loop:")
    for item in lst:
        print("-", item)


def demo_del():
    title("13) del -> delete by index or slice (in-place)")
    lst = ["a", "b", "c", "d", "e"]
    show(lst, "before")
    del lst[1]         # delete one item
    show(lst, "after del lst[1]")
    del lst[1:3]       # delete slice
    show(lst, "after del lst[1:3]")


def demo_slicing():
    title("14) Slicing -> creates a NEW list (not in-place)")
    lst = ["a", "b", "c", "d", "e"]
    show(lst, "original")

    part = lst[1:4]
    show(part, "slice [1:4]")

    every_2 = lst[::2]
    show(every_2, "slice [::2]")


def demo_slice_assignment():
    title("15) Slice assignment -> replace/remove/insert chunks (in-place)")
    lst = ["a", "b", "c", "d", "e"]
    show(lst, "before")

    # Replace slice
    lst[1:3] = ["X", "Y"]
    show(lst, "after replace lst[1:3]=['X','Y']")

    # Insert without removing (empty slice)
    lst[2:2] = ["INSERTED"]
    show(lst, "after insert lst[2:2]=['INSERTED']")

    # Remove slice by assigning empty list
    lst[1:4] = []
    show(lst, "after remove lst[1:4]=[]")


def demo_sorted_vs_sort():
    title("16) sorted(list) vs list.sort()")
    lst = [3, 1, 10, 2]
    show(lst, "original")

    new_lst = sorted(lst)  # returns new list
    show(new_lst, "sorted(lst) result")
    show(lst, "original after sorted(lst) (unchanged)")

    lst.sort()  # in-place
    show(lst, "after lst.sort() (changed)")


def demo_min_max_sum():
    title("17) min(), max(), sum() (numbers)")
    nums = [3, 1, 10, 2]
    show(nums)
    print("min:", min(nums))
    print("max:", max(nums))
    print("sum:", sum(nums))


def demo_common_patterns():
    title("18) Useful patterns (quick reference)")

    # Build a new list with comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print("comprehension:", newlist)

    # Safe remove pattern
    lst = ["a", "b", "c"]
    target = "x"
    print("\nSafe remove:")
    if target in lst:
        lst.remove(target)
    else:
        print(f"{target!r} not found; nothing removed")

    # Enumerate
    print("\nEnumerate:")
    for i, item in enumerate(["x", "y", "z"], start=1):
        print(i, item)


def main():
    demo_append()
    demo_extend()
    demo_insert()
    demo_remove()
    demo_pop()
    demo_clear()
    demo_index()
    demo_count()
    demo_sort()
    demo_reverse()
    demo_copy()
    demo_len_in()
    demo_del()
    demo_slicing()
    demo_slice_assignment()
    demo_sorted_vs_sort()
    demo_min_max_sum()
    demo_common_patterns()

    title("DONE ✅")
    print("Tip: Edit lists and re-run to practice.")


if __name__ == "__main__":
    main()