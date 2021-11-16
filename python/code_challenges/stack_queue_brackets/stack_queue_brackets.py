
def validate_brackets(input_data):
    stack = []
    for i in input_data:

        if i in ["(", "{", "["]:
            stack.append(i)

        elif i in [")", "}", "]"]:
            if not stack:

                return False

            item = stack.pop()

            if item == '(':

                if i != ")":

                    return False

            if item == '{':


                if i != "}":

                    return False

            if item == '[':

                if i != "]":

                    return False

    return True



if __name__=='__main__':
  string1 = "{g}"
  print(validate_brackets(string1))

  string2 = "{[][{op}}"
  print(validate_brackets(string2))


