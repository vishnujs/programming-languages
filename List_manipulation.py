#List manipulation Coding problem #1

#Input the size of a list with size N, Based on the input instuctions manipulate the list,
#	Left : left rotation
#	Right : right rotation
#	Update pos val: update the value at the given position
#	Increment pos: increment the value by 1 at the given position
#	? pos: displays the position
	
  
  
  
n_elements = int(input())
elements_string = input()
list_input = [int(element) for element in elements_string.rstrip().split(" ")]
no_queries = int(input())
for i in range(no_queries):
    input_choice = input()
    choice_list = input_choice.rstrip().split(" ")
    if choice_list[0] == "Left":
        left_shited = list_input[1:]
        left_shited.append(list_input[0])
        list_input = left_shited
    elif choice_list[0] == "Right":
        left_shited = [list_input[len(list_input)-1]]+list_input[:-1]
        list_input = left_shited
    elif choice_list[0] == "Update":
        list_input[int(choice_list[1])-1] = int(choice_list[2])
    elif choice_list[0] == "Increment":
        list_input[int(choice_list[1])-1] = list_input[int(choice_list[1])-1]+1
    elif choice_list[0] == "?":
        print(list_input[int(choice_list[1])-1])
