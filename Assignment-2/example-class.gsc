[
    "seq",
        ["set", "Shape", ["dict_create"]],
        ["dict_set", ["get", "Shape"], "density", "shape_density"],
        ["dict_set", ["get", "Shape"], "_classname", "Shape"],
        ["dict_set", ["get", "Shape"], "_parent", "None"],
        ["dict_set", ["get", "Shape"], "_new", "shape_new"],

        ["set", "Square", ["dict_create"]],
        ["dict_set", ["get", "Square"], "area", "square_area"],
        ["dict_set", ["get", "Square"], "_classname", "Square"],
        ["dict_set", ["get", "Square"], "_parent", "Shape"],
        ["dict_set", ["get", "Square"], "_new", "square_new"],

        ["set", "Circle", ["dict_create"]],
        ["dict_set", ["get", "Circle"], "area", "circle_area"],
        ["dict_set", ["get", "Circle"], "_classname", "Circle"],
        ["dict_set", ["get", "Circle"], "_parent", "Shape"],
        ["dict_set", ["get", "Circle"], "_new", "circle_new"],

        ["set", "sq", ["make", "Square", "sq", "3"]],

        ["set", "ci", ["make", "Circle", "ci", "2"]],

        ["print", ["add", ["ccall", "sq", "density", "5"], ["ccall", "ci", "density", "5"]]]
]