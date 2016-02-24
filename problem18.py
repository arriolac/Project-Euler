from commons import Node

input_str = (
    "75,"
    "95 64,"
    "17 47 82,"
    "18 35 87 10,"
    "20 04 82 47 65,"
    "19 01 23 75 03 34,"
    "88 02 77 73 07 63 67,"
    "99 65 04 28 06 16 70 92,"
    "41 41 26 56 83 40 80 70 33,"
    "41 48 72 33 47 32 37 16 94 29,"
    "53 71 44 65 25 43 91 52 97 51 14,"
    "70 11 33 28 77 73 17 78 39 68 17 57,"
    "91 71 52 38 17 14 91 43 58 50 27 29 48,"
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31,"
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
)

def main():

    # Convert to int 2D matrix
    rows = [
        [int(val) for val in row.split(" ")]
        for row in input_str.split(",")
    ]

    # Create tree where root is rows[0][0]
    num_rows = len(rows)

    for i in range(0, num_rows):

        # Get rows
        curr_row_index = num_rows - 1 - i
        curr_row = rows[curr_row_index]

        if curr_row_index != num_rows - 1:
            row_below = rows[curr_row_index + 1]
        else:
            row_below = None

        # Iterate through columns
        for j in range(0, len(curr_row)):
            left_node = None
            right_node = None
            if row_below is not None:
                left_node = row_below[j]
                right_node = row_below[j + 1]

            val = curr_row[j]
            curr_row[j] = Node(val, left_node=left_node, right_node=right_node)

    # Get root, recurse
    root = rows[0][0]
    return max_value(root)

def max_value(node):
    if node.left_node is None and node.right_node is None:
        return node.val
    else:
        return max(max_value(node.left_node), max_value(node.right_node)) + node.val

if __name__ == '__main__':
    print main()
