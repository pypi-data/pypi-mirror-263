import lark


class KnowledgeGraph:
    def _validate_triple(self, triple):
        if not isinstance(triple, tuple):
            raise ValueError("Triple must be a tuple")
        if len(triple) != 3:
            raise ValueError("Triple must have exactly 3 elements")

    def __init__(self):
        self.index_by_connection = {}
        self.reverse_index_by_connection = {}

    def add_node(self, triple):
        item = triple[0]
        relates_to = triple[1]
        value = triple[2]

        self._validate_triple(triple)

        if isinstance(value, list):
            for val in value:
                if val not in self.reverse_index_by_connection:
                    self.reverse_index_by_connection[val] = {}

                if relates_to not in self.reverse_index_by_connection[val]:
                    self.reverse_index_by_connection[val][relates_to] = []

                self.reverse_index_by_connection[val][relates_to].append(item)

                self.reverse_index_by_connection[val][relates_to] = list(
                    set(self.reverse_index_by_connection[val][relates_to])
                )
        else:
            if value not in self.reverse_index_by_connection:
                self.reverse_index_by_connection[value] = {}

            if relates_to not in self.reverse_index_by_connection[value]:
                self.reverse_index_by_connection[value][relates_to] = []

            self.reverse_index_by_connection[value][relates_to].append(item)

            if item not in self.reverse_index_by_connection:
                self.reverse_index_by_connection[item] = {}

            if relates_to not in self.reverse_index_by_connection[item]:
                self.reverse_index_by_connection[item][relates_to] = []

            self.reverse_index_by_connection[item][relates_to].append(value)

            self.reverse_index_by_connection[value][relates_to] = list(
                set(self.reverse_index_by_connection[value][relates_to])
            )

    def get_nodes(self, item):
        return self.reverse_index_by_connection.get(item, {})

    def get_nodes_by_connection(self, item, connection):
        result = self.reverse_index_by_connection.get(item, {}).get(
            connection, {}
        ) or self.reverse_index_by_connection.get(item, {})
        return list(set(result))

    def get_connection_count(self, item):
        return len(self.index_by_connection.get(item, {}))
    
    def get_connection_paths(self, item1, item2):
        paths = []
        current_node = item1
        visited = set()

        def dfs(node, path):
            if node == item2:
                print("Found path", path)
                paths.append(path)
                return

            visited.add(node)
            print("Visiting", node)

            for connection in self.get_nodes(node):
                for c in self.get_nodes(node)[connection]:
                    if c in visited:
                        continue

                    dfs(c, path + [(c, connection)])
                    
                if connection in visited:
                    continue

                dfs(connection, path + [connection])

        dfs(current_node, [current_node])

        # return shortest path
        shortest_path = min(paths, key=len)

        # print as -> statements
        print(shortest_path[0], end="")

        for i in range(1, len(shortest_path)):
            print(" ->", shortest_path[i][1], "->", shortest_path[i][0], end="")

        print()

        return shortest_path

# Tracy -> WorksFor -> Citations -> Developer -> EntityType!

kg = KnowledgeGraph()

entities = [
    {
        "Entity": "Train 1.0",
        "Developer": "Roboflow",
        "Task type": "object detection, image segmentation",
        "Release date": "January 10, 2023",
    },
    {
        "Entity": "MetaCLIP",
        "Developer": "Meta AI",
        "Task type": "classification",
        "Release date": "January 11, 2023",
    },
    {
        "Entity": "Train 2.0",
        "Developer": "Roboflow",
        "Task type": "classification",
        "Release date": "January 11, 2023",
    },
    {"Entity": "IndieWeb", "Type": ["Community", "Events Series"]},
    {"Entity": "CLIP", "Type": "Paper", "Authors": ["Alex", "2", "3"]},
]

for entity in entities:
    # add all items
    entity_name = entity["Entity"]
    for key, value in entity.items():
        kg.add_node((entity_name, key, value))

