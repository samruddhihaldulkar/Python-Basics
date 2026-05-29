'''Create a nested dictionary storing:
course name
faculty
credits
enrolled students
Find the course with highest enrolled students. '''
#content formation
'''
data = {
    course_data:{
        course_name{
            faculty:"mr xyz",
            students:{
                stu_name:credit
            }
        }
    }
}
'''



key1_dict = {}
num_key1 = int(input("Enter the number of key1 entries: "))

for key1_index in range(1, num_key1 + 1):
    key1 = input(f"Enter the name of key1 entry {key1_index}: ")
    value1 = input(f"Enter the value1 for key1 entry {key1_index}: ")

    key2_dict = {}
    num_key2 = int(input("Enter the number of key2 entries for this key1: "))

    for key2_index in range(1, num_key2 + 1):
        key2 = input(f"Enter the name of key2 entry {key2_index}: ")
        value2 = int(input(f"Enter the value2 for {key2}: "))
        key2_dict[key2] = value2

    key1_dict[key1] = {
        "value1": value1,
        "key2_dict": key2_dict,
    }

final_summary = {}
if key1_dict:
    max_key1 = None
    max_value2_count = -1

    for key1, value1_details in key1_dict.items():
        value2_count = len(value1_details["key2_dict"])
        if value2_count > max_value2_count:
            max_value2_count = value2_count
            max_key1 = key1

    final_summary = {
        "key1_dict": key1_dict,
        "highest_enrollment": {
            "key1": max_key1,
            "value1": key1_dict[max_key1]["value1"],
            "value2_count": max_value2_count,
            "key2_dict": key1_dict[max_key1]["key2_dict"],
        },
    }

print("\nFinal summary:")
print(final_summary) 