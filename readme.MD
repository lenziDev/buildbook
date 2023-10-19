# BuildBook Music App
This command-line application allows you to apply a batch of changes to a music service dataset.

## How to Run the Application
1. **Requirements:**
    - Python (3.x recommended)
2. **Installation:**
    - No additional installation is required.
3. **Running the Application:**
    - Open a terminal or command prompt.
    - Navigate to the directory containing main.py and your input files.
    - Use the following command template:
    ```bash
    python main.py <input-file> <changes-file> <output-file>
    ```
    - Example:
    ```bash
    python main.py spotify.json changes.json output.json
    ```
    - This will process the changes and save the updated dataset to output.json.

## How to Run the Tests
1. **Requirements:**
    - pytest (install using pip install pytest if not already installed) or you can just run
    ```
    pip install -r requirements.txt
    ```
2. **Running the Tests:**
    - Open a terminal or command prompt.
    - Navigate to the directory containing main_test.py and your test files.
    - Use the following command:
    ```
    pytest
    ```
    - This will execute the tests and display the results.

## Scaling the Application
If you need to scale the application to handle larger input files or changes files, consider the following steps:

1. **Optimize Data Processing:**

    - Ensure that your data processing algorithms are efficient. Avoid nested loops and consider using appropriate data structures.

2. **Memory Management:**

    - If dealing with very large files, consider reading and processing data in chunks to reduce memory usage.

3. **Parallelization:**

    - Depending on the nature of your application, you may explore parallel processing techniques to speed up operations.

4. **Error Handling and Logging:**

    - Implement robust error handling and logging to identify and address any potential issues with large datasets.

5. **Testing and Profiling:**

    - Conduct thorough testing with large datasets to identify performance bottlenecks. Use profiling tools to analyze code performance.

6. **Use of External Libraries:**

    - Consider using specialized libraries or tools for handling large datasets, if applicable.

## Total time dedicated

It was dedicated 01:25 hours for this exercise.