kg.add_node(("Roboflow", "Owned", "Lenny"))
kg.add_node(("Roboflow", "Developer", "MetaCLIP"))
kg.add_node(("Roboflow", "Makes", "Computer vision software."))
kg.add_node(("Roboflow", "EntityType", "Company"))
kg.add_node(("MetaAI", "EntityType", "Company"))
kg.add_node(("Tracy", "WorksFor", "MetaAI"))
kg.add_node(("Tracy", "WorksFor", "Roboflow"))
kg.add_node(("Company", "EntityType", "Roboflow"))
kg.add_node(("James", "Birthday", "March 20th, 2024"))
kg.add_node(("James", "WorksFor", "Roboflow"))
kg.add_node(("James", "WorksFor", "PersonalWeb"))
kg.add_node(("James", "WorksFor", "IndieWeb"))
kg.add_node(("Lenny", "Birthday", "March 21th, 2024"))
kg.add_node(("Events Series", "Organizer", "IndieWeb"))
kg.add_node(("Lenny", "Enjoys", "Coffee"))
kg.add_node(("James", "Enjoys", "Coffee"))
kg.add_node(("James", "Hobbies", "Coffee"))
kg.add_node(("Alex", "Enjoys", "Coffee"))
kg.add_node(
    (
        "IndieWeb",
        "IsDescribedBy",
        "A community of individuals who create on their own personal websites",
    )
)
kg.add_node(("PersonalWeb", "IsDescribedBy", "Another community"))
kg.add_node(("Roboflow", "IsDescribedBy", "Computer vision"))
kg.add_node(
    (
        "Computer vision",
        "IsDescribedBy",
        "A field of computer science that enables computers to interpret and understand the visual world",
    )
)
kg.add_node(("Alex", "Citations", ["MetaAI", "GoogleAI", "Coffee", "Teacup", "Roboflow"]))

# create parser
# get all properties of a node
# get specific property of a node
parser = lark.Lark(
    """
start: query (operand query)*
query: "{" node ((relation | interrelation) node)* "}" (EXPAND | QUESTION | COUNT)?
operand: PLUS | INTERSECTION
PLUS: "+"
INTERSECTION: "INTERSECTION"
relation: "->"
interrelation: "<->"
EXPAND: "!"
QUESTION: "?"
COUNT: "#"
COMPARATOR: "=" | "!=" | ">" | "<"
CNAME: /[a-zA-Z0-9_]+/
condition: ("(" string COMPARATOR string ")"?)*
node: property condition?
property: CNAME
string: ESCAPED_STRING | int
int: /[0-9]+/
%import common.WS
%import common.ESCAPED_STRING
%ignore WS
"""
)

# l = parser.parse("{ Roboflow -> Owned -> WorksFor -> IsDescribedBy } !")
# l = parser.parse('{ CLIP -> Authors ("Citations" > "3") }')
# l = parser.parse("{ Roboflow -> Developer } INTERSECTION { MetaAI -> Developer }")
# l = parser.parse("{ IndieWeb <-> Roboflow }")
# l = parser.parse("{ MetaAI -> Citations -> Enjoys }")
# l = parser.parse("{ Events Series -> Organizer}!")
# l = parser.parse('{ Roboflow ("EntityType" = "Company") }')
# l = parser.parse(
#     '{ Roboflow ("EntityType" = "Company") -> WorksFor ("Enjoys" = "Coffee") -> Hobbies }'
# )
l = parser.parse("{ Roboflow -> WorksFor }!")

# parse tree
parent_tree = l.children

final_results = []
operand = None
expand = False


def eval_condition(condition, node):
    result = []

    term1 = condition.children[0].children[0].value.strip().strip('"')
    comparator = condition.children[1].value.strip()
    term2 = condition.children[2].children[0].value.strip().strip('"')

    print("Evaluating condition", term1, comparator, term2, "on", node)

    if isinstance(node, list):
        for item in node:
            if not kg.get_nodes(item).get(term1):
                print("Node", item, "does not have property", term1)
                continue

            evaluated_term = kg.get_nodes(item)[term1][0]

            if comparator == "=" and evaluated_term == term2:
                result.append(item)
            elif comparator == "!=" and evaluated_term != term2:
                result.append(item)
            elif (
                comparator == ">"
                and isinstance(evaluated_term, int)
                and evaluated_term > int(term2)
            ):
                result.append(item)
            elif comparator == ">" and len(list(set(evaluated_term))) > int(term2):
                result.append(item)
            elif (
                comparator == "<"
                and isinstance(evaluated_term, int)
                and evaluated_term < int(term2)
            ):
                result.append(item)
            elif comparator == "<" and len(list(set(evaluated_term))) < int(term2):
                result.append(item)
    else:
        # print(node, term1, kg.get_nodes_by_connection(node, term1), "not found")
        if not kg.get_nodes_by_connection(node, term1):
            print("Node", node, "does not have property", term1)
            return []
        
        evaluated_term = kg.get_nodes(node)[term1][0]

        if comparator == "=" and evaluated_term == term2:
            result.append(node)
        elif comparator == "!=" and evaluated_term != term2:
            result.append(node)
        elif comparator == ">" and len(list(set(evaluated_term))) > int(term2):
            result.append(item)
        elif (
            comparator == "<"
            and isinstance(evaluated_term, int)
            and evaluated_term < int(term2)
        ):
            result.append(item)
        elif comparator == "<" and len(list(set(evaluated_term))) < int(term2):
            result.append(item)

    print("Result", result)

    return result


