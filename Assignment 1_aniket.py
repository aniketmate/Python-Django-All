
class List_Operations:
    """Perform all built in methods for list"""

    def __init__(self, lst):
        self.List = lst

    def list_append(self, val):
        self.List.append(val)
        print(f"My List after performing append operation----{My_List} ")

    def list_extend(self, val):
        self.List.extend(val)
        print(f"My List after performing extend operation----{My_List} ")

    def list_insert(self, n, val):
        self.List.insert(n, val)
        print(f"My List after performing insert operation----{My_List} ")

    def list_remove(self, val):
        self.List.remove(val)
        print(f"My List after performing remove operation----{My_List} ")

    def list_sort(self):
        self.List.sort()
        print(f"My List after performing sort operation----{My_List} ")

    def list_pop(self):
        p = self.List.pop()
        print(
            f" After performing pop operation the element removed from list is----{p} ")

    def list_reverse(self):
        self.List.reverse()
        print(f"My List after performing reverse operation----{My_List} ")

    def list_count(self, val):
        s = self.List.count(val)
        print(f" After performing count operation----{val} occurs {s} times ")

    def list_index(self, val):
        s = self.List.index(val)
        print(f" After performing index operation----{val} occurs {s} index ")

    def list_clear(self):
        s = self.List.clear()
        print(f"My List after performing clear operation----{My_List} ")


My_List = [2, 5, 3, 4, 8, 6, 9, 7, 5]
l = List_Operations(My_List)


l.list_append(12)
l.list_extend("Aniket")
l.list_insert(4, "Mate")
l.list_remove(8)
l.list_sort()
l.list_pop()
l.list_reverse()
l.list_count(5)
l.list_index(5)
l.list_clear()


"""
 OUTPUT
            
My List after performing append operation----[2, 5, 3, 4, 8, 6, 9, 7, 12]
My List after performing extend operation----[2, 5, 3, 4, 8, 6, 9, 7, 'A', 'n', 'i', 'k', 'e', 't']
My List after performing insert operation----[2, 5, 3, 4, 'Mate', 8, 6, 9, 7]
My List after performing remove operation----[2, 5, 3, 4, 6, 9, 7]
My List after performing sort operation----[2, 3, 4, 5, 6, 7, 8, 9]
After performing pop operation the element removed from list is----5
My List after performing reverse operation----[7, 9, 6, 8, 4, 3, 5, 2]
After performing count operation----5 occurs 2 times
After performing index operation----5 occurs 1 index
My List after performing clear operation----[]

"""
# -----------------------------------------------------------------------------------------------------------------------------------------------


class Set_Operations:
    """Perform all built in methods for set"""

    def __init__(self, st):
        self.Set = st

    def set_add(self, val):
        self.Set.add(val)
        print(f"After performing add operation we get ----{set}")

    def set_update(self, val):
        self.Set.update(val)
        print(f"After performing update operation we get ----{set}")

    def set_pop(self):
        p = self.Set.pop()
        print(
            f" After performing pop operation the element removed from set is----{p} ")

    def set_remove(self, val):
        self.Set.remove(val)
        print(f" After performing remove operation we get----{set} ")

    def set_discard(self, val):
        self.Set.discard(val)
        print(f" After performing discard operation we get----{set} ")

    def set_clear(self):
        self.Set.clear()
        print(f" After performing clear operation we get----{set} ")


set = {20, 25, 55, 35, 65, 60}
s1 = Set_Operations(set)

s1.set_add(45)
s1.set_update("Aniket")
s1.set_pop()
s1.set_remove(25)
s1.set_discard(35)
s1.set_clear()


# Output

# After performing add operation we get ----{65, 35, 45, 20, 55, 25, 60}
# After performing update operation we get ----{65, 'n', 35, 'k', 'e', 20, 't', 55, 25, 60, 'A', 'i'}
# After performing pop operation the element removed from set is----65
# After performing remove operation we get----{65, 35, 20, 55, 60}
# After performing discard operation we get----{65, 20, 55, 25, 60}
# After performing clear operation we get----set()


# -------------------------------------------------------------------------------------------------------------------------------------------

