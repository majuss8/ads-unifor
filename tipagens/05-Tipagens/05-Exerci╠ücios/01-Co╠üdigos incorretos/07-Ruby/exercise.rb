class Person
    attr_accessor :name, :age

    def initialize(name, age)
        @name = name
        @age = age
    end
end

def display_info(person)
    raise TypeError, "Expected Person instance" unless person.is_a?(Person)
    puts "Name: #{person.name}, Age: #{person.age}"
end

alice = Person.new("Alice", 30)
display_info(alice) # alice é uma classe/objeto Person

invalid_data = [1, 2, 3]
display_info(invalid_data) # invalid_data não é uma classe/objeto Person

result = "The number is: " + 10
puts result