expand = False
count = False
question = False


def get_result(parent_tree):
    global operand
    global expand
    global count
    global question

    is_evaluating_relation = False
    relation_terms = []

    for child in parent_tree:
        children = child.children

        if len(children) == 0:
            continue

        node = None
        result = None

        # search for evaluating relation
        for i in range(len(children)):
            if isinstance(children[i], lark.tree.Tree):
                print(children[i])
                if children[i].data == "interrelation":
                    is_evaluating_relation = True
                    break

        for i in range(len(children)):
            if isinstance(children[i], lark.tree.Tree):
                if children[i].data == "property":
                    property = children[i].children[0].value.strip()
                    print("Getting", property, "of", node)
                    if isinstance(node, list):
                        result = [kg.get_nodes_by_connection(n, property) for n in node]
                        result = [item for sublist in result for item in sublist]
                    else:
                        result = kg.get_nodes_by_connection(node, property)
                    node = result
                elif children[i].data == "node":
                    if is_evaluating_relation:
                        relation_terms.append(children[i].children[0].children[0].value)
                        if len(relation_terms) == 2:
                            print("Getting connection between", relation_terms)
                            result = kg.get_connection_paths(
                                relation_terms[0], relation_terms[1]
                            )
                            node = result
                            is_evaluating_relation = False
                            relation_terms = []
                            continue
                    print("Getting node", children[i].children[0])
                    node = children[i].children[0].children[0].value.strip()
                    property = children[i].children[0].children[0].value.strip()
                    if (
                        len(children[i].children) > 1
                        and len(children[i].children[1].children) > 0
                    ):
                        print("Getting", property, "of", result)
                        all_items = []
                        if result:
                            if (
                                len(
                                    [
                                        kg.get_nodes(r)[node]
                                        for r in result
                                        if node in kg.get_nodes(r)
                                    ]
                                )
                                == 0
                            ):
                                result = result[property]
                            else:
                                result = [
                                    kg.get_nodes(r)[node]
                                    for r in result
                                    if node in kg.get_nodes(r)
                                ][0]
                            condition = children[i].children[1]
                            result = eval_condition(condition, result)
                            all_items.append(result)
                        else:
                            condition = children[i].children[1]
                            result = eval_condition(condition, node)
                            print(result)
                            all_items.append(result)
                        # flatten list
                        result = [item for sublist in all_items for item in sublist]
                    else:
                        # print('x')
                        # if no result, get all properties
                        if not result:
                            result = kg.get_nodes(node)
                            print("Result", result)
                        # if result is list:
                        elif isinstance(result, list):
                            result = [
                                kg.get_nodes(r)[node]
                                for r in result
                                if node in kg.get_nodes(r)
                            ]
                            result = [item for sublist in result for item in sublist]
                            print("Result", result)
                        else:
                            result = result[node]

                    if result == []:
                        return []
                else:
                    print("Unknown data type", children[i].data)
            else:
                if children[i].type == "EXPAND":
                    expand = True
                    continue
                if children[i].type == "COUNT":
                    count = True
                    continue
                if children[i].type == "QUESTION":
                    question = True
                    continue
                if children[i].type == "operand":
                    operand = children[i].value
                    continue

        final_results.append(result)


get_result(parent_tree)
# print(get_connection_paths(kg, "Roboflow", "MetaAI"))

# exit()

# parse operand
if operand == "INTERSECTION":
    final_result = set(final_results[0]).intersection(set(final_results[1]))
else:
    try:
        final_result = set(final_results[0]).union(set(final_results[1]))
    except:
        if len(final_results) == 0:
            final_result = []
        else:
            final_result = final_results[0]
if count:
    final_result = len(final_result)
    print(final_result)
elif question:
    print(bool(final_result))
elif expand:
    # if dict, print and exit
    if isinstance(final_result, dict):
        print(final_result)
        exit()

    acc = []
    print("Final result", final_result)

    for item in final_result:
        nodes = kg.get_nodes(item)
        if not nodes:
            continue
        acc.append({item: nodes})

    acc = sorted(acc, key=lambda x: list(x.keys())[0])

    print(acc)
else:
    print(final_result)
