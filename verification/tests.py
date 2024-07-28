"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
    {
        "input": [{'maçã': 10, 'banana': 5}, [('maçã', 3), ('banana', 2)]],
        "answer": {'maçã': 7, 'banana': 3}
    },
    {
        "input": [{'laranja': 5}, [('laranja', 2)]],
        "answer": {'laranja': 3}
    }

    ]
}