class Dictionary_Operations:
    """Perform all built in methods for set"""

    def __init__(self, dict):
        self.Dict = dict

    def clear_dict(self):
        self.Dict.clear()
        print(f"After performing clear operation we get-----{My_Dict}")

    def get_dict(self, val):
        g = self.Dict.get(val)
        print(f"After performing get operation we get-----{g}")

    def pop_dict(self, val):
        p = self.Dict.pop(val)
        print(f"After performing pop operation we get-----{p}")

    def popitem_dict(self):
        self.Dict.popitem()
        print(f"After performing popitems operation we get-----{My_Dict}")

    def keys_dict(self):
        k = self.Dict.keys()
        print(f"After performing keys operation we get-----{k}")

    def values_dict(self):
        v = self.Dict.values()
        print(f"After performing values operation we get-----{v}")

    def items_dict(self):
        I = self.Dict.items()
        print(f"After performing items operation we get-----{I}")

    def setdefault_dict(self, key, val):
        self.Dict.setdefault(key, val)
        print(
            f"After performing set default operation we get for key {key}-----{self.Dict.get(key)}")

    def update_dict(self, val):
        self.Dict.update(val)
        print(f"After performing update operation we get for key {My_Dict}")


My_Dict = {1: "Apple", 2: "Ball", 3: "Cat"}

d = Dictionary_Operations(My_Dict)

d.clear_dict()
d.get_dict(2)
d.pop_dict(3)
d.popitem_dict()
d.keys_dict()
d.values_dict()
d.items_dict()
d.setdefault_dict(2, "Ball")
d.update_dict([(4, "dog")])


# OUTPUT
# After performing clear operation we get-----{}
# After performing get operation we get-----Ball
# After performing pop operation we get-----Cat
# After performing popitems operation we get-----{1: 'Apple', 2: 'Ball'}
# After performing keys operation we get-----dict_keys([1, 2, 3])
# After performing values operation we get-----dict_values(['Apple', 'Ball', 'Cat'])
# After performing items operation we get-----dict_items([(1, 'Apple'), (2, 'Ball'), (3, 'Cat')])
# After performing set default operation we get for key 2-----Ball
# After performing update operation we get for key {1: 'Apple', 2: 'Ball', 3: 'Cat', 4: 'dog'}


# -----------------------------------------------------------------------------------------------------------------------------------------

class String_Operations:
    """Perform all built in methods for string"""

    def __init__(self, str):
        self.string = str

    def find_string(self, val):
        r = self.string.find(val)
        if r == -1:
            print(
                f"After performing find operation we did not find the {val} in the available string")
        else:
            print(
                f"After performing find operation we found the substring at position {r} in the available string")

    def count_string(self, val):
        c = self.string.count(val)
        print(f"After performing count operation we get {c} ")

    def split_string(self, val):
        s = self.string.split(val)
        print(f"After performing split operation we get  {s} ")

    def join_string(self, val):
        j = self.string.join(val)
        print(f"After performing join operation we get  {j} ")

    def case_string(self):
        u = self.string.upper()
        print(f"After performing upper case operation we get  {u} ")
        l = self.string.lower()
        print(f"After performing lower case operation we get  {l} ")

    def strip_string(self):
        s = self.string.lstrip()
        print(f"After performing strip operation we get  {s} ")

    def start_end_string(self, val):
        s = self.string.startswith(val)
        print(f"After performing starting operation we get  {s} ")
        e = self.string.endswith(val)
        print(f"After performing ending operation we get  {e} ")

    def replace_string(self, x, y):
        r = self.string.replace(x, y)
        print(f"After performing replace operation we get  {r} ")


My_String = ("My name is Aniket Mate")
s1 = String_Operations(My_String)


s1.find_string("is")
s1.find_string("are")
s1.count_string("M")
s1.split_string(" ")
s1.join_string("----")
s1.case_string()
s1.start_end_string("My")
s1.strip_string()
s1.replace_string("My", "Your")


# OUTPUT
# After performing find operation we found the substring at position 8 in the available string
# After performing find operation we did not find the are in the available string
# After performing count operation we get 2
# After performing split operation we get  ['My', 'name', 'is', 'Aniket', 'Mate']
# After performing join operation we get  -My name is Aniket Mate-My name is Aniket Mate-My name is Aniket Mate-
# After performing upper case operation we get  MY NAME IS ANIKET MATE
# After performing lower case operation we get  my name is aniket mate
# After performing starting operation we get  True
# After performing ending operation we get  False
# After performing strip operation we get  My name is Aniket Mate
# After performing replace operation we get  Your name is Aniket Mate

# ---------------------------------------------------------------------------------------------------------------------------------------------
