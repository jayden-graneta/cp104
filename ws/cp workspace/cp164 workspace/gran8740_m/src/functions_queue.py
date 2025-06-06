"""
-------------------------------------------------------
Queue Functions
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2024-06-12"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from Queue_array import Queue


def threads_weave(threads):
    """
    -------------------------------------------------------
    Combines multiple Queues into one Queue where the multiple Queue
    values are interwoven into the returned Queue. Values are removed
    from each Queue in threads.
    Use: singleton = threads_weave(threads)
    -------------------------------------------------------
    Parameters:
        threads - a list of Queues to process (list of Queue)
    Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
        singleton - a Queue (Queue)
    -------------------------------------------------------
    """

    # your code here
    singleton = Queue()

    for x in threads:
        for i in threads[x]:
            singleton.append(threads[x].pop())

    return singleton


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source, meaning moving its contents
    from the front to the rear n times.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
        None
    -------------------------------------------------------
    """

    # your code here
    for x in range(n):
        source.insert(0, source.pop())
    return
