[
"seq",
    ["set", "ex1", "Example: Dict_create and set:"],
    ["print", ["get", "ex1"]],
    ["set", "my_dict", ["dict_create"]],
    ["dict_set", ["get","my_dict"], "key1", 100],
    ["print", ["get", "my_dict"]],

    ["set", "ex5", "Example: get dict key1:"],
    ["print", ["get", "ex5"]],
    ["print", ["dict_get", ["get", "my_dict"], "key1"]],

    ["set", "ex2", "Example: Dict_Merge:"],
    ["print", ["get", "ex2"]],
    ["set", "other_dict", ["dict_create"]],
    ["dict_set", ["get","other_dict"], "key2", 300],
    ["print", ["get", "other_dict"]],
    ["set", "merged_dict", ["dict_merge", ["get", "my_dict"], ["get","other_dict"]]],
    ["print", ["get", "merged_dict"]],

    ["set", "ex3", "Example: Create and set Array:"],
    ["print", ["get", "ex3"]],
    ["set", "array", ["array_create", 5]],
    ["array_set", ["get", "array"], 0, 2],
    ["array_set", ["get", "array"], 1, 3],
    ["array_set", ["get", "array"], 2, 4],
    ["array_set", ["get", "array"], 3, 5],
    ["array_set", ["get", "array"], 4, 6],
    ["print", ["get", "array"]],

    ["set", "ex4", "Example: get Array at a[3]:"],
    ["print", ["get", "ex4"]],
    ["print", ["array_get", ["get", "array"], 3]],

    ["set", "ex6", "Example: Multiply"],
    ["print", ["get", "ex6"]],
    ["set", "a", 2],
    ["set", "b", 5],
    ["print", ["get", "a"]],
    ["print", ["get", "b"]],
    ["print", ["multiplication", ["get", "a"], ["get", "b"]]],


    ["set", "ex7", "Example: Division"],
    ["print", ["get", "ex7"]],
    ["print", ["get", "a"]],
    ["print", ["get", "b"]],
    ["print", ["division", ["get", "a"], ["get", "b"]]],

    ["set", "ex8", "Example: Power"],
    ["print", ["get", "ex8"]],
    ["print", ["get", "b"]],
    ["print", ["get", "a"]],
    ["print", ["power", ["get", "b"], ["get", "a"]]],

    ["set", "ex9", "Example: While"],
    ["print", ["get", "ex9"]],
    ["set", "counter", 1],
    ["while", ["leq", ["get", "counter"], 5],
        ["seq",
            ["print", ["get", "counter"]],
            ["set", "counter", ["add", ["get", "counter"], 1]]
        ]
    ],

    ["set", "ex10", "Print and the rest are used throughout the program. I consider them as examples."],
    ["print", ["get", "ex10"]]
]