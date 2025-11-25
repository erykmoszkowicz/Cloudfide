from test_virtual_column import *


all_tests = [
    test_sum_of_two_columns,
    test_multiplication_of_two_columns,
    test_subtraction_of_two_columns,
    test_empty_result_when_invalid_labels,
    test_empty_result_when_invalid_rules,
    test_when_extra_spaces_in_rules
]

passed_count = 0
failed_tests = []

# Iterate over all tests
for test_func in all_tests:
    test_name = test_func.__name__
    # Passed tests
    try:
        test_func()
        print(f"Passed: {test_name}")
        passed_count += 1
    
    # Failed tests
    except AssertionError as e:
        print(f"Failed: {test_name}")
        failed_tests.append((test_name, e))

    except Exception as e:
        print(f"Error: {test_name}: {type(e).__name__}")
        failed_tests.append((test_name, e))

# Number of total tests
total_tests = len(all_tests)

# Final tests results
if passed_count == total_tests:
    print(f"\nAll {total_tests} tests passed.")

else:
    failed_count = total_tests - passed_count
    print(f"Failed: {failed_count}/{total_tests} tests.")
    
    for name, error in failed_tests:
        print(f"\n[{name}]")
        print(str(error).split('\n', 1)[0]) 