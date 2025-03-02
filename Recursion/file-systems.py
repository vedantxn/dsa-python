import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)                       # account for direct usage
    if os.path.isdir(path):                              # if this is a directory,
        for filename in os.listdir(path):                # then for each child:
            childpath = os.path.join(path, filename)      # compose full path to child
            total += disk_usage(childpath)               # add child’s usage to total

    print('{0:<7}'.format(total), path)                  # descriptive output (optional)
    return total 

#recursion trace
'''
 /user/rt/courses/cs016/grades
 /user/rt/courses/cs016/homeworks/hw1
 /user/rt/courses/cs016/homeworks/hw2
 /user/rt/courses/cs016/homeworks/hw3
 /user/rt/courses/cs016/homeworks
 /user/rt/courses/cs016/programs/pr1
 /user/rt/courses/cs016/programs/pr2
 /user/rt/courses/cs016/programs/pr3
 /user/rt/courses/cs016/programs
 /user/rt/courses/cs016
 /user/rt/courses/cs252/projects/papers/buylow
 /user/rt/courses/cs252/projects/papers/sellhigh
 /user/rt/courses/cs252/projects/papers
 /user/rt/courses/cs252/projects/demos/market
 /user/rt/courses/cs252/projects/demos
 /user/rt/courses/cs252/projects

 /user/rt/courses/cs252/grades
 /user/rt/courses/cs252
 /user/rt/courses/
'''