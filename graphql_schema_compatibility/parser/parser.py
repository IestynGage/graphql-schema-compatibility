from io import TextIOWrapper


with open('/Users/iestyngage/git/graphql-schema-compatibility/tests/resources/simple-schema/schema-1.graphql') as f:
  lines = f.readlines()
  print(lines)

class SchemaParser:
  def __init__(self):
    print("Parser defined")

  def parse(self, text_file: TextIOWrapper):
    lines = text_file.readlines()
    print(lines)
        
  def __str__(self):
    return f"MyClass instance: parameter1={self.parameter1}, parameter2={self.parameter2}"
    
if __name__ == "__main__":
  instance = SchemaParser()
