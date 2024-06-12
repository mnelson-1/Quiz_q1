import sys
import time

def strip_string(s):
    return s.strip()

class DuplicateInt:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = input_file_name[:-3] + 'txt_duplicates.txt'

    def process_file(self, file_lines):
        count_dict = {}
        for line in file_lines:
            stripped_line = strip_string(line)
            if not stripped_line:
                continue  # Skip empty lines or lines with only whitespaces

            parts = stripped_line.split()
            if len(parts) != 1:
                continue  # Skip lines with multiple integers

            try:
                number = int(parts[0])
                if number in count_dict:
                    count_dict[number] += 1
                else:
                    count_dict[number] = 1
            except ValueError:
                continue  # Skip lines with non-integer inputs

        # Get only the numbers that have a count greater than 1
        duplicates = [number for number, count in count_dict.items() if count > 1]
        return sorted(duplicates)

    def read_and_write_to_file(self):
        try:
            with open(self.input_file_name, 'r') as input_file:
                raw_data = input_file.readlines()

            duplicate_numbers = self.process_file(raw_data)

            with open(self.output_file_name, 'w') as output_file:
                for number in duplicate_numbers:
                    output_file.write(f'{number}\n')
        except FileNotFoundError:
            print(f"No such file or directory: {self.input_file_name}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No file name provided")
        print("Usage: python -u DuplicateInt.py <input_file_name>")
    else:
        start_time = time.time()
        input_file_name = sys.argv[1]

        duplicate_int_processor = DuplicateInt(input_file_name)
        duplicate_int_processor.read_and_write_to_file()

        end_time = time.time()
        print(f"Elapsed time: {end_time - start_time} seconds")

