class SampleObject:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

sample_object = SampleObject()
dict_from_object = vars(sample_object)

print("Dictionary from the object's fields:", dict_from_object)
