# polymorphisme berarti memiliki bentuk yang banyak atau berbeda-beda
# istilah ini mengacu pada kemampuan fungsi dengan nama yang sama yantk membawa
# fungsionalitas yang berbeda secara bersamaan, sehingga menciptakan struktur
# yang dapat menggunaan banyak bentuk
# polymorphism mengacu pada method yang dimiliki oleh child class

class Bird:
    def intro(self):
        print("There are different types of birds")

    def flight(self):
        print("Most of birds can fly but some can not")


class parrot(Bird):
    def flight(self):
        print("Parrots can fly")


class penguin(Bird):
    def flight(self):
        print("penguins can not fly")


obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()

obj_bird.intro()
obj_bird.flight()

obj_parr.intro()
obj_parr.flight()

obj_peng.intro()
obj_peng.flight()

obj_peng.intro()
obj_peng.flight()
