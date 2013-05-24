Solution to Problem #126 - Real-World Merge Sort
================================================

[original problem](http://www.reddit.com/r/dailyprogrammer/comments/1epasu/052013_challenge_126_easy_realworld_merge_sort/)

My original solution ran in O(n^2) time and used a linear search to insert the contents of line A into line B. See slow() for the original implementation.

After looking at the other solutions, this [post by regul](http://www.reddit.com/r/dailyprogrammer/comments/1epasu/052013_challenge_126_easy_realworld_merge_sort/ca2oz40) improved on my solution by using a binary search to determine where to insert the new elements into list B. I decided to implement the binary search into my own solution, but decided not to post it as it was too similar to regul's original post.
